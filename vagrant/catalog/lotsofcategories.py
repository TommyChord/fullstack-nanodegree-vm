from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Category, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

# Create a DBSession() instance
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Add an initial user
user1 = User(name='Mr. Nerdy', email='nerdy@categories.com',
             picture='/static/img/nerd.png')
session.add(user1)
session.commit()

# Load category "Amp Simulator"
category01 = Category(name="Amp Simulator", user_id=1)
session.add(category01)
session.commit()

# Load items for category "Amp Simulator"
description = ("The Behringer GDI21 V-Tone is an analog guitar modelling pream"
               "p/stompbox that features authentic V-TONE modelling technology"
               " and DI recording output. Delivering a total of 27 possible "
               "configurations, the GDI21 recreates three of the most "
               "sought-after classic guitar amps with three gain modes and "
               "three microphone placements. Complete with dedicated controls,"
               " a ground lift switch and dual DI mode for direct recording, "
               "the Behringer GDI21 V-TONE stompbox is perfect for both live "
               "performances and studio sessions.")
item01 = Item(title="Behringer GDI21 V-Tone Guitar Preamp",
              description=description,
              category=category01,
              user=user1)

session.add(item01)
session.commit()

description = ("The Behringer ADI21 V-Tone Acoustic Preamp is designed to be "
               "used with guitars featuring piezo pickups and delivers a "
               "natural, acoustic sound full of life. The acoustic premp adds "
               "a richness to your overall acoustic performance and features "
               "an active direct injection box with proprietary mic emulation "
               "circuitry. A full 3-band EQ offers sweepable mids and blend "
               "control, allowing guitarists to mix their sound to reach their"
               " desired tones. The ADI21 is powered by a 9-volt battery or "
               "PSU-SB DC power supply (sold separately).")
item02 = Item(title="Behringer ADI21 V-Tone Acoustic Preamp",
              description=description,
              category=category01,
              user=user1)

session.add(item02)
session.commit()

description = ("The Behringer TM300 Tube Amp Modeller Pedal delivers true "
               "modeling technology with up to 27 different configurations. "
               "Guitarists can find their perfect tube amp sounds ranging from"
               " clean tones through to heavy distortion with 3 x classic "
               "guitar amps, gain modes and mic placements. Dedicated drive, "
               "high and low EQ, level, mic, model and amp controls ensure "
               "excellent sound shaping possibilities whilst an LED shows when"
               " the pedal is active and offers a battery check. With an "
               "electronic on and switch, the TM300 promises maximum signal "
               "integrity in bypass mode and operates on either a 9-volt "
               "battery or the Behringer PSU-SB DC power supply (sold "
               "separately).")
item03 = Item(title="Behringer TM300 Tube Amp Modeller Pedal",
              description=description,
              category=category01,
              user=user1)

session.add(item03)
session.commit()

description = ("The Mooer MAG1 Acoustikar Acoustic Guitar Simulator Pedal is "
               "loaded with 3 different acoustic guitar effects so that you "
               "can enhance your sound with a whole new dimension. The effects"
               " include Piezo for clear articulation, Standard for a classic "
               "acoustic tone or Jumbo for a full-bodied, resonant effect. For"
               " even more versatility, there are 3 controls that are simple, "
               "and offer easy operation yet they hold a variety of tonal "
               "possibilities. The Level knob adjusts the effect output, "
               "whilst the Body control adjusts the resonance and the Top "
               "alters the sound's overall character and harmonics. The "
               "Acoustikar Pedal features True Bypass which preserves the "
               "tone, and eliminates signal interference when the unit is not "
               "in use.")
item04 = Item(title="Mooer MAG1 Acoustikar Acoustic Guitar Simulator Pedal",
              description=description,
              category=category01,
              user=user1)

session.add(item04)
session.commit()

description = ("The Mooer TresCab Speaker Simulation Pedal is loaded with 5 "
               "different cab models for you to simulate, without the need for"
               " carrying around a big, heavy amp. The cabinet options include"
               " 1x8'' and 1x10'' combo amps, open 1x12'' and 2x12'' modes, "
               "and a 4x12'' closed mode, which can be selected via the simple"
               " Mode control. The TresCab's other versatile controls consist "
               "of Low/Dis, High/Pos and a mode switch to select either EQ "
               "mode for making tonal adjustments to the effect, or Mic mode "
               "which allows you to place and alter a microphone. The TresCab "
               "Speaker Simulator also features True Bypass which eliminates "
               "signal interference when the unit is not in use, to preserve "
               "the tone.")
item05 = Item(title="Mooer TresCab Speaker Simulation Pedal",
              description=description,
              category=category01,
              user=user1)

session.add(item05)
session.commit()

description = ("The Hughes & Kettner Red Box 5 is an award winning speaker "
               "simulation, emulating the true sound of a guitar cabinet. The "
               "Red Box 5 features a new filtering option which can be used "
               "for small/large housing, modern/vintage speakers, and "
               "loose/tight response of the cabinet. As well as this, the Red "
               "Box has clear, direct sound and room emulating software "
               "plugins to enhance the sound quality and overall experience. "
               "As an added bonus, the Red Box is powered with phantom powered"
               " as well as an external power supply for extra power and "
               "versatility. ")
item06 = Item(title="Hughes & Kettner Red Box 5",
              description=description,
              category=category01,
              user=user1)

session.add(item06)
session.commit()

description = ("The Carl Martin Rock Bug Amp/Speaker Simulator faithfully "
               "emulates both open and closed speaker cabinets, producing a "
               "variety of tube-like tones. The Rock Bug features a toggle "
               "switch that lets you choose between an open or a closed "
               "cabinet simulation. This amp simulator features a headphone "
               "input and allows you to play your guitar anywhere without "
               "disturbing others. The Carl Martin Rock Bug can be used as a "
               "backup amp if your main amp stops working during a live "
               "performance. Finally, the Rock Bug also features a XLR output "
               "and can be easily connected to a desk during live performances"
               " and recording sessions.")
item07 = Item(title="Carl Martin Rock Bug Amp/Speaker Simulator",
              description=description,
              category=category01,
              user=user1)

session.add(item07)
session.commit()

description = ("So much power in one little box. The Hotone Binary Amp "
               "Modeller is here to bring you mountains of tone, giving you to"
               " access 16 different amps at the press of a switch. With it "
               "sitting on your pedalboard, you'll have the ultimate control "
               "over your tone, being able to select your amp settings with "
               "ease. From amps like a clean jazz amp and Fender '65 Twin "
               "Reverb to the Mesa/Boogie Dual Rectifier and Marshall JCM 800,"
               " there are many different options, along with matched cab "
               "simulators, for you to choose from.<br>"
               "Modern versatility. With multiple control dials which you can "
               "use to shape/EQ your sound, you'll have total flexibility over"
               " your music making. Having new tones at your disposal, you'll "
               "find the doors to creativity are well and truly open, and when"
               " performing live you'll be able to instantly change your sound"
               " whenever you like. As such, you may well find that the Hotone"
               " Binary Amp Modeller swiftly becomes a permanent part of your "
               "pedalboard, giving you a whole world of sonic options to play "
               "with..")
item08 = Item(title="Hotone Binary Amp Modeller",
              description=description,
              category=category01,
              user=user1)

session.add(item08)
session.commit()

description = ("Master your sound. With a Hotone Binary IR Cab Modeller on "
               "your pedalboard, you'll have access to virtually all of the "
               "cab tones you could ever wish for. Coming with 100 presets to "
               "help you find the ideal sound, this pedal may well change your"
               " musical life, and open doors to a new world of sonic options."
               " That's not all, though. It also comes with a number of dials "
               "to help you shape your tone/cab presets further, with 10 "
               "studio mics and three mic position simulations programmed in. "
               "Armed with the Hotone Binary IR Cab Modeller, your sound is "
               "guaranteed to be huge, which will massively help in both live "
               "situations as well as studio recording sessions. If you're "
               "looking for the ultimate all-in-one simulator, you've found "
               "it.")
item09 = Item(title="Hotone Binary Cab Modeller",
              description=description,
              category=category01,
              user=user1)

session.add(item09)
session.commit()

description = ("The Mooer Micro Radar Cabinet Simulation Pedal does exactly "
               "as its name suggests, by offering a variety of 30 different "
               "speaker cabinet models for you to choose from. The Radar "
               "Pedal works as a virtual speaker cabinet so you don't have to "
               "lug around a heavy amp head to each of your gigs. The Micro "
               "Radar comes equipped with 30 IRs and 11 microphone models, "
               "providing you with a wide range of tonal possibilities to "
               "suit your individual style and needs. If the default IRs "
               "aren't quite enough for you, the Radar Pedal also allows you "
               "to load your own custom Impulse Responses onto the pedal for "
               "storing and recalling up to 36 user presets. With 4 power "
               "amps and customisable EQ, the Mooer Radar has all that you "
               "need to shape your ideal tone, and for an even more dynamic "
               "performance you can pair it with Mooer's Micro Preamp series "
               "to create the sound you want.")
item10 = Item(title="Mooer Micro Radar Cabinet Simulation Pedal",
              description=description,
              category=category01,
              user=user1)

session.add(item10)
session.commit()

# Load category "Boost"
category02 = Category(name="Boost", user_id=1)
session.add(category02)
session.commit()

# Load items for category "Boost"
description = ("The Palmer Pocket Booster is a versatile, small effect pedal "
               "ideal for when you need quick and easy gain control. The "
               "Pocket Booster can be used to increase the volume of an anemic"
               " amp, placed at the front end for more overdrive or at the end"
               " of an effects chain to provide a lead level boost. The Palmer"
               " Pocket Booster can be powered by a 9V battery or optional "
               "power adapter.")
item11 = Item(title="Palmer Pocket Booster Effect Pedal",
              description=description,
              category=category02,
              user=user1)

session.add(item11)
session.commit()

description = ("The TC Electronic Rush Booster Pedal offers a simple "
               "plug-and-play booster for electric guitarists. Its "
               "all-analogue circuit provides you with up to 20dBs of "
               "super-transparent clean boost, ideal for cutting through any "
               "mix. This affordable pedal is housed in a sturdy, roadworthy "
               "enclosure, along with top-mounted jack input/output for "
               "maximised space on your pedalboard. With its extreme value for"
               " money, the Rush booster is ideal for players on a strict "
               "budget.")
item12 = Item(title="TC Electronic Rush Booster Pedal",
              description=description,
              category=category02,
              user=user1)

session.add(item12)
session.commit()

description = ("The TC Electronic Spark Booster Mini Effects Pedal is the "
               "perfect solution to adding impact to your solos or main riffs."
               " Despite its compact size, this powerful pedal features an "
               "analogue circuit that is capable of delivering up to 20dB of "
               "clean boost. Complete with a simple level control knob, "
               "players can easily dial in the perfect amount of boost. This "
               "compact unit is a must have for any guitarist looking for a "
               "powerful impact.")
item13 = Item(title="TC Electronic Spark Booster Mini",
              description=description,
              category=category02,
              user=user1)

session.add(item13)
session.commit()

description = ("Mooer Audio are dedicated to researching and manufacturing "
               "musical instruments and audio equipment by applying "
               "state-of-the-art technology to their products. The Micro "
               "Series Guitar Effects Pedals are compact, lightweight and will"
               " inspire you to create new sounds.")
item14 = Item(title="Mooer MBT1 Flex Boost Pedal",
              description=description,
              category=category02,
              user=user1)

session.add(item14)
session.commit()

description = ("The Outlaw Effects Boilermaker Boost pedal is a transparent "
               "boost with active EQ, packaged in a tiny chassis to make a "
               "minimal impact on your pedalboard and maximum impact on your "
               "tone. The Boilermaker is designed to adapt to your setup and "
               "can fulfil a number of requirements with its 20dB of clean "
               "boost, 15dB of active EQ, and subtle gain control. These "
               "functions give it the capability of acting as a clean boost, a"
               " subtle overdrive sound, or as an always-on tone enhancer - "
               "where it can behave like a guitar preamp. Packed in an "
               "ultra-durable aluminium chassis and crafted with high-quality "
               "components, the Boilermaker is built to withstand the rigours "
               " of gigging and touring. The Boilermaker is a one-box solution"
               " to creating a pristine clean boost sound that can easily "
               "adapt to your setup and fulfil multiple requirements.")
item15 = Item(title="Outlaw Effects Boilermaker Boost",
              description=description,
              category=category02,
              user=user1)

session.add(item15)
session.commit()

description = ("Spark Booster is an analog clean boost and soft overdrive "
               "pedal TC Electronic's new Spark Booster is a special type of "
               "pedal. It's a pedal that will ignite your playing and "
               "kick-start your inspiration.")
item16 = Item(title="TC Electronic Spark Booster",
              description=description,
              category=category02,
              user=user1)

session.add(item16)
session.commit()

description = ("The Blackstar LT Boost Pedal allows players to achieve a "
               "boosted effect by adjusting the amount of cut or boost that is"
               " applied to the guitar signal. With three simple to use "
               "controls, including Bass, Treble and Gain, the Blackstar LT "
               "Boost provides easy operation and great versatility. The "
               "controls can be used to boost your amp harder, with a clean "
               "overdrive as well as increasing the amount of gain to achieve "
               "mighty projection. The Blackstar LT Boost allows for deep "
               "tonal shaping, as well as offering ease of use, all within a "
               "small and compact unit that will stand the rigours of the "
               "road.")
item17 = Item(title="Blackstar LT Boost Pedal",
              description=description,
              category=category02,
              user=user1)

session.add(item17)
session.commit()

description = ("Got the digital blues? Coat your guitar in warm, organic tone."
               " The new Analogizer thaws out digitally processed guitar, and "
               "gives you the sound and feel of an analog delay without the "
               "long delay times.")
item18 = Item(title="Electro Harmonix Analogizer Effects Pedal",
              description=description,
              category=category02,
              user=user1)

session.add(item18)
session.commit()

description = ("The Foxgear QBoost Semi-Parametric Boost gives excellent way "
               "to control your full band performances. Being able to change "
               "the live mix is an essential tool for the serious live band, "
               "getting it right is integral for a good performance. QBoost "
               "lets you change this on the fly. The QBoost is a semi-"
               "parametric boost pedal that allows you to cut through the mix "
               "when playing riffs or solos, or step back in the mix when "
               "playing rhythmic sections. It's an analog pedal that gives you"
               " a lot of control of your playing and adds a professional "
               "level of versatility to your performances. With no added noise"
               ", the QBoost pedal is fully transparent and offers you a great"
               " tone at an affordable price")
item19 = Item(title="Foxgear QBoost Semi-Parametric Boost",
              description=description,
              category=category02,
              user=user1)

session.add(item19)
session.commit()

description = ("The CKK Electronic Omni Boost MK2 is a diverse guitar pedal "
               "for both live and studio applications. The Omni Boost consists"
               " of two boost types: fat gain and clean gain. The clean signal"
               " offers up to 20dB of boost, or can be turned to its minimum "
               "and act as buffer signal restoration. The fat boost setting "
               "increases the mid frequency and is suited to balancing and "
               "improving overdrive pedals. This pedal is suited to versatile "
               "guitarists who play both clean and driven songs.")
item20 = Item(title="CKK Electronic Omni Boost MK2 Guitar Pedal",
              description=description,
              category=category02,
              user=user1)

session.add(item20)
session.commit()

# Load category "Boutique Pedals"
category = Category(name="Boutique Pedals", user=user1)
session.add(category)
session.commit()

# Load category "Buffer"
category = Category(name="Buffer", user=user1)
session.add(category)
session.commit()

# Load category "Chorus"
category = Category(name="Chorus", user=user1)
session.add(category)
session.commit()

# Load category "Compressor"
category = Category(name="Compressor", user=user1)
session.add(category)
session.commit()

# Load category "Drum Machine"
category = Category(name="Drum Machine", user=user1)
session.add(category)
session.commit()

# Load category "EBow"
category = Category(name="EBow", user=user1)
session.add(category)
session.commit()

# Load category "EQ"
category = Category(name="EQ", user=user1)
session.add(category)
session.commit()

# Load category "Expression"
category = Category(name="Expression", user=user1)
session.add(category)
session.commit()

# Load category "Filter"
category = Category(name="Filter", user=user1)
session.add(category)
session.commit()

# Load category "Flanger"
category = Category(name="Flanger", user=user1)
session.add(category)
session.commit()

# Load category "Fuzz"
category = Category(name="Fuzz", user=user1)
session.add(category)
session.commit()

# Load category "Guitar Synth"
category = Category(name="Guitar Synth", user=user1)
session.add(category)
session.commit()

# Load category "Limiter Enhancer"
category = Category(name="Limiter Enhancer", user=user1)
session.add(category)
session.commit()

# Load category "Line Selector"
category = Category(name="Line Selector", user=user1)
session.add(category)
session.commit()

# Load category "Looper"
category = Category(name="Looper", user=user1)
session.add(category)
session.commit()

# Load category "MIDI"
category = Category(name="MIDI", user=user1)
session.add(category)
session.commit()

# Load category "Modulator"
category = Category(name="Modulator", user=user1)
session.add(category)
session.commit()

# Load category "Noise Gate"
category = Category(name="Noise Gate", user=user1)
session.add(category)
session.commit()

# Load category "Octave"
category = Category(name="Octave", user=user1)
session.add(category)
session.commit()

# Load category "Overdrive"
category = Category(name="Overdrive", user=user1)
session.add(category)
session.commit()

# Load category "Phaser"
category = Category(name="Phaser", user=user1)
session.add(category)
session.commit()

# Load category "Preamp"
category = Category(name="Preamp", user=user1)
session.add(category)
session.commit()

# Load category "Reverb"
category = Category(name="Reverb", user=user1)
session.add(category)
session.commit()

# Load category "Tremolo"
category = Category(name="Tremolo", user=user1)
session.add(category)
session.commit()

# Load category "Tuner"
category = Category(name="Tuner", user=user1)
session.add(category)
session.commit()

# Load category "Vocal Effects"
category = Category(name="Vocal Effects", user=user1)
session.add(category)
session.commit()

# Load category "Volume"
category = Category(name="Volume", user=user1)
session.add(category)
session.commit()

# Load category "Wah"
category = Category(name="Wah", user=user1)
session.add(category)
session.commit()

# Load category "Rack Effects"
category = Category(name="Rack Effects", user=user1)
session.add(category)
session.commit()

# Load category "Pedal Packs"
category = Category(name="Pedal Packs", user=user1)
session.add(category)
session.commit()

# Load category "Pedal Boards"
category = Category(name="Pedal Boards", user=user1)
session.add(category)
session.commit()

print("Added categories and items!")
