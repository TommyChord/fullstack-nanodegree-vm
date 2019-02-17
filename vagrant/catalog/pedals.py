from flask import request, g
from flask import Flask, jsonify, render_template, flash, redirect, url_for
from flask import session as login_session
from flask import make_response
from models import Base, Category, Item, User
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, exists
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import random
import string
import httplib2
import json
import requests

engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Tommys Pedal Show"


@app.route('/catalog/json')
def categories_json():
    categories = session.query(Category).all()
    return jsonify(Category=[i.serialize for i in categories])


@app.route('/catalog/all/json')
def all_items_json():
    items = session.query(Item).all()
    return jsonify(Item=[i.serialize for i in items])


@app.route('/catalog/<category_id>/json')
def category_items_json(category_id):
    items = session.query(Item).filter_by(category_id=category_id).all()
    return jsonify(Item=[i.serialize for i in items])


# Create anti-forgery state token
@app.route('/login')
def show_login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']

    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')

    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = get_user_id(data["email"])
    if not user_id:
        user_id = create_user(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;'
    output += '-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("You are now logged in as %s" % login_session['username'])

    return output

# User Helper Functions


def create_user(login_session):
    new_user = User(name=login_session['username'], email=login_session[
        'email'], picture=login_session['picture'])
    session.add(new_user)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def get_user_info(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def get_user_id(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/disconnect')
def disconnect():
    # Only disconnect a connected user.
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']

        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('catalog'))

    else:
        flash("You were not logged in to begin with!")
        print login_session
        return redirect(url_for('catalog'))


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/')
@app.route('/catalog')
def catalog():
    categories = session.query(Category).all()
    items = session.query(Item).order_by(Item.id.desc()).limit(15)

    return render_template('catalog.html', categories=categories, items=items)


@app.route('/catalog/<category>')
def show_items(category):
    categories = session.query(Category).all()
    selected_category = session.query(Category).filter_by(name=category).one()
    items = session.query(Item).filter_by(category_id=selected_category.id).all()

    return render_template('items.html',
                           categories=categories,
                           items=items,
                           selected_category=selected_category)


@app.route('/catalog/<category>/<title>/delete', methods=['GET', 'POST'])
def delete_item(category, title):
    # Check if the user is logged in
    if 'username' not in login_session:
        flash('You are required to login before working with pedal items')
        return redirect('/login')

    item = session.query(Item).filter_by(title=title).one()

    # Verify if user is the creator and allowed to edit
    if int(login_session['user_id']) == item.user_id:
        if request.method == 'POST':
            session.delete(item)
            session.commit()
            return redirect(url_for('show_items', category=category))
        else:
            return render_template('delete_item.html', item=item)
    else:
        flash('You are not the creator of this item so you are not allowed to '
              'delete. Please contact %s (%s) to have the pedal deleted.'
              % item.user.name, item.user.email)
        return render_template('item_details.html', item=item)


@app.route('/catalog/new', methods=['GET', 'POST'])
def new_item():
    if 'username' not in login_session:
        return redirect('/login')

    categories = session.query(Category).order_by(Category.name.asc())

    if request.method == 'POST':
        pedal_exist = session.query(exists().where(Item.title == request.
                                                   form['title'])).scalar()
        if pedal_exist:
            flash('This pedal (%s) already exist and cannot be duplicated'
                  % request.form['title'])
            return render_template('new_item.html', categories=categories)
        else:
            new_pedal = Item(title=request.form['title'],
                             description=request.form['description'],
                             category_id=request.form['category'],
                             user_id=login_session['user_id'])

            session.add(new_pedal)
            session.commit()
            flash('New pedal %s Successfully Created' % new_pedal.title)
            return redirect(url_for('catalog'))
    else:
        return render_template('new_item.html', categories=categories)


@app.route('/catalog/<category>/<title>/edit', methods=['GET', 'POST'])
def edit_item(category, title):
    if 'username' not in login_session:
        flash('You are required to login before working with pedal items')
        return redirect('/login')

    item = session.query(Item).filter_by(title=title).one()

    # Verify if user is the creator and allowed to edit
    if int(login_session['user_id']) == item.user_id:
        categories = session.query(Category).order_by(Category.name.asc())

        if request.method == 'POST':
            print "POST request"
            if request.form['title']:
                item.title = request.form['title']
            if request.form['description']:
                item.description = request.form['description']
            if request.form['description']:
                item.category_id = request.form['category']
            session.commit()

            flash('Pedal %s Successfully Updated' % request.form['title'])
            return redirect(url_for('item_details',
                                    category=item.category.name,
                                    title=item.title))
        else:
            return render_template('edit_item.html', categories=categories,
                                   item=item)
    else:
        flash('You are not the creator of this item so you are not allowed to '
              'edit. Please contact %s (%s) if updates are required'
              % item.user.name, item.user.email)
        return render_template('item_details.html', item=item)


@app.route('/catalog/<category>/<title>')
def item_details(category, title):
    item = session.query(Item).filter_by(title=title).one()
    return render_template('item_details.html', item=item)


if __name__ == '__main__':
    app.secret_key = 'You_Never_Guess_My_Key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
