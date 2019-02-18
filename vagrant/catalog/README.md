# Catalog Project
The goal of this project is to build a web based GUI on top of a database. The web site has to do authentication against
a third party vendor (I have chosen Google). It also has to do authorization to determine if a user can edit or delete 
items from the database. The rules are:
- If the user is not logged in, he/she can only view information
- A user that is logged in can add new items to the database
- A user can only edit or delete items that was created by themselves, no other items.

I have chosen to build a site that contains information of guitar pedals, as playing guitar is my #1 hobby.

### Requirements
* Vagrant
* Vagrant environment provided by Udacity
* Python 2.7
* SQLAlchemy
* Flask

### Setup
1. Bring up the virtual machine with ````vagrant up```` if it's not running already.
2. SSH to your vagrant environment issuing the ````vagrant ssh```` command
3. To load some initial data, cd into the /vagrant/catalog/ directory and run the command 
    ````python lotsofcategories.py````.
4. Start the website by running `````python pedals.py`````

### Start the application
SSH to your vagrant environment if you are not there already by issuing the ````vagrant ssh```` command and then 
````cd /vagrant/catalog/```` to get into the directory where the application exist. From there, execute the following
command on the commandline:

````python pedals.py````

This command will start the application which can then be accessed from your favourite browser on the address of
[localhost:8000](http://localhost:8000)

### Application functionality
From the initial page [localhost:8000](http://localhost:8000) you will see a list of pedal categories on the left side, 
and on the right side the last 15 added pedals. From there you can click on a category either on the left side, or in 
the brackets next to the pedal name. This will list all pedals in the selected category. 
You can also click directly on the pedal name to see more details of that pedal, and information on who added the pedal 
to the system.

If you are logged in you will see a green button "Add New" that allows you to add a new pedal to the system. This is 
visible on both the home page and under the pedal listing of each category. 

If you are the one that added the pedal to the system, on the details page you will have two buttons. One for updating 
the pedal information, and one for deleting the pedal from the system. If you are not the person adding the pedal you 
will not see those buttons on the page.

### RESTful API endpoints
The application also provides other developers a way to fetch information from this site to use in their own 
applications. The output from the APIs are JSON files, and there are currently three APIs available:
1. [/catalog/json](http://localhost:8000/catalog/json) This endpoint will list all available pedal categories.
2. [/catalog/\<categoryID\>/json](http://localhost:8000/catalog/1/json) This endpoint will list all pedals in the chosen
category, where "categoryID" is the ID of the pedal category. This can be found from the endpoint above (1).
3. [/catalog/all/json](http://localhost:8000/catalog/all/json) This endpoint will list out all pedals we have in the 
system, grouped by pedal category.