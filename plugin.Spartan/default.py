# -*- coding: utf-8 -*-

""" ^ SECTION 1:
    This should be at the top of your code to declare the type of text
    format you're using. Without this you may find some text editors save
    it in an incompatible format and this can make bug tracking extremely
    confusing! More info here: https://www.python.org/dev/peps/pep-0263/
"""
#----------------------------------------------------------------
"""
    SECTION 2:
    This is where you'd put your license details, the GPL3 license 
    is the most common to use as it makes it easy for others to fork
    and improve upon your code. If you're re-using others code ALWAYS
    check the license first, removal of licenses is NOT allowed and you
    generally have to keep to the same license used in the original work
    (check license details as some do differ).

    Although not all licenses require it (some do, some don't),
    you should always give credit to the original author(s). Someone may have spent
    months if not years on the code so really it's the very least you can do if
    you choose to use their work as a base for your own.
"""
#----------------------------------------------------------------
"""
    SECTION 3:
    This is your global imports, any modules you need to import code from
    are added here. You'll see a handful of the more common imports below.
"""
import os           # access operating system commands
import urlparse     # splits up the directory path - much easier importing this than coding it up ourselves
import xbmc         # the base xbmc functions, pretty much every add-on is going to need at least one function from here
import xbmcaddon    # pull addon specific information such as settings, id, fanart etc.
import xbmcgui      # gui based functions, contains things like creating dialog pop-up windows
import xbmcplugin   # contains functions required for creating directory structure style add-ons (plugins)

# (*) = These modules require the noobsandnerds repo to be installed
import koding       # (*) a framework for easy add-on development, this template is to be used in conjunction with this module.
import nanscrapers  # (*) if you want to easily grab video links the hard work is done for you with this module.

from koding import Add_Dir  # By importing something like this we don't need to use <module>.<function> to call it,
                            # instead you can just use the function name - in this case Add_Dir().

from koding import route, Run # These are essential imports which allow us to open directories and navigate through the add-on.

#----------------------------------------------------------------
"""
    SECTION 4:
    These are our global variables, anything we set here can be accessed by any of
    our functions later on. Please bare in mind though that if you change the value
    of a global variable from inside a function the value will revert back to the
    value set here once that function has completed.
"""
addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id
dialog       = xbmcgui.Dialog()                     # A basic dialog message command
home_folder  = xbmc.translatePath('special://home/')# Convert the special path of Kodi home folder to the physical path
addon_folder = os.path.join(home_folder,'addons')   # Join our folder above with 'addons' so we have a link to our addons folder
art_path     = os.path.join(addon_folder,addon_id)  # Join addons folder with the addon_id, we'll use this as a basic art folder
debug        = koding.Addon_Setting('debug')        # Grab the setting of our debug mode in add-on settings
#----------------------------------------------------------------
"""
    SECTION 5:
    This is optional, if you want to have your add-on hosted at noobsandnerds.com and
    would like to hook into their special framework then you need to add the following
    line. It has been commented out in this template, just uncomment if you want to use it
    but you will need to have your add-on approved by the noobsandnerds team for this functionality.
"""

# koding.User_Info()

#----------------------------------------------------------------
"""
    SECTION 6:
    Add our custom functions in here, it's VERY important these go in this section
    as the code in section 7 relies on these functions. If that code tries to run
    before these functions are declared the add-on will fail.

    You'll notice each function in here has a decorator above it (an @route() line of code),
    this assigns a mode to the function so it can be called with Add_Dir and it also tells
    the code what paramaters to send through. For example you'll notice the Main_Menu() function
    we've assigned to the mode "main" - this means if we ever want to get Add_Dir to open that
    function we just use the mode "main". This particular function does not require any extra
    params to be sent through but if you look at the Testing() function you'll see we send through
    2 different paramaters (url and description), if you look at the Add_Dir function in Main_Menu()
    you'll see we've snet these through as a dictionary. Using that same format you can send through
    as many different params as you wish.route
"""

#-----------------------------------------------------------
# EDIT THIS MAIN_MENU() FUNCTION - THIS IS FUN TO PLAY WITH!
#-----------------------------------------------------------
@route(mode="main")
def Main_Menu():

# Only show koding tutorials if debug mode is enabled in addon settings
    if debug=='true':
        Add_Dir(name='KODING TUTORIALS', url='', mode='tutorials', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))

    Add_Dir(name='Live TV', url='', mode='video_live', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')

    Add_Dir(name='Movies', url='', mode='video_examples', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')	
	
    Add_Dir(name='Walking Dead Season 7', url='', mode='video_exam', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')	

    Add_Dir(name='Fear The Walking Dead Season 3', url='', mode='video_ex', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')

    Add_Dir(name='Game Of Thrones Season 7', url='', mode='video_e', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')
	
    Add_Dir(name='The Grand Tour Season 1', url='', mode='video_grand', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')
   
    Add_Dir(name='Top Gear', url='', mode='video_gear', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')
	
    Add_Dir(name='James May Things You Need To Know', url='', mode='video_may', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')
	
    Add_Dir(name='Russell Peters', url='', mode='video_peters', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')
	
    Add_Dir(name='Derren Brown', url='', mode='video_brown', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')
	
    Add_Dir(name='Fawlty Towers', url='', mode='video_towers', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')
	
    Add_Dir(name='Documentaries', url='', mode='video_doc', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')

    Add_Dir(name='Music Videos', url='', mode='video_mvids', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')	
	
    Add_Dir(name='YouTube Videos', url='', mode='video_tube', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='', content_type='video')

	


	
# Once you've played with the above try uncommenting each of the following lines one by one.
# After uncommenting a line re-run the add-on to see your changes take place.

    # Add_Dir(name='OPEN FOLDER - TEST MODE', url='test_mode', mode='open_folder', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
    # Add_Dir(name='OPEN FOLDER - NO URL', url='', mode='open_folder', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
    # Add_Dir(name='VIDEO EXAMPLES', url='', mode='video_examples', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='A couple of test videos for you to look at.', content_type='video')
    # Add_Dir(name='MUSIC EXAMPLE', url='', mode='music_examples', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'),content_type='song')

# This is our test zone, this just calls the Test_Function mode so feel free to play with the code in that function.
    # Add_Dir(name='TESTING ZONE', url='{"test1":"this is","test2":"some example","test3":"text"}', mode='test_function', folder=False, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
#-----------------------------
@route(mode="test_function", args=["test1","test2","test3"])
def Test_Function(test1, test2, test3):
# Example of sending multiple variables through the Add_Dir function
    xbmc.log(test1,2)
    xbmc.log(test2,2)
    xbmc.log(test3,2)
    dialog.ok('CHECK THE LOG','Take a look at your log, you should be able to see the 3 lines of example text we sent through.')
#-----------------------------
@route(mode="open_folder", args=["url"])
def Test_Folder(url):
    if url == 'test_mode':
        dialog.ok('Test Mode','open_folder has been called with the url being "test_mode". When you click OK you should open into and empty folder - this is because folder=True in our Add_Dir()')
    else:
        dialog.ok('TRY THESE EXAMPLES','If you\'ve left the mode as the default you\'ll receive a message explaining the mode does not exist. Feel free to change this to a mode that does exist.')
        Add_Dir(name='EXAMPLE FOLDER', url='', mode='changeme', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
        Add_Dir(name='EXAMPLE ITEM', url='', mode='changeme', folder=False, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
        Add_Dir(name='EXAMPLE BAD FUNCTION', url='', mode='bad_function', folder=False, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
#-----------------------------
@route(mode="bad_function")
def Bad_Function():
    if debug != 'true':
        dialog.ok('SET DEBUG TO TRUE','Go into your add-on settings and set debug mode to True then run this again. If debug is set to true we have proper error reporting in place to help your add-on development.')
        koding.Open_Settings(focus='1.1')
    xbmc.log(this_should_error)
#-----------------------------
@route(mode='testing', args=["my_text","my_desc"])
def Testing(my_text,my_desc):
    dialog.ok('TEST','Here are the params we recieved in Testing() function:', 'my_text: [COLOR=dodgerblue]%s[/COLOR]' % my_text,'my_desc: [COLOR=dodgerblue]%s[/COLOR]'%my_desc)
#-----------------------------
@route(mode="video_examples")
def Video_Examples():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='Star Wars Episode 1 The Phantom Menace', url='http://greeksattv.co.uk/Mario/Star.Wars.Episode.1.The.Phantom.Menace.1999.1080p.BrRip.x264.BOKUTOX.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/22/4f/9d/224f9d64ad01d1bf5937a46ffe99eaec.jpg',
        fanart='http://wallpapercave.com/wp/VLMEAYD.jpg',
        info_labels={"originaltitle":"Star Wars Episode 1 The Phantom Menace","genre":"crime,british", "plot":"Two Jedi Knights escape a hostile blockade to find allies and come across a young boy who may bring balance to the Force, but the long dormant Sith resurface to claim their old glory", "mpaa":"18"})

    Add_Dir(name='Star Wars Episode 2 Attack Of The Clones', url='http://greeksattv.co.uk/Mario/Star.Wars.Episode.2.Attack.of.the.Clones.2002.1080p.BrRip.x264.BOKUTOX.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg',
        info_labels={"originaltitle":"Star Wars Episode 2 Attack Of The Clones","genre":"crime,british", "plot":"Ten years after initially meeting, Anakin Skywalker shares a forbidden romance with Padmé, while Obi-Wan investigates an assassination attempt on the Senator and discovers a secret clone army crafted for the Jedi", "mpaa":"18"})

    Add_Dir(name='Star Wars Episode 3 Revenge Of The Sith', url='http://greeksattv.co.uk/Mario/Star.Wars.Episode.3.Revenge.of.the.Sith.2005.1080p.BrRip.x264.BOKUTOX.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://usercontent2.hubstatic.com/12709537_f520.jpg',
        fanart='https://usercontent2.hubstatic.com/12709537_f520.jpg',
        info_labels={"originaltitle":"Star Wars Episode 3 Revenge Of The Sith","genre":"crime,british", "plot":"Three years into the Clone Wars, the Jedi rescue Palpatine from Count Dooku. As Obi-Wan pursues a new threat, Anakin acts as a double agent between the Jedi Council and Palpatine and is lured into a sinister plan to rule the galaxy", "mpaa":"18"}) 

    Add_Dir(name='Star Wars Episode 4 A New Hope', url='http://greeksattv.co.uk/Mario/Star.Wars.Episode.4.A.New.Hope.1977.1080p.BrRip.x264.BOKUTOX.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.soundspheremag.com/wp-content/migration/images/stories/anewhopeposter.jpg',
        fanart='http://www.soundspheremag.com/wp-content/migration/images/stories/anewhopeposter.jpg',
        info_labels={"originaltitle":"Star Wars Episode 4 A New Hope","genre":"crime,british", "plot":"Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids to save the galaxy from the Empire's world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader", "mpaa":"18"})

    Add_Dir(name='Star Wars Episode 5 The Empire Strikes Back', url='http://greeksattv.co.uk/Mario/Star.Wars.Episode.5.The.Empire.Strikes.Back.1980.1080p.BrRip.x264.BOKUTOX.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/star-wars-episode-v--the-empire-strikes-back.13948.jpg',
        fanart='https://i.jeded.com/i/star-wars-episode-v--the-empire-strikes-back.13948.jpg',
        info_labels={"originaltitle":"Star Wars Episode 5 The Empire Strikes Back","genre":"crime,british", "plot":"After the rebels are overpowered by the Empire on their newly established base, Luke Skywalker begins Jedi training with Master Yoda. His friends accept shelter from a questionable ally as Darth Vader hunts them in a plan to capture Luke", "mpaa":"18"})

    Add_Dir(name='Star Wars Episode 6 Return Of The Jedi', url='http://greeksattv.co.uk/Mario/Star.Wars.Episode.6.Return.of.the.Jedi.1983.1080p.BrRip.x264.BOKUTOX.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/star-wars-episode-vi--return-of-the-jedi.13947.jpg',
        fanart='https://i.jeded.com/i/star-wars-episode-vi--return-of-the-jedi.13947.jpg',
        info_labels={"originaltitle":"Star Wars Episode 6 Return Of The Jedi","genre":"crime,british", "plot":"After a daring mission to rescue Han Solo from Jabba the Hutt, the rebels dispatch to Endor to destroy a more powerful Death Star. Meanwhile, Luke struggles to help Vader back from the dark side without falling into the Emperor's trap", "mpaa":"18"}) 

    Add_Dir(name='Star Wars Episode 7 The Force Awakens', url='http://greeksattv.co.uk/Mario/Star.Wars.Episode.VII.The.Force.Awakens.2015.1080p.BluRay.H264.AAC-RARBG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://d1x7zurbps6occ.cloudfront.net/product/xlarge/515275-150413.jpg',
        fanart='https://d1x7zurbps6occ.cloudfront.net/product/xlarge/515275-150413.jpg',
        info_labels={"originaltitle":"Star Wars Episode 7 The Force Awakens","genre":"crime,british", "plot":"Three decades after the Empire's defeat, a new threat arises in the militant First Order. Stormtrooper defector Finn and spare parts scavenger Rey are caught up in the Resistance's search for the missing Luke Skywalker", "mpaa":"18"})

    Add_Dir(name='Star Wars Rogue One', url='http://greeksattv.co.uk/Mario/Rogue.One.2016.720p.BRRip.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2016/10/rogueone_onesheetA.jpg',
        fanart='http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2016/10/rogueone_onesheetA.jpg',
        info_labels={"originaltitle":"Star Wars Rogue One","genre":"crime,british", "plot":"The Rebel Alliance makes a risky move to steal the plans for the Death Star, setting up the epic saga to follow", "mpaa":"18"})

    Add_Dir(name='Deadpool', url='http://greeksattv.co.uk/Mario/Deadpool.2016.720p.BluRay.x264.VPPV.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://cdn.traileraddict.com/content/20th-century-fox/deadpool-poster-2.jpg',
        fanart='https://cdn.traileraddict.com/content/20th-century-fox/deadpool-poster-2.jpg',
        info_labels={"originaltitle":"Deadpool","genre":"crime,british", "plot":"A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge", "mpaa":"18"})

    Add_Dir(name='The Avengers', url='http://greeksattv.co.uk/Mario/The.Avengers.2012.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/0f/03/e6/0f03e6733b0cf567cc92e8e20290462f--avengers-poster-avengers-.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/0f/03/e6/0f03e6733b0cf567cc92e8e20290462f--avengers-poster-avengers-.jpg',
        info_labels={"originaltitle":"The Avengers","genre":"crime,british", "plot":"Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity", "mpaa":"18"})

    Add_Dir(name='The Avengers Age Of Ultron', url='http://greeksattv.co.uk/Mario/Avengers.Age.of.Ultron.2015.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/avengers-age-of-ultron.jpg',
        fanart='http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/avengers-age-of-ultron.jpg',
        info_labels={"originaltitle":"The Avengers Age Of Ultron","genre":"crime,british", "plot":"When Tony Stark and Bruce Banner try to jump-start a dormant peacekeeping program called Ultron, things go horribly wrong and it's up to Earth's mightiest heroes to stop the villainous Ultron from enacting his terrible plan", "mpaa":"18"}) 

    Add_Dir(name='Iron Man', url='http://greeksattv.co.uk/Mario/Iron%20Man%202008.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.collider.com/wp-content/uploads/2015/04/iron-man-1-poster.jpg',
        fanart='http://cdn.collider.com/wp-content/uploads/2015/04/iron-man-1-poster.jpg',
        info_labels={"originaltitle":"Iron Man","genre":"crime,british", "plot":"After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil", "mpaa":"18"})

    Add_Dir(name='Iron Man 2', url='http://greeksattv.co.uk/Mario/Iron.Man.II.x264.720p.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/fe/04/04/fe0404f0fc125a32d7a6ce975f7ad3a6--jon-favreau-mickey-rourke.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/fe/04/04/fe0404f0fc125a32d7a6ce975f7ad3a6--jon-favreau-mickey-rourke.jpg',
        info_labels={"originaltitle":"Iron Man 2","genre":"crime,british", "plot":"With the world now aware of his identity as Iron Man, Tony Stark must contend with both his declining health and a vengeful mad man with ties to his father's legacy", "mpaa":"18"})

    Add_Dir(name='Iron Man 3', url='http://greeksattv.co.uk/Mario/Iron.Man.3.2013.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://www.discshop.se/img/front_large/112523/iron_man_3.jpg',
        fanart='https://www.discshop.se/img/front_large/112523/iron_man_3.jpg',
        info_labels={"originaltitle":"Iron Man 3","genre":"crime,british", "plot":"When Tony Stark's world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey of rebuilding and retribution", "mpaa":"18"})   

    Add_Dir(name='Thor', url='http://greeksattv.co.uk/Mario/Thor.2011.720p.BrRip.264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.collider.com/wp-content/uploads/thor-movie-poster-chris-hemsworth-01.jpg',
        fanart='http://cdn.collider.com/wp-content/uploads/thor-movie-poster-chris-hemsworth-01.jpg',
        info_labels={"originaltitle":"Thor","genre":"crime,british", "plot":"The powerful but arrogant god Thor is cast out of Asgard to live amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders", "mpaa":"18"})   

    Add_Dir(name='Thor The Dark World', url='http://greeksattv.co.uk/Mario/Thor.The.Dark.World.2013.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.ientry.com/sites/webpronews/article_pics/thor_poster.jpg',
        fanart='http://cdn.ientry.com/sites/webpronews/article_pics/thor_poster.jpg',
        info_labels={"originaltitle":"Thor The Dark World","genre":"crime,british", "plot":"When Dr. Jane Foster gets cursed with a powerful entity known as the Aether, Thor is heralded of the cosmic event known as the Convergence and the genocidal Dark Elves", "mpaa":"18"})  

    Add_Dir(name='Captain America Civil War', url='http://greeksattv.co.uk/Mario/Captain.America.Civil.War.2016.720p.BluRay.x264.VPPV.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/07/bc/cb/07bccb732e65f653e87928de34e551a3.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/07/bc/cb/07bccb732e65f653e87928de34e551a3.jpg',
        info_labels={"originaltitle":"Captain America Civil War","genre":"crime,british", "plot":"Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man", "mpaa":"18"})  

    Add_Dir(name='Guardians Of The Galaxy', url='http://greeksattv.co.uk/Mario/Guardians.of.the.Galaxy.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://1.media.dorkly.cvcdn.com/26/95/18b149286ca6f2920e017bd5d2ffcbf5.jpg',
        fanart='http://1.media.dorkly.cvcdn.com/26/95/18b149286ca6f2920e017bd5d2ffcbf5.jpg',
        info_labels={"originaltitle":"Guardians Of The Galaxy","genre":"crime,british", "plot":"A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe", "mpaa":"18"})   

    Add_Dir(name='Doctor Strange', url='http://greeksattv.co.uk/Mario/Doctor.Strange.2016.720p.BluRay.H264.AAC-RARBG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn-static.denofgeek.com/sites/denofgeek/files/2016/11/doctor_strange_ver29.jpg',
        fanart='http://cdn-static.denofgeek.com/sites/denofgeek/files/2016/11/doctor_strange_ver29.jpg',
        info_labels={"originaltitle":"Doctor Strange","genre":"crime,british", "plot":"While on a journey of physical and spiritual healing, a brilliant neurosurgeon is drawn into the world of the mystic arts", "mpaa":"18"})   

    Add_Dir(name='Ant Man', url='http://greeksattv.co.uk/Mario/Ant.Man.2015.720p.Ganool-%5BMy-Film%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://static5.businessinsider.com/image/5579c5f4ecad04613449d053-1200-2000/cool-ant-man-poster.jpg',
        fanart='http://www.impawards.com/2015/posters/ant_man_ver19.jpg',
        info_labels={"originaltitle":"Ant Man","genre":"crime,british", "plot":"Armed with a super-suit with the astonishing ability to shrink in scale but increase in strength, cat burglar Scott Lang must embrace his inner hero and help his mentor, Dr. Hank Pym, plan and pull off a heist that will save the world", "mpaa":"18"}) 

    Add_Dir(name='Spider Man', url='http://greeksattv.co.uk/Mario/SpiderMan.2002.720p.BrRip.264.YIFY..mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://assets1.ignimgs.com/2017/03/24/2002-spider-man-2-1490395333192_1280w.jpg',
        fanart='http://assets1.ignimgs.com/2017/03/24/2002-spider-man-2-1490395333192_1280w.jpg',
        info_labels={"originaltitle":"Spider Man","genre":"crime,british", "plot":"When bitten by a genetically modified spider, a nerdy, shy, and awkward high school student gains spider-like abilities that he eventually must use to fight evil as a superhero after tragedy befalls his family", "mpaa":"18"})   

    Add_Dir(name='Spider Man 2', url='http://greeksattv.co.uk/Mario/Spider.Man.2.2004.720p.BrRip.264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://assets1.ignimgs.com/2017/03/24/2004-spider-man2-7-1490395333213_1280w.jpg',
        fanart='http://assets1.ignimgs.com/2017/03/24/2004-spider-man2-7-1490395333213_1280w.jpg',
        info_labels={"originaltitle":"Spider Man 2","genre":"crime,british", "plot":"When bitten by a genetically modified spider, a nerdy, shy, and awkward high school student gains spider-like abilities that he eventually must use to fight evil as a superhero after tragedy befalls his family", "mpaa":"18"})   

    Add_Dir(name='Spider Man 3', url='http://greeksattv.co.uk/Mario/SpiderMan.3.2007.720p.BrRip.264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://cdn.europosters.eu/image/750/posters/spiderman-3-swing-i1393.jpg',
        fanart='https://cdn.europosters.eu/image/750/posters/spiderman-3-swing-i1393.jpg',
        info_labels={"originaltitle":"Spider Man 3","genre":"crime,british", "plot":"Peter Parker is beset with troubles in his failing personal life as he battles a brilliant scientist named Doctor Otto Octavius", "mpaa":"18"}) 

    Add_Dir(name='The Amazing Spider Man', url='http://greeksattv.co.uk/Mario/The.Amazing.Spiderman.2012.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://static.comicvine.com/uploads/scale_small/11/113509/4383735-4855984673-Spide.jpg',
        fanart='https://static.comicvine.com/uploads/scale_small/11/113509/4383735-4855984673-Spide.jpg',
        info_labels={"originaltitle":"The Amazing Spider Man","genre":"crime,british", "plot":"After Peter Parker is bitten by a genetically altered spider, he gains newfound, spider-like powers and ventures out to solve the mystery of his parent's mysterious death", "mpaa":"18"})

    Add_Dir(name='The Amazing Spider Man 2', url='http://greeksattv.co.uk/Mario/The.Amazing.Spider.Man.2.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.collider.com/wp-content/uploads/the-amazing-spider-man-2-poster-imax1.jpg',
        fanart='http://cdn.collider.com/wp-content/uploads/the-amazing-spider-man-2-poster-imax1.jpg',
        info_labels={"originaltitle":"The Amazing Spider Man 2","genre":"crime,british", "plot":"When New York is put under siege by Oscorp, it is up to Spider-Man to save the city he swore to protect as well as his loved ones", "mpaa":"18"}) 

    Add_Dir(name='Batman Vs Superman Dawn Of Justice Extended', url='http://greeksattv.co.uk/Mario/Batman.v.Superman.Dawn.of.Justice.2016.EXTENDED.720p.BRRip.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/c5/2f/0b/c52f0b9660b80d4d1d60ba93d368034d.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/c5/2f/0b/c52f0b9660b80d4d1d60ba93d368034d.jpg',
        info_labels={"originaltitle":"Batman Vs Superman Dawn Of Justice Extended","genre":"crime,british", "plot":"Fearing that the actions of Superman are left unchecked, Batman takes on the Man of Steel, while the world wrestles with what kind of a hero it really needs", "mpaa":"18"}) 

    Add_Dir(name='Suicide Squad Extended', url='http://greeksattv.co.uk/Mario/Suicide.Squad.2016.Extended.720p.BRRip.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.hollywoodreporter.com/sites/default/files/custom/d4a65bda5131bde968111034cce8f4f33537875d.jpg',
        fanart='http://www.hollywoodreporter.com/sites/default/files/custom/d4a65bda5131bde968111034cce8f4f33537875d.jpg',
        info_labels={"originaltitle":"Suicide Squad Extended","genre":"crime,british", "plot":"A secret government agency recruits some of the most dangerous incarcerated super-villains to form a defensive task force. Their first mission: save the world from the apocalypse", "mpaa":"18"})

    Add_Dir(name='Batman Forever', url='http://greeksattv.co.uk/Mario/Batman.Forever.1995.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://ironheadstudio.com/wp-content/uploads/2014/10/batman-forever-movie-poster.jpg',
        fanart='http://ironheadstudio.com/wp-content/uploads/2014/10/batman-forever-movie-poster.jpg',
        info_labels={"originaltitle":"Batman Forever","genre":"crime,british", "plot":"Batman must battle former district attorney Harvey Dent, who is now Two-Face and Edward Enigma, The Riddler with help from an amorous psychologist and a young circus acrobat who becomes his sidekick, Robin", "mpaa":"18"}) 

    Add_Dir(name='Batman And Robin', url='http://greeksattv.co.uk/Mario/Batman.And.Robin.1997.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/fc/0a/6e/fc0a6eeb3564e0389e105d9436ce50c1.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/fc/0a/6e/fc0a6eeb3564e0389e105d9436ce50c1.jpg',
        info_labels={"originaltitle":"Batman And Robin","genre":"crime,british", "plot":"Batman and Robin try to keep their relationship together even as they must stop Mr. Freeze and Poison Ivy from freezing Gotham City", "mpaa":"18"}) 

    Add_Dir(name='Batman The Dark Knight', url='http://greeksattv.co.uk/Mario/The.Dark.Knight.2008.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://paulmmartinblog.files.wordpress.com/2011/07/the_dark_knight_poster.jpg',
        fanart='https://paulmmartinblog.files.wordpress.com/2011/07/the_dark_knight_poster.jpg',
        info_labels={"originaltitle":"Batman The Dark Knight","genre":"crime,british", "plot":"When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice", "mpaa":"18"}) 

    Add_Dir(name='Batman The Dark Knight Rises', url='http://greeksattv.co.uk/Mario/The.Dark.Knight.Rises.2012.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.collider.com/wp-content/uploads/the-dark-knight-rises-poster.jpg',
        fanart='http://cdn.collider.com/wp-content/uploads/the-dark-knight-rises-poster.jpg',
        info_labels={"originaltitle":"Batman The Dark Knight Rises","genre":"crime,british", "plot":"Eight years after the Joker's reign of anarchy, the Dark Knight, with the help of the enigmatic Selina, is forced from his exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane", "mpaa":"18"}) 

    Add_Dir(name='Pirates Of The Caribbean The Curse Of The Black Pearl', url='http://greeksattv.co.uk/Mario/Pirates.of.the.Caribbean.Curse.of.the.Black.Pearl.2003.720p.BrRip.x264.Deceit.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://livedoor.blogimg.jp/manbokcm/imgs/9/d/9d0664cc.jpg',
        fanart='http://livedoor.blogimg.jp/manbokcm/imgs/9/d/9d0664cc.jpg',
        info_labels={"originaltitle":"Pirates Of The Caribbean The Curse Of The Black Pearl","genre":"crime,british", "plot":"Blacksmith Will Turner teams up with eccentric pirate Captain Jack Sparrow to save his love, the governors daughter, from Jacks former pirate allies, who are now undead", "mpaa":"18"}) 

    Add_Dir(name='Pirates Of The Caribbean Dead Mans Chest', url='http://greeksattv.co.uk/Mario/Pirates.of.the.Caribbean.Dead.Mans.Chest.2006.720p.BrRip.x264.Deceit.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://movieswithmae.com/wp-content/uploads/2015/05/iwvyZBRD7qfDQ8ylRmf5NbLC5Oi.jpg',
        fanart='http://movieswithmae.com/wp-content/uploads/2015/05/iwvyZBRD7qfDQ8ylRmf5NbLC5Oi.jpg',
        info_labels={"originaltitle":"Pirates Of The Caribbean Dead Mans Chest","genre":"crime,british", "plot":"Jack Sparrow races to recover the heart of Davy Jones to avoid enslaving his soul to Jones' service, as other friends and foes seek the heart for their own agenda as well", "mpaa":"18"})

    Add_Dir(name='Pirates Of The Caribbean At Worlds End', url='http://greeksattv.co.uk/Mario/Pirates.of.the.Caribbean.At.Worlds.End.2007.720p.BrRip.x264.Deceit.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://moviereviews.s3.amazonaws.com/2016/03/07/22/54/35/729/cKbR9EuchlPVQEOty02DazxVz7e.jpg',
        fanart='http://moviereviews.s3.amazonaws.com/2016/03/07/22/54/35/729/cKbR9EuchlPVQEOty02DazxVz7e.jpg',
        info_labels={"originaltitle":"Pirates Of The Caribbean At Worlds End","genre":"crime,british", "plot":"Captain Barbossa, Will Turner and Elizabeth Swann must sail off the edge of the map, navigate treachery and betrayal, find Jack Sparrow, and make their final alliances for one last decisive battle", "mpaa":"18"}) 	

    Add_Dir(name='Pirates Of The Caribbean On Stranger Tides', url='http://greeksattv.co.uk/Mario/Pirates.of.the.Caribbean.On.Stranger.Tides.2011.720p.BrRip.x264.Deceit.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/1b/41/38/1b4138cf663e817ae0e8b1b1e1eac8cd.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/1b/41/38/1b4138cf663e817ae0e8b1b1e1eac8cd.jpg',
        info_labels={"originaltitle":"Pirates Of The Caribbean On Stranger Tides","genre":"crime,british", "plot":"Jack Sparrow and Barbossa embark on a quest to find the elusive fountain of youth, only to discover that Blackbeard and his daughter are after it too", "mpaa":"18"}) 	

    Add_Dir(name='Transformers', url='http://greeksattv.co.uk/Mario/Transformers.2007.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.firstshowing.net/img/transformers-poster-big.jpg',
        fanart='http://www.firstshowing.net/img/transformers-poster-big.jpg',
        info_labels={"originaltitle":"Transformers","genre":"crime,british", "plot":"An ancient struggle between two Cybertronian races, the heroic Autobots and the evil Decepticons, comes to Earth, with a clue to the ultimate power held by a teenager", "mpaa":"18"})	

    Add_Dir(name='Transformers Revenge Of The Fallen', url='http://greeksattv.co.uk/Mario/Transformers.Revenge.of.the.Fallen.IMAX.EDITION.2009.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://news.tfw2005.com/wp-content/uploads/sites/10/2009/06/34141_1244079750.jpg',
        fanart='http://news.tfw2005.com/wp-content/uploads/sites/10/2009/06/34141_1244079750.jpg',
        info_labels={"originaltitle":"Transformers Revenge Of The Fallen","genre":"crime,british", "plot":"Sam Witwicky leaves the Autobots behind for a normal life. But when his mind is filled with cryptic symbols, the Decepticons target him and he is dragged back into the Transformers war", "mpaa":"18"}) 	

    Add_Dir(name='Transformers Dark Of The Moon', url='http://greeksattv.co.uk/Mario/Transformers.3.2011.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.collider.com/wp-content/uploads/transformers-dark-of-the-moon-movie-poster-04.jpg',
        fanart='http://cdn.collider.com/wp-content/uploads/transformers-dark-of-the-moon-movie-poster-04.jpg',
        info_labels={"originaltitle":"Transformers Dark Of The Moon","genre":"crime,british", "plot":"The Autobots learn of a Cybertronian spacecraft hidden on the moon, and race against the Decepticons to reach it and to learn its secrets", "mpaa":"18"}) 	

    Add_Dir(name='Transformers Age Of Extinction', url='http://greeksattv.co.uk/Mario/Transformers.Age.of.Extinction.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/716z0J6wbhL._SY550_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/716z0J6wbhL._SY550_.jpg',
        info_labels={"originaltitle":"Transformers Age Of Extinction","genre":"crime,british", "plot":"Autobots must escape sight from a bounty hunter who has taken control of the human serendipity: Unexpectedly, Optimus Prime and his remaining gang turn to a mechanic, his daughter, and her back street racing boyfriend for help", "mpaa":"18"}) 	

    Add_Dir(name='The Fate Of The Furious', url='http://greeksattv.co.uk/Mario/The.Fate.of.the.Furious.2017.EXTENDED.DIRECTORS.CUT.1080p.WEBRip.6CH.x265.HEVC-PSA.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://leaker.se/sites/leaker/files/covers/the-fate-of-the-furious-2017-hdts-h264-ac3-hq-hive-cm8.jpg',
        fanart='http://leaker.se/sites/leaker/files/covers/the-fate-of-the-furious-2017-hdts-h264-ac3-hq-hive-cm8.jpg',
        info_labels={"originaltitle":"The Fate Of The Furious","genre":"crime,british", "plot":"When a mysterious woman seduces Dom into the world of terrorism and a betrayal of those closest to him, the crew face trials that will test them as never before", "mpaa":"18"}) 	

    Add_Dir(name='Independence Day Resurgence', url='http://greeksattv.co.uk/Mario/Independence.Day.Resurgence.2016.720p.WEBRip.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://3.bp.blogspot.com/-Ffjn6fWlv-o/V3m4dZR1p8I/AAAAAAAABOI/o8F2P4m_VDgp6xDAzT6yEFVb1wBVoGC5wCLcB/s1600/Independence%2BDay%2BResurgence.jpg',
        fanart='https://3.bp.blogspot.com/-Ffjn6fWlv-o/V3m4dZR1p8I/AAAAAAAABOI/o8F2P4m_VDgp6xDAzT6yEFVb1wBVoGC5wCLcB/s1600/Independence%2BDay%2BResurgence.jpg',
        info_labels={"originaltitle":"Independence Day Resurgence","genre":"crime,british", "plot":"Two decades after the first Independence Day invasion, Earth is faced with a new extra-Solar threat. But will mankind's new space defenses be enough? ", "mpaa":"18"}) 	

    Add_Dir(name='Ghostbusters 2016 Extended', url='http://greeksattv.co.uk/Mario/Ghostbusters.2016.EXTENDED.720p.BRRip.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BMTg3OTM4NTM4NV5BMl5BanBnXkFtZTgwOTI3NDc0OTE@._V1_UY1200_CR89,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMTg3OTM4NTM4NV5BMl5BanBnXkFtZTgwOTI3NDc0OTE@._V1_UY1200_CR89,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Ghostbusters 2016 Extended","genre":"crime,british", "plot":"Following a ghost invasion of Manhattan, paranormal enthusiasts Erin Gilbert and Abby Yates, nuclear engineer Jillian Holtzmann, and subway worker Patty Tolan band together to stop the otherworldly threat", "mpaa":"18"}) 	

    Add_Dir(name='Ghostbusters', url='http://greeksattv.co.uk/Mario/Ghost.Busters.1984.4K.Remastered.Edition.720p.BluRay.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://i.dailymail.co.uk/i/pix/2014/08/29/article-2738009-20E7844700000578-546_634x971.jpg',
        fanart='http://i.dailymail.co.uk/i/pix/2014/08/29/article-2738009-20E7844700000578-546_634x971.jpg',
        info_labels={"originaltitle":"Ghostbusters","genre":"crime,british", "plot":"Three former parapsychology professors set up shop as a unique ghost removal service", "mpaa":"18"})	

    Add_Dir(name='Ghostbusters 2', url='http://greeksattv.co.uk/Mario/Ghostbusters.II.1989.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://fanart.tv/fanart/movies/2978/movieposter/ghostbusters-ii-5925290024c45.jpg',
        fanart='https://fanart.tv/fanart/movies/2978/movieposter/ghostbusters-ii-5925290024c45.jpg',
        info_labels={"originaltitle":"Ghostbusters 2","genre":"crime,british", "plot":"Three former parapsychology professors set up shop as a unique ghost removal service", "mpaa":"18"}) 	

    Add_Dir(name='Sherlock Holmes', url='http://greeksattv.co.uk/Mario/Sherlock%20Holmes%202009.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.guardarefilm.biz/uploads/posts/2014-08/1407107554_sherlock-holmes-2009-streaming.jpg',
        fanart='http://www.guardarefilm.biz/uploads/posts/2014-08/1407107554_sherlock-holmes-2009-streaming.jpg',
        info_labels={"originaltitle":"Sherlock Holmes","genre":"crime,british", "plot":"Detective Sherlock Holmes and his stalwart partner Watson engage in a battle of wits and brawn with a nemesis whose plot is a threat to all of England", "mpaa":"18"})	

    Add_Dir(name='Sherlock Holmes A Game Of Shadows', url='http://greeksattv.co.uk/Mario/Sherlock.Holmes.A.Game.Of.Shadows.2011.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.filmofilia.com/wp-content/uploads/2011/10/sherlock_holmes_2-poster.jpg',
        fanart='http://www.filmofilia.com/wp-content/uploads/2011/10/sherlock_holmes_2-poster.jpg',
        info_labels={"originaltitle":"Sherlock Holmes A Game Of Shadows","genre":"crime,british", "plot":"Sherlock Holmes and his sidekick Dr. Watson join forces to outwit and bring down their fiercest adversary, Professor Moriarty", "mpaa":"18"}) 	

    Add_Dir(name='Teenage Mutant Ninja Turtles Out Of The Shadows', url='http://greeksattv.co.uk/Mario/Teenage.Mutant.Ninja.Turtles.Out.of.the.Shadows.2016.720p.BluRay.x26.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/Teenage-Mutant-Ninja-Turtles-Out-of-the-Shadows-poster.jpg',
        fanart='https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/Teenage-Mutant-Ninja-Turtles-Out-of-the-Shadows-poster.jpg',
        info_labels={"originaltitle":"Teenage Mutant Ninja Turtles Out Of The Shadows","genre":"crime,british", "plot":"After facing Shredder, who has joined forces with mad scientist Baxter Stockman and henchmen Bebop and Rocksteady to take over the world, the Turtles must confront an even greater nemesis: the notorious Krang", "mpaa":"18"})	
		
    Add_Dir(name='Going In Style', url='http://greeksattv.co.uk/Mario/Going.In.Style.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5Mzg3NjI4OF5BMl5BanBnXkFtZTgwNzA3Mzg4MDI@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5Mzg3NjI4OF5BMl5BanBnXkFtZTgwNzA3Mzg4MDI@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Going In Style","genre":"crime,british", "plot":"Desperate to pay the bills and come through for their loved ones, three lifelong pals risk it all by embarking on a daring bid to knock off the very bank that absconded with their money", "mpaa":"18"}) 	

    Add_Dir(name='The Mummy', url='http://greeksattv.co.uk/Mario/The%20Mummy%20(2017)%20720p%20HC%20HDRip%20x264%20AAC.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.joblo.com/newsimages1/rsz-the-mummy-2017-poster.jpg',
        fanart='http://www.joblo.com/newsimages1/rsz-the-mummy-2017-poster.jpg',
        info_labels={"originaltitle":"The Mummy","genre":"crime,british", "plot":"An ancient princess is awakened from her crypt beneath the desert, bringing with her malevolence grown over millennia, and terrors that defy human comprehension", "mpaa":"18"}) 	

    Add_Dir(name='Alien Covenant', url='http://greeksattv.co.uk/Mario/Alien.Covenant.2017.V2.720p.HC.HDRip.950MB.MkvCage.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.alien-covenant.com/aliencovenant_uploads/POSTER.jpg',
        fanart='http://www.alien-covenant.com/aliencovenant_uploads/POSTER.jpg',
        info_labels={"originaltitle":"Alien Covenant","genre":"crime,british", "plot":"The crew of a colony ship, bound for a remote planet, discover an uncharted paradise with a threat beyond their imagination, and must attempt a harrowing escape", "mpaa":"18"}) 	

    Add_Dir(name='Life', url='http://greeksattv.co.uk/Mario/Life.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn1-www.comingsoon.net/assets/uploads/gallery/life-2017/life_ver3_xlg.jpg',
        fanart='http://cdn1-www.comingsoon.net/assets/uploads/gallery/life-2017/life_ver3_xlg.jpg',
        info_labels={"originaltitle":"Life","genre":"crime,british", "plot":"A team of scientists aboard the International Space Station discover a rapidly evolving life form, that caused extinction on Mars, and now threatens the crew and all life on Earth", "mpaa":"18"})	

    Add_Dir(name='Wonder Woman', url='http://greeksattv.co.uk/Mario/Wonder%20Woman%202017%20HC%20720p%20WEBRip%20999%20MB%20-%20iExTV.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.dccomics.com/sites/default/files/imce/2016/07-JUL/WWPosterRdcd_579260f4b9aba4.81209460.jpg',
        fanart='http://www.dccomics.com/sites/default/files/imce/2016/07-JUL/WWPosterRdcd_579260f4b9aba4.81209460.jpg',
        info_labels={"originaltitle":"Wonder Woman","genre":"crime,british", "plot":"Before she was Wonder Woman, she was Diana, princess of the Amazons, trained warrior. When a pilot crashes and tells of conflict in the outside world, she leaves home to fight a war, discovering her full powers and true destiny", "mpaa":"18"}) 	

    Add_Dir(name='Resident Evil Vendetta', url='http://greeksattv.co.uk/Mario/Resident.Evil.Vendetta.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/b/ba/Resident_Evil_Vendetta_poster.jpeg',
        fanart='https://upload.wikimedia.org/wikipedia/en/b/ba/Resident_Evil_Vendetta_poster.jpeg',
        info_labels={"originaltitle":"Resident Evil Vendetta","genre":"crime,british", "plot":"Chris Redfield enlists the help of Leon S. Kennedy and Rebecca Chambers to stop a death merchant, with a vengeance, from spreading a deadly virus in New York", "mpaa":"18"})	

    Add_Dir(name='Smurfs The Lost Village', url='http://greeksattv.co.uk/Mario/Smurfs.The.Lost.Village.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/0/07/Smurfs_The_Lost_Village_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/0/07/Smurfs_The_Lost_Village_poster.jpg',
        info_labels={"originaltitle":"Smurfs The Lost Village","genre":"crime,british", "plot":"In this fully animated, all-new take on the Smurfs, a mysterious map sets Smurfette and her friends Brainy, Clumsy and Hefty on an exciting race through the Forbidden Forest leading to the discovery of the biggest secret in Smurf history", "mpaa":"18"}) 	

    Add_Dir(name='The Recall', url='http://greeksattv.co.uk/Mario/The.Recall.2017.720p.WEB-DL.700MB.MkvCage.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://pbs.twimg.com/media/DBkAYTJXsAEmCpf.jpg',
        fanart='https://pbs.twimg.com/media/DBkAYTJXsAEmCpf.jpg',
        info_labels={"originaltitle":"The Recall","genre":"crime,british", "plot":"When five friends vacation at a remote lake house they expect nothing less than a good time, unaware that planet Earth is under an alien invasion and mass-abduction", "mpaa":"18"}) 	

    Add_Dir(name='Chips', url='http://greeksattv.co.uk/Mario/CHIPS.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.indiewire.com/wp-content/uploads/2017/01/chips.jpg',
        fanart='http://www.indiewire.com/wp-content/uploads/2017/01/chips.jpg',
        info_labels={"originaltitle":"Chips","genre":"crime,british", "plot":"A rookie officer is teamed with a hardened pro at the California Highway Patrol, though the newbie soon learns his partner is really an undercover Fed investigating a heist that may involve some crooked copsc", "mpaa":"18"}) 	

    Add_Dir(name='Power Rangers', url='http://greeksattv.co.uk/Mario/Power.Rangers.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/7/78/Power_Rangers_%282017_Official_Theatrical_Poster%29.png',
        fanart='https://upload.wikimedia.org/wikipedia/en/7/78/Power_Rangers_%282017_Official_Theatrical_Poster%29.png',
        info_labels={"originaltitle":"Power Rangers","genre":"crime,british", "plot":"A group of high-school students, who are infused with unique superpowers, harness their abilities in order to save the world", "mpaa":"18"}) 	

    Add_Dir(name='The Belko Experiment', url='http://greeksattv.co.uk/Mario/The.Belko.Experiment.2016.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/thumb/7/73/The_Belko_Experiment_poster.jpg/220px-The_Belko_Experiment_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/thumb/7/73/The_Belko_Experiment_poster.jpg/220px-The_Belko_Experiment_poster.jpg',
        info_labels={"originaltitle":"The Belko Experiment","genre":"crime,british", "plot":"In a twisted social experiment, eighty Americans are locked in their high-rise corporate office in Bogotá, Colombia, and ordered by an unknown voice coming from the company's intercom system to participate in a deadly game of kill or be killed", "mpaa":"18"}) 	

    Add_Dir(name='John Wick Chapter 2', url='http://greeksattv.co.uk/Mario/John.Wick.Chapter.2.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.trailer.ivid.it/movie/download/poster/jpg/john-wick-2-orig-locandina-300.jpg',
        fanart='http://www.trailer.ivid.it/movie/download/poster/jpg/john-wick-2-orig-locandina-300.jpg',
        info_labels={"originaltitle":"John Wick Chapter 2","genre":"crime,british", "plot":"After returning to the criminal underworld to repay a debt, John Wick discovers that a large bounty has been put on his life", "mpaa":"18"}) 	

    Add_Dir(name='The Lego Batman Movie', url='http://greeksattv.co.uk/Mario/The.LEGO.Batman.Movie.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.theshirleyjourney.com/wp-content/uploads/2017/02/the-lego-batman-movie-poster-691x1024.png',
        fanart='http://www.theshirleyjourney.com/wp-content/uploads/2017/02/the-lego-batman-movie-poster-691x1024.png',
        info_labels={"originaltitle":"The Lego Batman Movie","genre":"crime,british", "plot":"", "mpaa":"18"}) 	

    Add_Dir(name='Beauty And The Beast', url='http://greeksattv.co.uk/Mario/Beauty.And.The.Beast.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.movieweb.com/img.site/PHgk1X2GuMRGkg_1_l.jpg',
        fanart='http://cdn.movieweb.com/img.site/PHgk1X2GuMRGkg_1_l.jpg',
        info_labels={"originaltitle":"Beauty And The Beast","genre":"crime,british", "plot":"A cooler-than-ever Bruce Wayne must deal with the usual suspects as they plan to rule Gotham City, while discovering that he has accidentally adopted a teenage orphan who wishes to become his sidekick", "mpaa":"18"}) 	

    Add_Dir(name='Get Out', url='http://greeksattv.co.uk/Mario/Get.Out.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://sabzdl.xyz/wp-content/uploads/2017/04/Poster-2017-Get-Out-e1491242989143.jpg',
        fanart='http://sabzdl.xyz/wp-content/uploads/2017/04/Poster-2017-Get-Out-e1491242989143.jpg',
        info_labels={"originaltitle":"Get Out","genre":"crime,british", "plot":"It's time for a young African American to meet with his white girlfriend's parents for a weekend in their secluded estate in the woods, but before long, the friendly and polite ambience will give way to a nightmare", "mpaa":"18"}) 	

    Add_Dir(name='Colossal', url='http://greeksattv.co.uk/Mario/Colossal.2016.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.freaksugar.com/wp-content/uploads/2017/04/colossal-poster2.jpg',
        fanart='http://www.freaksugar.com/wp-content/uploads/2017/04/colossal-poster2.jpg',
        info_labels={"originaltitle":"Colossal","genre":"crime,british", "plot":"Gloria is an out-of-work party girl forced to leave her life in New York City, and move back home. When reports surface that a giant creature is destroying Seoul, she gradually comes to the realization that she is somehow connected to this phenomenon", "mpaa":"18"}) 		

    Add_Dir(name='Logan', url='http://greeksattv.co.uk/Mario/Logan.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://screencrush.com/files/2017/01/loganposter2.jpg',
        fanart='http://screencrush.com/files/2017/01/loganposter2.jpg',
        info_labels={"originaltitle":"Logan","genre":"crime,british", "plot":"In the near future, a weary Logan cares for an ailing Professor X, somewhere on the Mexican border. However, Logan's attempts to hide from the world, and his legacy, are upended when a young mutant arrives, pursued by dark forces", "mpaa":"18"}) 		

    Add_Dir(name='Ghost In The Shell', url='http://greeksattv.co.uk/Mario/Ghost.In.The.Shell.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn1-www.comingsoon.net/assets/uploads/2017/02/ghost-in-the-shell-poster-1-e1487814956866.jpg',
        fanart='http://cdn1-www.comingsoon.net/assets/uploads/2017/02/ghost-in-the-shell-poster-1-e1487814956866.jpg',
        info_labels={"originaltitle":"Ghost In The Shell","genre":"crime,british", "plot":"In the near future, Major is the first of her kind: A human saved from a terrible crash, who is cyber-enhanced to be a perfect soldier devoted to stopping the world's most dangerous criminals", "mpaa":"18"}) 		

    Add_Dir(name='xXx Return Of Xander Cage', url='http://greeksattv.co.uk/Mario/XXx.Return.Of.Xander.Cage.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://dyn4.media.titanbooks.com/products/9171/Untitled%2029.jpg',
        fanart='https://dyn4.media.titanbooks.com/products/9171/Untitled%2029.jpg',
        info_labels={"originaltitle":"xXx Return Of Xander Cage","genre":"crime,british", "plot":"Xander Cage is left for dead after an incident, though he secretly returns to action for a new, tough assignment with his handler Augustus Gibbons", "mpaa":"18"}) 		

    Add_Dir(name='The Founder', url='http://greeksattv.co.uk/Mario/The.Founder.2016.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.hollywoodchicago.com/sites/default/files/the-founder.jpg',
        fanart='http://www.hollywoodchicago.com/sites/default/files/the-founder.jpg',
        info_labels={"originaltitle":"The Founder","genre":"crime,british", "plot":"The story of Ray Kroc, a salesman who turned two brothers' innovative fast food eatery, McDonald's, into one of the biggest restaurant businesses in the world with a combination of ambition, persistence and ruthlessness", "mpaa":"18"}) 		

    Add_Dir(name='Sleepless', url='http://greeksattv.co.uk/Mario/Sleepless.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.newdvdreleasedates.com/images/posters/large/sleepless-2017-01.jpg',
        fanart='http://www.newdvdreleasedates.com/images/posters/large/sleepless-2017-01.jpg',
        info_labels={"originaltitle":"Sleepless","genre":"crime,british", "plot":"A cop with a connection to the criminal underworld scours a nightclub in search of his kidnapped son", "mpaa":"18"}) 		

    Add_Dir(name='Office Christmas Party', url='http://greeksattv.co.uk/Mario/Office.Christmas.Party.2016.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/8/8a/Office_Christmas_Party.png',
        fanart='https://upload.wikimedia.org/wikipedia/en/8/8a/Office_Christmas_Party.png',
        info_labels={"originaltitle":"Office Christmas Party","genre":"crime,british", "plot":"When his uptight CEO sister threatens to shut down his branch, the branch manager throws an epic Christmas party in order to land a big client and save the day, but the party gets way out of hand... ", "mpaa":"18"}) 		

    Add_Dir(name='Kong Skull Island', url='http://greeksattv.co.uk/Mario/Kong.Skull.Island.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://api.comingsoon.net//images//2017/poster_57517_1486991879.jpg',
        fanart='http://api.comingsoon.net//images//2017/poster_57517_1486991879.jpg',
        info_labels={"originaltitle":"Kong Skull Island","genre":"crime,british", "plot":"A team of scientists explore an uncharted island in the Pacific, venturing into the domain of the mighty Kong, and must fight to escape a primal Eden", "mpaa":"18"}) 		

    Add_Dir(name='The Magnificent Seven', url='http://greeksattv.co.uk/Mario/The.Magnificent.Seven.2016.720p.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.2oceansvibe.com/wp-content/uploads/2016/09/Mag-7-640x480.jpg',
        fanart='http://www.2oceansvibe.com/wp-content/uploads/2016/09/Mag-7-640x480.jpg',
        info_labels={"originaltitle":"The Magnificent Seven","genre":"crime,british", "plot":"Seven gunmen in the old west gradually come together to help a poor village against savage thieves", "mpaa":"18"}) 		

    Add_Dir(name='The Great Wall', url='http://greeksattv.co.uk/Mario/The.Great.Wall.2016.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://newbloommag.net/wp-content/uploads/2017/01/ihugyft.jpg',
        fanart='http://newbloommag.net/wp-content/uploads/2017/01/ihugyft.jpg',
        info_labels={"originaltitle":"The Great Wall","genre":"crime,british", "plot":"European mercenaries searching for black powder become embroiled in the defense of the Great Wall of China against a horde of monstrous creatures", "mpaa":"18"}) 		

    Add_Dir(name='Passengers', url='http://greeksattv.co.uk/Mario/Passengers.2016.720p.BluRay.H264.AAC-RARBG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.reelspoilers.com/wp-content/uploads/2017/01/245-683x1024.jpg',
        fanart='http://www.reelspoilers.com/wp-content/uploads/2017/01/245-683x1024.jpg',
        info_labels={"originaltitle":"Passengers","genre":"crime,british", "plot":"A spacecraft traveling to a distant colony planet and transporting thousands of people has a malfunction in its sleep chambers. As a result, two passengers are awakened 90 years early", "mpaa":"18"})	

    Add_Dir(name='Arrival', url='http://greeksattv.co.uk/Mario/Arrival.2016.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://lwlcdn.lwlies.com/wp-content/uploads/2016/11/Arrival-poster-900x0-c-default.jpg',
        fanart='http://lwlcdn.lwlies.com/wp-content/uploads/2016/11/Arrival-poster-900x0-c-default.jpg',
        info_labels={"originaltitle":"Arrival","genre":"crime,british", "plot":"When twelve mysterious spacecraft appear around the world, linguistics professor Louise Banks is tasked with interpreting the language of the apparent alien visitors", "mpaa":"18"}) 		

    Add_Dir(name='Jack Reacher Never Go Back', url='http://greeksattv.co.uk/Mario/Jack.Reacher.Never.Go.Back.2016.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/0/05/Jack_Reacher_Never_Go_Back_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/0/05/Jack_Reacher_Never_Go_Back_poster.jpg',
        info_labels={"originaltitle":"Jack Reacher Never Go Back","genre":"crime,british", "plot":"Jack Reacher must uncover the truth behind a major government conspiracy in order to clear his name. On the run as a fugitive from the law, Reacher uncovers a potential secret from his past that could change his life forever", "mpaa":"18"}) 		

    Add_Dir(name='Hacksaw Ridge', url='http://greeksattv.co.uk/Mario/Hacksaw.Ridge.2016.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.ytimg.com/vi/sXu9J1R5H8M/movieposter.jpg',
        fanart='https://i.ytimg.com/vi/sXu9J1R5H8M/movieposter.jpg',
        info_labels={"originaltitle":"Hacksaw Ridge","genre":"crime,british", "plot":"WWII American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, refuses to kill people, and becomes the first man in American history to receive the Medal of Honor without firing a shot", "mpaa":"18"}) 		

    Add_Dir(name='Phone Booth', url='http://greeksattv.co.uk/Mario/Phone.Booth.2002.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/c/c4/Phone_Booth_movie.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/c/c4/Phone_Booth_movie.jpg',
        info_labels={"originaltitle":"Phone Booth","genre":"crime,british", "plot":"Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle", "mpaa":"18"}) 		

    Add_Dir(name='Jurassic World', url='http://greeksattv.co.uk/Mario/Jurassic.World.2015.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://static2.hypable.com/wp-content/uploads/2015/04/jurassic-world-poster-dino-chris-pratt.jpg',
        fanart='http://static2.hypable.com/wp-content/uploads/2015/04/jurassic-world-poster-dino-chris-pratt.jpg',
        info_labels={"originaltitle":"Jurassic World","genre":"crime,british", "plot":"A new theme park, built on the original site of Jurassic Park, creates a genetically modified hybrid dinosaur, which escapes containment and goes on a killing spree", "mpaa":"18"}) 	

    Add_Dir(name='The Martian Extended', url='http://greeksattv.co.uk/Mario/The.Martian.2015.EXTENDED.720p.BRRip.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://static.hd-trailers.net/images/the-martian-104112-poster-xlarge.jpg',
        fanart='http://static.hd-trailers.net/images/the-martian-104112-poster-xlarge.jpg',
        info_labels={"originaltitle":"The Martian Extended","genre":"crime,british", "plot":"An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive", "mpaa":"18"}) 	

    Add_Dir(name='Assassins Creed', url='http://greeksattv.co.uk/Mario/Assassins.Creed.2016.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn3-www.superherohype.com/assets/uploads/gallery/assassins-creed-movie/asscreedinternational.jpg',
        fanart='http://cdn3-www.superherohype.com/assets/uploads/gallery/assassins-creed-movie/asscreedinternational.jpg',
        info_labels={"originaltitle":"Assassins Creed","genre":"crime,british", "plot":"Callum Lynch explores the memories of his ancestor Aguilar de Nerha and gains the skills of a Master Assassin, before taking on the secret Templar society", "mpaa":"18"}) 	

    Add_Dir(name='Central Intelligence', url='http://greeksattv.co.uk/Mario/Central.Intelligence.2016.UNRATED.720p.BRRip.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.hungrywatching.com/wp-content/uploads/2016/06/CentralIntelligence.jpg',
        fanart='http://www.hungrywatching.com/wp-content/uploads/2016/06/CentralIntelligence.jpg',
        info_labels={"originaltitle":"Central Intelligence","genre":"crime,british", "plot":"After he reconnects with an awkward pal from high school through Facebook, a mild-mannered accountant is lured into the world of international espionage", "mpaa":"18"}) 	

    Add_Dir(name='The Purge Election Year', url='http://greeksattv.co.uk/Mario/The.Purge.Election.Year.2016.720p.WEBRip.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://calendar.fiu.edu/wp-content/uploads/2016/10/PEY-11.jpg',
        fanart='https://calendar.fiu.edu/wp-content/uploads/2016/10/PEY-11.jpg',
        info_labels={"originaltitle":"The Purge Election Year","genre":"crime,british", "plot":"Former Police Sergeant Barnes becomes head of security for Senator Charlie Roan, a Presidential candidate targeted for death on Purge night due to her vow to eliminate the Purge", "mpaa":"18"}) 

    Add_Dir(name='Avatar Extended Collector Edition', url='http://greeksattv.co.uk/Mario/Avatar%20Extended%20Collectors%20Edition%202009.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://moviecultists.com/wp-content/uploads/2009/11/avatar-poster.jpg',
        fanart='http://moviecultists.com/wp-content/uploads/2009/11/avatar-poster.jpg',
        info_labels={"originaltitle":"","genre":"crime,british", "plot":"A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home", "mpaa":"18"}) 	

    Add_Dir(name='Ted 2', url='http://greeksattv.co.uk/Mario/Ted.2.2015.720p.BluRay.x264.YIFY.%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.cinencuentro.com/wp-content/uploads/2015/07/ted2-posterok.jpg',
        fanart='http://cdn.cinencuentro.com/wp-content/uploads/2015/07/ted2-posterok.jpg',
        info_labels={"originaltitle":"Ted 2","genre":"crime,british", "plot":"Newlywed couple Ted and Tami-Lynn want to have a baby, but in order to qualify to be a parent, Ted will have to prove he's a person in a court of law", "mpaa":"18"})

    Add_Dir(name='Death Race 2050', url='http://greeksattv.co.uk/Mario/Death.Race.2050.2017.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzNjA4MjgyMl5BMl5BanBnXkFtZTgwMTE1ODIyMDI@._V1_UY1200_CR155,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzNjA4MjgyMl5BMl5BanBnXkFtZTgwMTE1ODIyMDI@._V1_UY1200_CR155,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Death Race 2050","genre":"crime,british", "plot":"In the year 2050 the planet has become overpopulated, to help control population the government develops a Death Race. Annually competitors race across the country scoring points for killing people with their vehicles", "mpaa":"18"})
		
    Add_Dir(name='Cars', url='http://greeksattv.co.uk/Mario/Cars.2006.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/ef/66/79/ef6679c17de80fa3a22835274097a046--movie-cars-pixar-movies.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/ef/66/79/ef6679c17de80fa3a22835274097a046--movie-cars-pixar-movies.jpg',
        info_labels={"originaltitle":"Cars","genre":"crime,british", "plot":"A hot-shot race-car named Lightning McQueen gets waylaid in Radiator Springs, where he finds the true meaning of friendship and family", "mpaa":"18"}) 
				
    Add_Dir(name='Cars 2', url='http://greeksattv.co.uk/Mario/Cars.2.2011.720p.BrRip.264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://blog.bigmoviezone.com/images/Cars2Poster02_555px.jpg',
        fanart='http://blog.bigmoviezone.com/images/Cars2Poster02_555px.jpg',
        info_labels={"originaltitle":"Cars 2","genre":"crime,british", "plot":"Star race car Lightning McQueen and his pal Mater head overseas to compete in the World Grand Prix race. But the road to the championship becomes rocky as Mater gets caught up in an intriguing adventure of his own: international espionage", "mpaa":"18"}) 
		
    Add_Dir(name='Cars 3', url='http://greeksattv.co.uk/Mario/Cars.3.2017-HDTC-720p.Dual.YG.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/ce/d1/b0/ced1b01817c162f5fdc989cb245980f8.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/ce/d1/b0/ced1b01817c162f5fdc989cb245980f8.jpg',
        info_labels={"originaltitle":"Cars 3","genre":"crime,british", "plot":"Lightning McQueen sets out to prove to a new generation of racers that he's still the best race car in the world", "mpaa":"18"})
		
    Add_Dir(name='The Love Guru', url='http://greeksattv.co.uk/Mario/The%20Love%20Guru%20(2008).mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://static.rogerebert.com/uploads/movie/movie_poster/the-love-guru-2008/large_vUEXYLnsw6MKNEOvO3Ik4ev6VYm.jpg',
        fanart='http://static.rogerebert.com/uploads/movie/movie_poster/the-love-guru-2008/large_vUEXYLnsw6MKNEOvO3Ik4ev6VYm.jpg',
        info_labels={"originaltitle":"The Love Guru","genre":"crime,british", "plot":"Pitka, an American raised outside of his country by gurus, returns to the States in order to break into the self-help business. His first challenge is to settle the romantic troubles and subsequent professional skid of a star hockey player whose wife left him for a rival athlete", "mpaa":"18"}) 
				
    Add_Dir(name='Fun Fatboy Run', url='http://greeksattv.co.uk/Mario/Run.FatBoy.Run.2007.BrRip.720p.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://static.tvtropes.org/pmwiki/pub/images/run-fat-boy-run01_1797.jpg',
        fanart='http://static.tvtropes.org/pmwiki/pub/images/run-fat-boy-run01_1797.jpg',
        info_labels={"originaltitle":"Fun Fatboy Run","genre":"crime,british", "plot":"Five years after jilting his pregnant fiancée on their wedding day, out-of-shape Dennis decides to run a marathon to win her back", "mpaa":"18"})
						
    Add_Dir(name='The Strangers', url='http://greeksattv.co.uk/Mario/The.Strangers.2008.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://horrorfilmcentral.com/wp-content/uploads/2015/02/strangers_ver4_xlg.jpg',
        fanart='http://horrorfilmcentral.com/wp-content/uploads/2015/02/strangers_ver4_xlg.jpg',
        info_labels={"originaltitle":"The Strangers","genre":"crime,british", "plot":"A young couple staying in an isolated vacation home are terrorized by three unknown assailants", "mpaa":"18"})
								
    Add_Dir(name='Employee Of The Month', url='http://greeksattv.co.uk/Mario/Employee.of.the.Month.2006.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://resizing.flixster.com/ZsBE2rRub2_Wv_Z1knPgR7GzmcU=/800x1200/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/80/11178023_ori.jpg',
        fanart='http://resizing.flixster.com/ZsBE2rRub2_Wv_Z1knPgR7GzmcU=/800x1200/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/80/11178023_ori.jpg',
        info_labels={"originaltitle":"Employee Of The Month","genre":"crime,british", "plot":"A slacker competes with a repeat winner for the Employee of the Month title at work, in order to gain the affections of a new female employee", "mpaa":"18"})
								
    Add_Dir(name='Sleight', url='http://greeksattv.co.uk/Mario/Sleight.2016.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://cdn.traileraddict.com/content/unknown/sleight-2017-2.jpg',
        fanart='https://cdn.traileraddict.com/content/unknown/sleight-2017-2.jpg',
        info_labels={"originaltitle":"Sleight","genre":"crime,british", "plot":"A young street magician (Jacob Latimore) is left to care for his little sister after their parents passing, and turns to illegal activities to keep a roof over their heads. When he gets in too deep, his sister is kidnapped, and he is forced to use his magic and brilliant mind to save her", "mpaa":"18"})

    Add_Dir(name='Brotherhood', url='http://greeksattv.co.uk/Mario/Brotherhood.2016.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.mymovies.net/images/film/cin/350x522/fid16557.jpg',
        fanart='http://images.mymovies.net/images/film/cin/350x522/fid16557.jpg',
        info_labels={"originaltitle":"Brotherhood","genre":"crime,british", "plot":"With Sam facing up to the new world, he realizes it also comes with new problems and new challenges that he must face that he knows, will require old friends to help him survive new dangers", "mpaa":"18"}) 	

    Add_Dir(name='Planet Of The Apes 2001', url='http://greeksattv.co.uk/Mario/Planet.of.the.Apes.2001.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://static.rogerebert.com/uploads/movie/movie_poster/planet-of-the-apes-2001/large_gYQKMOwLolMRyofpRzXPAawiLPC.jpg',
        fanart='http://static.rogerebert.com/uploads/movie/movie_poster/planet-of-the-apes-2001/large_gYQKMOwLolMRyofpRzXPAawiLPC.jpg',
        info_labels={"originaltitle":"Planet Of The Apes 2001","genre":"crime,british", "plot":"An Air Force astronaut crash lands on a mysterious planet where evolved, talking apes dominate a race of primitive humans", "mpaa":"18"})	

    Add_Dir(name='Rise Of The Planet Of The Apes', url='http://greeksattv.co.uk/Mario/Rise.of.the.Planet.of.the.Apes.2011.BluRay.720p.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/27/02/be/2702be958ce50a7794480a9b3b25b28a.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/27/02/be/2702be958ce50a7794480a9b3b25b28a.jpg',
        info_labels={"originaltitle":"Rise Of The Planet Of The Apes","genre":"crime,british", "plot":"A substance designed to help the brain repair itself gives rise to a super-intelligent chimpanzee who leads an ape uprising", "mpaa":"18"}) 	

    Add_Dir(name='Dawn Of The Planet Of The Apes', url='http://greeksattv.co.uk/Mario/Dawn.of.the.Planet.of.the.Apes.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://s3.foxmovies.com/foxmovies/production/films/1/images/posters/368-asset-page.jpg',
        fanart='http://s3.foxmovies.com/foxmovies/production/films/1/images/posters/368-asset-page.jpg',
        info_labels={"originaltitle":"Dawn Of The Planet Of The Apes'","genre":"crime,british", "plot":"A growing nation of genetically evolved apes led by Caesar is threatened by a band of human survivors of the devastating virus unleashed a decade earlier", "mpaa":"18"}) 	

    Add_Dir(name='The Maze Runner The Scorch Trials', url='http://greeksattv.co.uk/Mario/Maze.Runner.The.Scorch.Trials.2015.BluRay.720p.%5BNightsdl.Com%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/83/4e/e8/834ee8a494de21f0118d75b37cc51cfd--the-scorch-trials-movie-posters.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/83/4e/e8/834ee8a494de21f0118d75b37cc51cfd--the-scorch-trials-movie-posters.jpg',
        info_labels={"originaltitle":"The Maze Runner The Scorch Trials","genre":"crime,british", "plot":"After having escaped the Maze, the Gladers now face a new set of challenges on the open roads of a desolate landscape filled with unimaginable obstacles", "mpaa":"18"}) 	

    Add_Dir(name='Knock Knock', url='http://greeksattv.co.uk/Mario/Knock.Knock.2015.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.dvdsreleasedates.com/posters/800/K/Knock-Knock-2015-movie-poster.jpg',
        fanart='http://www.dvdsreleasedates.com/posters/800/K/Knock-Knock-2015-movie-poster.jpg',
        info_labels={"originaltitle":"Knock Knock","genre":"crime,british", "plot":"A devoted father helps two stranded young women who knock on his door, but his kind gesture turns into a dangerous seduction and a deadly game of cat and mouse", "mpaa":"18"}) 	

    Add_Dir(name='Apollo 13', url='http://greeksattv.co.uk/Mario/Apollo.13.1995.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://img.moviepostershop.com/apollo-13-movie-poster-1995-1010190529.jpg',
        fanart='http://img.moviepostershop.com/apollo-13-movie-poster-1995-1010190529.jpg',
        info_labels={"originaltitle":"Apollo 13","genre":"crime,british", "plot":"NASA must devise a strategy to return Apollo 13 to Earth safely after the spacecraft undergoes massive internal damage putting the lives of the three astronauts on board in jeopardy", "mpaa":"18"})	

    Add_Dir(name='Armageddon', url='http://greeksattv.co.uk/Mario/Armageddon_1998.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/51yk78NeNUL.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/51yk78NeNUL.jpg',
        info_labels={"originaltitle":"Armageddon","genre":"crime,british", "plot":"After discovering that an asteroid the size of Texas is going to impact Earth in less than a month, N.A.S.A. recruits a misfit team of deep core drillers to save the planet", "mpaa":"18"})	

    Add_Dir(name='Deep Impact', url='http://greeksattv.co.uk/Mario/Deep.Impact.1998.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/5190IH2O9YL.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/5190IH2O9YL.jpg',
        info_labels={"originaltitle":"Deep Impact","genre":"crime,british", "plot":"Unless a comet can be destroyed before colliding with Earth, only those allowed into shelters will survive. Which people will survive?", "mpaa":"18"})	

    Add_Dir(name='Sausage Party', url='http://greeksattv.co.uk/Mario/Sausage.Party.2016.720p.BRRip.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.panicposters.com/media/catalog/product/cache/1/image/f63dc5ec28f3175f8a7f615bd217eb71/p/p/pp33947-sausage-party-poster.jpg',
        fanart='http://www.panicposters.com/media/catalog/product/cache/1/image/f63dc5ec28f3175f8a7f615bd217eb71/p/p/pp33947-sausage-party-poster.jpg',
        info_labels={"originaltitle":"Sausage Party","genre":"crime,british", "plot":"A sausage strives to discover the truth about his existence", "mpaa":"18"}) 	

    Add_Dir(name='South Park Bigger Longer And Uncut', url='http://greeksattv.co.uk/Mario/South.Park.Bigger.Longer.and.Uncut.1999.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://usercontent1.hubstatic.com/13189268.jpg',
        fanart='https://usercontent1.hubstatic.com/13189268.jpg',
        info_labels={"originaltitle":"South Park Bigger Longer And Uncut","genre":"crime,british", "plot":"When Cartman and his friends go see an R rated movie, they start swearing and their parent's think that Canada is to blame", "mpaa":"18"}) 		

    Add_Dir(name='The Man From U.N.C.L.E', url='http://greeksattv.co.uk/Mario/The%20Man%20from%20U.N.C.L.E.%202015%20BluRay%20720p%20%5BFilmia%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://img00.deviantart.net/fee9/i/2015/165/f/b/the_man_from_u_n_c_l_e_poster_by_sonic_sun-d8xbyt0.jpg',
        fanart='http://img00.deviantart.net/fee9/i/2015/165/f/b/the_man_from_u_n_c_l_e_poster_by_sonic_sun-d8xbyt0.jpg',
        info_labels={"originaltitle":"The Man From U.N.C.L.E","genre":"crime,british", "plot":"In the early 1960s, CIA agent Napoleon Solo and KGB operative Illya Kuryakin participate in a joint mission against a mysterious criminal organization, which is working to proliferate nuclear weapons", "mpaa":"18"}) 			

    Add_Dir(name='Son Of God', url='http://greeksattv.co.uk/Mario/Son.of.God.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/a/ae/Son_of_God_film_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/a/ae/Son_of_God_film_poster.jpg',
        info_labels={"originaltitle":"Son Of God","genre":"crime,british", "plot":"The life story of Jesus is told from his humble birth through his teachings, crucifixion and ultimate resurrection", "mpaa":"18"}) 	

    Add_Dir(name='The Wolf Of Wall Street', url='http://greeksattv.co.uk/Mario/The.Wolf.of.Wall.Street.2013.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/91gDgij-QML._SY445_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/91gDgij-QML._SY445_.jpg',
        info_labels={"originaltitle":"The Wolf Of Wall Street","genre":"crime,british", "plot":"Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government", "mpaa":"18"}) 			

    Add_Dir(name='Interstellar', url='http://greeksattv.co.uk/Mario/Interstellar.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar3.jpg',
        fanart='http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar3.jpg',
        info_labels={"originaltitle":"Interstellar","genre":"crime,british", "plot":"A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival", "mpaa":"18"}) 	

    Add_Dir(name='Terminator Genisys', url='http://greeksattv.co.uk/Mario/Terminator.Genisys.2015.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/b/bc/Terminator_Genisys.JPG',
        fanart='https://upload.wikimedia.org/wikipedia/en/b/bc/Terminator_Genisys.JPG',
        info_labels={"originaltitle":"Terminator Genisys","genre":"crime,british", "plot":"When John Connor, leader of the human resistance, sends Sgt. Kyle Reese back to 1984 to protect Sarah Connor and safeguard the future, an unexpected turn of events creates a fractured timeline", "mpaa":"18"}) 	

    Add_Dir(name='Edge Of Tomorrow', url='http://greeksattv.co.uk/Mario/Edge.of.Tomorrow.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://img03.deviantart.net/fcc5/i/2015/107/d/2/edge_of_tomorrow_poster_by_jonesyd1129-d7n7zbb.jpg',
        fanart='http://img03.deviantart.net/fcc5/i/2015/107/d/2/edge_of_tomorrow_poster_by_jonesyd1129-d7n7zbb.jpg',
        info_labels={"originaltitle":"Edge Of Tomorrow","genre":"crime,british", "plot":"A soldier fighting aliens gets to relive the same day over and over again, the day restarting every time he dies", "mpaa":"18"})

    Add_Dir(name='Titanic', url='http://greeksattv.co.uk/Mario/Titanic.1997.720p.HDTV.x264-YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/44/55/d9/4455d96357fb041d1cf3c8a5264ed593--titanic-leonardo-dicaprio-leonardo-dicaprio-kate-winslet.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/44/55/d9/4455d96357fb041d1cf3c8a5264ed593--titanic-leonardo-dicaprio-leonardo-dicaprio-kate-winslet.jpg',
        info_labels={"originaltitle":"Titanic","genre":"crime,british", "plot":"A soldier fighting aliens gets to relive the same day over and over again, the day restarting every time he dies", "mpaa":"18"}) 	

    Add_Dir(name='Gravity', url='http://greeksattv.co.uk/Mario/Gravity.2013.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.moviemoviepodcast.com/wp-content/uploads/2013/10/Gravity-Poster.jpg',
        fanart='http://www.moviemoviepodcast.com/wp-content/uploads/2013/10/Gravity-Poster.jpg',
        info_labels={"originaltitle":"Gravity","genre":"crime,british", "plot":"Two astronauts work together to survive after an accident which leaves them alone in space", "mpaa":"18"}) 	

    Add_Dir(name='San Andreas', url='http://greeksattv.co.uk/Mario/San.Andreas.2015.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/3/38/San_Andreas_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/3/38/San_Andreas_poster.jpg',
        info_labels={"originaltitle":"San Andreas","genre":"crime,british", "plot":"In the aftermath of a massive earthquake in California, a rescue-chopper pilot makes a dangerous journey with his ex-wife across the state in order to rescue his daughter.", "mpaa":"18"}) 	

    Add_Dir(name='Weird Science', url='http://greeksattv.co.uk/Mario/Weird.Science.1985.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-production.global.ssl.fastly.net/uploads/photos/file/60772/weird-science-cast.jpg',
        fanart='https://images-production.global.ssl.fastly.net/uploads/photos/file/60772/weird-science-cast.jpg',
        info_labels={"originaltitle":"Weird Science","genre":"crime,british", "plot":"Gary Wallace and Wyatt Donnelly create their dream woman, Lisa, on their computer. Lisa has extraordinary powers and can grant the boys their wishes for short periods of time", "mpaa":"18"})	

    Add_Dir(name='The Taking Of Pelham 1 2 3', url='http://greeksattv.co.uk/Mario/The.Taking.of.Pelham.1.2.3.2009.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.sonypictures.com/movies/thetakingofpelham123/assets/images/onesheet.jpg',
        fanart='http://www.sonypictures.com/movies/thetakingofpelham123/assets/images/onesheet.jpg',
        info_labels={"originaltitle":"The Taking Of Pelham 1 2 3","genre":"crime,british", "plot":"Armed men hijack a New York City subway train, holding the passengers hostage in return for a ransom, and turning an ordinary day's work for dispatcher Walter Garber into a face-off with the mastermind behind the crime", "mpaa":"18"}) 	

    Add_Dir(name='Law Abiding Citizen', url='http://greeksattv.co.uk/Mario/Law.Abiding.Citizen.720p.BrRip.450MB.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.filmofilia.com/wp-content/uploads/2009/08/lawabidingcitizen.jpg',
        fanart='http://www.filmofilia.com/wp-content/uploads/2009/08/lawabidingcitizen.jpg',
        info_labels={"originaltitle":"Law Abiding Citizen","genre":"crime,british", "plot":"Armed men hijack a New York City subway train, holding the passengers hostage in return for a ransom, and turning an ordinary day's work for dispatcher Walter Garber into a face-off with the mastermind behind the crime", "mpaa":"18"})	

    Add_Dir(name='The Karate Kid', url='http://greeksattv.co.uk/Mario/The.Karate.Kid.2010.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.sonypictures.com/movies/thekaratekid/assets/images/onesheet.jpg',
        fanart='http://www.sonypictures.com/movies/thekaratekid/assets/images/onesheet.jpg',
        info_labels={"originaltitle":"The Karate Kid","genre":"crime,british", "plot":"Work causes a single mother to move to China with her young son; in his new home, the boy embraces kung fu, taught to him by a master", "mpaa":"18"}) 	

    Add_Dir(name='White House Down', url='http://greeksattv.co.uk/Mario/White.House.Down.2013.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.sonypictures.com/movies/whitehousedown/assets/images/onesheet.jpg',
        fanart='http://www.sonypictures.com/movies/whitehousedown/assets/images/onesheet.jpg',
        info_labels={"originaltitle":"White House Down","genre":"crime,british", "plot":"While on a tour of the White House with his young daughter, a Capitol policeman springs into action to save his child and protect the president from a heavily armed group of paramilitary invaders", "mpaa":"18"})

    Add_Dir(name='Passenger 57', url='http://greeksattv.co.uk/Mario/Passenger.57.1992.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/12/80/ee/1280ee4d5e770c4d5b5d3cd4ae6dfda8--passenger-.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/12/80/ee/1280ee4d5e770c4d5b5d3cd4ae6dfda8--passenger-.jpg',
        info_labels={"originaltitle":"Passenger 57","genre":"crime,british", "plot":"An airline security expert must take action when he finds himself trapped on a passenger jet when terrorists seize control of it", "mpaa":"18"}) 	

    Add_Dir(name='Percy Jackson Sea Of Monsters', url='http://greeksattv.co.uk/Mario/Percy.Jackson.Sea.of.Monsters.2013.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/percy-jackson-sea-of-monsters.843.jpg',
        fanart='https://i.jeded.com/i/percy-jackson-sea-of-monsters.843.jpg',
        info_labels={"originaltitle":"Percy Jackson Sea Of Monsters","genre":"crime,british", "plot":"In order to restore their dying safe haven, the son of Poseidon and his friends embark on a quest to the Sea of Monsters, to find the mythical Golden Fleece, all the while trying to stop an ancient evil from rising", "mpaa":"18"})

    Add_Dir(name='Meet The Spartans', url='http://greeksattv.co.uk/Mario/Meet.the.Spartans.2008.720p.BluRay.H264.AAC-RARBG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/61ptYqiiONL._SY445_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/61ptYqiiONL._SY445_.jpg',
        info_labels={"originaltitle":"Meet The Spartans","genre":"crime,british", "plot":"The heroic Spartan king Leonidas, armed with nothing but leather underwear and a cape, leads a ragtag bunch of 13 Spartan misfit warriors to defend their homeland against thousands of invading Persians whom include the Ghost Rider, Rocky Balboa, the Autobots, and an ugly hunchbacked Paris Hilton and a shaved-head Brittany Spears", "mpaa":"18"}) 	

    Add_Dir(name='Robocop 2014', url='http://greeksattv.co.uk/Mario/RoboCop.2014.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifi-movies.com/images/contenu/data/0002036/affiche-robocop-2014-7.jpg',
        fanart='http://www.scifi-movies.com/images/contenu/data/0002036/affiche-robocop-2014-7.jpg',
        info_labels={"originaltitle":"Robocop 2014","genre":"crime,british", "plot":"In 2028 Detroit, when Alex Murphy - a loving husband, father and good cop - is critically injured in the line of duty, the multinational conglomerate OmniCorp sees their chance for a part-man, part-robot police officer", "mpaa":"18"})

    Add_Dir(name='The Dictator', url='http://greeksattv.co.uk/Mario/The.Dictator.2012.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://static.rogerebert.com/uploads/movie/movie_poster/the-dictator-2012/large_uAvG211cGNKSFyPzXFVMZzjkBB8.jpg',
        fanart='http://static.rogerebert.com/uploads/movie/movie_poster/the-dictator-2012/large_uAvG211cGNKSFyPzXFVMZzjkBB8.jpg',
        info_labels={"originaltitle":"The Dictator","genre":"crime,british", "plot":"The heroic story of a dictator who risked his life to ensure that democracy would never come to the country he so lovingly oppressed", "mpaa":"18"})	
		
    Add_Dir(name='2012', url='http://greeksattv.co.uk/Mario/2012.2009.BluRay.720p.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.filmofilia.com/wp-content/uploads/2009/08/2012_poster_3.jpg',
        fanart='http://www.filmofilia.com/wp-content/uploads/2009/08/2012_poster_3.jpg',
        info_labels={"originaltitle":"2012","genre":"crime,british", "plot":"A frustrated writer struggles to keep his family alive when a series of global catastrophes threatens to annihilate mankind", "mpaa":"18"})

    Add_Dir(name='Entrapment', url='http://greeksattv.co.uk/Mario/Entrapment.1999.Br.720p.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/58/65/08/5865080be4a25bfa42d079923b47da8c.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/58/65/08/5865080be4a25bfa42d079923b47da8c.jpg',
        info_labels={"originaltitle":"Entrapment","genre":"crime,british", "plot":"An insurance agent is sent by her employer to track down and help capture an art thief", "mpaa":"18"}) 	

    Add_Dir(name='Southpaw', url='http://greeksattv.co.uk/Mario/Southpaw.2015.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/8/89/Southpaw_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/8/89/Southpaw_poster.jpg',
        info_labels={"originaltitle":"Southpaw","genre":"crime,british", "plot":"Boxer Billy Hope turns to trainer Tick Wills to help him get his life back on track after losing his wife in a tragic accident and his daughter to child protection services", "mpaa":"18"})

    Add_Dir(name='Focus', url='http://greeksattv.co.uk/Mario/Focus.2015.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/b/bf/2015_Focus_film_poster.png',
        fanart='https://upload.wikimedia.org/wikipedia/en/b/bf/2015_Focus_film_poster.png',
       info_labels={"originaltitle":"Focus","genre":"crime,british", "plot":"In the midst of veteran con man Nicky's latest scheme, a woman from his past - now an accomplished femme fatale - shows up and throws his plans for a loop", "mpaa":"18"}) 	

    Add_Dir(name='Friends With Benifits', url='http://greeksattv.co.uk/Mario/Friends.with.Benefits.2011.720p.BrRip.264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://pic.pimg.tw/marcolee/1324141013-2148906624.jpg',
        fanart='http://pic.pimg.tw/marcolee/1324141013-2148906624.jpg"',
        info_labels={"originaltitle":"Friends With Benifits","genre":"crime,british", "plot":"A young man and woman decide to take their friendship to the next level without becoming a couple, but soon discover that adding sex only leads to complications", "mpaa":"18"})		

    Add_Dir(name='Friday 13th Extended Killer Cut', url='http://greeksattv.co.uk/Mario/Friday%20the%2013th%20(Extended%20Killer%20Cut)%20(2009)%20BRRip%20Xvid%20AC3-Anarchy.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://gruesomemagazine.com/wp-content/uploads/sites/6/2015/11/image.jpeg',
        fanart='http://gruesomemagazine.com/wp-content/uploads/sites/6/2015/11/image.jpeg',
        info_labels={"originaltitle":"Friday 13th Extended Killer Cut","genre":"crime,british", "plot":"A group of young adults discover a boarded up Camp Crystal Lake, where they soon encounter Jason Voorhees and his deadly intentions", "mpaa":"18"}) 

    Add_Dir(name='Get Hard', url='http://greeksattv.co.uk/Mario/Get.Hard.2015.EXTENDED.720p.WEB-DL.Tehmovies.com.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/thumb/3/38/Get_Hard_film_poster.png/220px-Get_Hard_film_poster.png',
        fanart='https://upload.wikimedia.org/wikipedia/en/thumb/3/38/Get_Hard_film_poster.png/220px-Get_Hard_film_poster.png',
        info_labels={"originaltitle":"Get Hard","genre":"crime,british", "plot":"When millionaire James King is jailed for fraud and bound for San Quentin, he turns to Darnell Lewis to prep him to go behind bars", "mpaa":"18"})

    Add_Dir(name='World War Z', url='http://greeksattv.co.uk/Mario/World.War.Z.2013.Unrated.720p.BluRay.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/d/dc/World_War_Z_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/d/dc/World_War_Z_poster.jpg',
        info_labels={"originaltitle":"World War Z","genre":"crime,british", "plot":"Former United Nations employee Gerry Lane traverses the world in a race against time to stop the Zombie pandemic that is toppling armies and governments, and threatening to destroy humanity itself", "mpaa":"18"})

    Add_Dir(name='I Am Legend', url='http://greeksattv.co.uk/Mario/I.am.legend.720p.450mbmu.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.best-horror-movies.com/i-am-legend-movie.jpg',
        fanart='http://images.best-horror-movies.com/i-am-legend-movie.jpg',
        info_labels={"originaltitle":"I Am Legend","genre":"crime,british", "plot":"Years after a plague kills most of humanity and transforms the rest into monsters, the sole survivor in New York City struggles valiantly to find a cure", "mpaa":"18"})

    Add_Dir(name='The Mask', url='http://greeksattv.co.uk/Mario/The.Mask.1994.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://static.rogerebert.com/uploads/movie/movie_poster/the-mask-1994/large_7plBoAhunhRVVmNCVMVo47Ede53.jpg',
        fanart='http://static.rogerebert.com/uploads/movie/movie_poster/the-mask-1994/large_7plBoAhunhRVVmNCVMVo47Ede53.jpg',
        info_labels={"originaltitle":"The Mask","genre":"crime,british", "plot":"Bank clerk Stanley Ipkiss is transformed into a manic superhero when he wears a mysterious mask", "mpaa":"18"}) 

    Add_Dir(name='Spy', url='http://greeksattv.co.uk/Mario/Spy.2015.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://static.metacritic.com/images/products/movies/2/7bfcc176839e151c210121fdcebb984c.jpg',
        fanart='http://static.metacritic.com/images/products/movies/2/7bfcc176839e151c210121fdcebb984c.jpg',
        info_labels={"originaltitle":"Spy","genre":"crime,british", "plot":"A desk-bound CIA analyst volunteers to go undercover to infiltrate the world of a deadly arms dealer, and prevent diabolical global disaster", "mpaa":"18"}) 

    Add_Dir(name='Prometheus', url='http://greeksattv.co.uk/Mario/Prometheus.2012.720p.BluRay.X264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/13/19/13/13191385877429a00299d1e085e71dcc.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/13/19/13/13191385877429a00299d1e085e71dcc.jpg',
        info_labels={"originaltitle":"Prometheus","genre":"crime,british", "plot":"Following clues to the origin of mankind, a team finds a structure on a distant moon, but they soon realize they are not alone", "mpaa":"18"}) 

    Add_Dir(name='Demolition Man', url='http://greeksattv.co.uk/Mario/Demolition.Man.1993.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.publispain.com/posters/demolition_man.jpg',
        fanart='http://www.publispain.com/posters/demolition_man.jpg',
        info_labels={"originaltitle":"Demolition Man","genre":"crime,british", "plot":"A police officer is brought out of suspended animation in prison to pursue an old ultra-violent nemesis who is loose in a non-violent future society", "mpaa":"18"}) 

    Add_Dir(name='In Time', url='http://greeksattv.co.uk/Mario/In.Time.2011.720p.Bluray.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://howdoesthemovieend.com/images/jmovies/img_pictures/in-time-poster.jpg',
        fanart='http://howdoesthemovieend.com/images/jmovies/img_pictures/in-time-poster.jpg',
        info_labels={"originaltitle":"In Time","genre":"crime,british", "plot":"In a future where people stop aging at 25, but are engineered to live only one more year, having the means to buy your way out of the situation is a shot at immortal youth. Here, Will Salas finds himself accused of murder and on the run with a hostage - a connection that becomes an important part of the way against the system", "mpaa":"18"}) 

    Add_Dir(name='Wreck It Ralph', url='http://greeksattv.co.uk/Mario/Wreck.it.Ralph.2012.720p.BrRip.x264.BOKUTOX.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.collider.com/wp-content/uploads/wreck-it-ralph-poster-main-characters.jpg',
        fanart='http://cdn.collider.com/wp-content/uploads/wreck-it-ralph-poster-main-characters.jpg',
        info_labels={"originaltitle":"Wreck It Ralph","genre":"crime,british", "plot":"A video game villain wants to be a hero and sets out to fulfill his dream, but his quest brings havoc to the whole arcade where he lives", "mpaa":"18"}) 

    Add_Dir(name='The Raid Redemption', url='http://greeksattv.co.uk/Mario/The.Raid.Redemption.2011.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/9/9a/The_Raid_2011_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/9/9a/The_Raid_2011_poster.jpg',
        info_labels={"originaltitle":"The Raid Redemption","genre":"crime,british", "plot":"A S.W.A.T. team becomes trapped in a tenement run by a ruthless mobster and his army of killers and thugs", "mpaa":"18"})

    Add_Dir(name='The Raid 2 Berandal', url='http://greeksattv.co.uk/Mario/The.Raid.2.2014.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/9/9a/The_Raid_2011_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/9/9a/The_Raid_2011_poster.jpg',
        info_labels={"originaltitle":"The Raid 2 Berandal","genre":"crime,british", "plot":"Only a short time after the first raid, Rama goes undercover with the thugs of Jakarta and plans to bring down the syndicate and uncover the corruption within his police force", "mpaa":"18"}) 

    Add_Dir(name='Man Of Steel', url='http://greeksattv.co.uk/Mario/Man.of.Steel.2013.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.collider.com/wp-content/uploads/man-of-steel-poster4.jpg',
        fanart='http://cdn.collider.com/wp-content/uploads/man-of-steel-poster4.jpg',
        info_labels={"originaltitle":"Man Of Steel","genre":"crime,british", "plot":"Clark Kent, one of the last of an extinguished race disguised as an unremarkable human, is forced to reveal his identity when Earth is invaded by an army of survivors who threaten to bring the planet to the brink of destruction", "mpaa":"18"})

    Add_Dir(name='Non Stop', url='http://greeksattv.co.uk/Mario/Non%20Stop%202014%20BluRay%20720p.%5BDownloado.Ir%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BOTI3NzcxMjkzMl5BMl5BanBnXkFtZTgwMDY0NTQ0MDE@._V1_UY1200_CR64,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BOTI3NzcxMjkzMl5BMl5BanBnXkFtZTgwMDY0NTQ0MDE@._V1_UY1200_CR64,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Non Stop","genre":"crime,british", "plot":"An air marshal springs into action during a transatlantic flight after receiving a series of text messages demanding $150 million into an off-shore account, or someone will die every 20 minutes", "mpaa":"18"}) 

    Add_Dir(name='Parker', url='http://greeksattv.co.uk/Mario/Parker.2013.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4MzM2NTQ1Nl5BMl5BanBnXkFtZTcwODIyODY1OA@@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4MzM2NTQ1Nl5BMl5BanBnXkFtZTcwODIyODY1OA@@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Parker","genre":"crime,british", "plot":"A thief with a unique code of professional ethics is double-crossed by his crew and left for dead. Assuming a new disguise and forming an unlikely alliance with a woman on the inside, he looks to hijack the score of the crew's latest heist", "mpaa":"18"})

    Add_Dir(name='Hollow Man', url='http://greeksattv.co.uk/Mario/Hollow.Man.2000.DC.720p.BRRip.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://myst-library.ru/uploads/files_elfinder/my_files/KINO/KINO%20News%204/Hollow-Man-731783.jpg',
        fanart='http://myst-library.ru/uploads/files_elfinder/my_files/KINO/KINO%20News%204/Hollow-Man-731783.jpg',
        info_labels={"originaltitle":"Hollow Man","genre":"crime,british", "plot":"Scientists discover how to make people invisible, but their test subject becomes an insane killer who stalks them", "mpaa":"18"}) 
		
    Add_Dir(name='Hollow Man 2', url='http://greeksattv.co.uk/Mario/Hollow.Man.II.2006.DVDRip.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/51s9kJWqMaL.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/51s9kJWqMaL.jpg',
        info_labels={"originaltitle":"Hollow Man 2","genre":"crime,british", "plot":"A Seattle detective and a biologist are on the run from a dangerous invisible assassin gone rogue", "mpaa":"18"}) 

    Add_Dir(name='Bruce Almighty', url='http://greeksattv.co.uk/Mario/Bruce.Almighty.2003.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/6/60/BruceAlmighty_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/6/60/BruceAlmighty_poster.jpg',
        info_labels={"originaltitle":"Bruce Almighty","genre":"crime,british", "plot":"A guy who complains about God too often is given almighty powers to teach him how difficult it is to run the world", "mpaa":"18"})

    Add_Dir(name='Evan Almighty', url='http://greeksattv.co.uk/Mario/Evan.Almighty.2007.BluRay.720p.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.themoviemind.com/wp-content/uploads/2008/05/evan-almighty.jpg',
        fanart='http://www.themoviemind.com/wp-content/uploads/2008/05/evan-almighty.jpg',
        info_labels={"originaltitle":"Evan Almighty","genre":"crime,british", "plot":"God contacts Congressman Evan Baxter and tells him to build an ark in preparation for a great flood", "mpaa":"18"}) 

    Add_Dir(name='Sorority Row', url='http://greeksattv.co.uk/Mario/Sorority.Row.2009.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/sorority-row.16386.jpg',
        fanart='https://i.jeded.com/i/sorority-row.16386.jpg',
        info_labels={"originaltitle":"Sorority Row","genre":"crime,british", "plot":"A group of sorority sisters try to cover up the death of their house-sister after a prank gone wrong, only to be stalked by a serial killer", "mpaa":"18"})

    Add_Dir(name='Watchmen Directors Cut', url='http://greeksattv.co.uk/Mario/Watchmen%20(2009)%20Dir%20Cut%20720p%20BRRip.mkv-muxed.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.watchmencomicmovie.com/posters/watchmen-theatrical-poster-big.jpg',
        fanart='http://www.watchmencomicmovie.com/posters/watchmen-theatrical-poster-big.jpg',
        info_labels={"originaltitle":"Watchmen","genre":"crime,british", "plot":"In 1985 where former superheroes exist, the murder of a colleague sends active vigilante Rorschach into his own sprawling investigation, uncovering something that could completely change the course of history as we know it", "mpaa":"18"}) 		

    Add_Dir(name='1408', url='http://greeksattv.co.uk/Mario/1408%20(2007)%20%5BDCBRRip%20600mb.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/thumb/6/63/1408poster.jpg/220px-1408poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/thumb/6/63/1408poster.jpg/220px-1408poster.jpg',
        info_labels={"originaltitle":"1408","genre":"crime,british", "plot":"A man who specializes in debunking paranormal occurrences checks into the fabled room 1408 in the Dolphin Hotel. Soon after settling in, he confronts genuine terror", "mpaa":"18"})

    Add_Dir(name='Dumb And Dumber Too', url='http://greeksattv.co.uk/Mario/Dumb.and.Dumber.To.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/b1/97/0a/b1970acfd26901456a0af436b279be43.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/b1/97/0a/b1970acfd26901456a0af436b279be43.jpg',
        info_labels={"originaltitle":"Dumb And Dumber Too","genre":"crime,british", "plot":"Twenty years since their first adventure, Lloyd and Harry go on a road trip to find Harry's newly discovered daughter, who was given up for adoption", "mpaa":"18"}) 

    Add_Dir(name='Total Recall Extended 2012', url='http://greeksattv.co.uk/Mario/Total.Recall.EXTENDED.2012.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://fontmeme.com/images/Total-Recall-Poster.jpg',
        fanart='https://fontmeme.com/images/Total-Recall-Poster.jpg',
        info_labels={"originaltitle":"Total Recall","genre":"crime,british", "plot":"A factory worker, Douglas Quaid, begins to suspect that he is a spy after visiting Rekall - a company that provides its clients with implanted fake memories of a life they would like to have led - goes wrong and he finds himself on the run", "mpaa":"18"})

    Add_Dir(name='The Perfect Match', url='http://greeksattv.co.uk/Mario/The.Perfect.Match.2016.720p.BluRay.x264.VPPV.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/2/2b/ThePerfectMatchPoster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/2/2b/ThePerfectMatchPoster.jpg',
        info_labels={"originaltitle":"The Perfect Match","genre":"crime,british", "plot":"A playboy named Charlie, convinced that all his relationships are dead, meets the beautiful and mysterious Eva. Agreeing to a casual affair, Charlie then wants a bit more from their relationship", "mpaa":"18"})

    Add_Dir(name='Forbidden Kingdom', url='http://greeksattv.co.uk/Mario/The%20Forbidden%20Kingdom.2008.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/5/51/ForbiddenKingdomPoster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/5/51/ForbiddenKingdomPoster.jpg',
        info_labels={"originaltitle":"Forbidden Kingdom","genre":"crime,british", "plot":"A discovery made by a kung fu obsessed American teen sends him on an adventure to China, where he joins up with a band of martial arts warriors in order to free the imprisoned Monkey King", "mpaa":"18"}) 

    Add_Dir(name='Blue Streak', url='http://greeksattv.co.uk/Mario/Blue.Streak.1999.720p.BluRay.X264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/a/ab/Blue_Streak_film_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/a/ab/Blue_Streak_film_poster.jpg',
        info_labels={"originaltitle":"Blue Streak","genre":"crime,british", "plot":"A former convict poses as a cop to retrieve a diamond he stole years ago", "mpaa":"18"}) 

    Add_Dir(name='G.I Joe Rise Of The Cobra', url='http://greeksattv.co.uk/Mario/G.I.%20Joe%20Rise%20of%20Cobra.2009.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.collider.com/wp-content/image-base/Movies/G/GI_Joe_Movie/Movie_Posters/GI%20Joe%20movie%20poster.jpg',
        fanart='http://cdn.collider.com/wp-content/image-base/Movies/G/GI_Joe_Movie/Movie_Posters/GI%20Joe%20movie%20poster.jpg',
        info_labels={"originaltitle":"G.I Joe Rise Of The Cobra","genre":"crime,british", "plot":"An elite military unit comprised of special operatives known as G.I. Joe, operating out of The Pit, takes on an evil organization led by a notorious arms dealer", "mpaa":"18"}) 

    Add_Dir(name='G.I Joe Retaliation', url='http://greeksattv.co.uk/Mario/G.I..Joe_.Retaliation.2013.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.collider.com/wp-content/uploads/gi-joe-retaliation-final-poster.jpg',
        fanart='http://cdn.collider.com/wp-content/uploads/gi-joe-retaliation-final-poster.jpg',
        info_labels={"originaltitle":"G.I Joe Retaliation","genre":"crime,british", "plot":"The G.I. Joes are not only fighting their mortal enemy Cobra; they are forced to contend with threats from within the government that jeopardize their very existence", "mpaa":"18"}) 

    Add_Dir(name='The Perfect Guy', url='http://greeksattv.co.uk/Mario/The.Perfect.Guy.2015.720p.BRRip.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NzcwMTkzMF5BMl5BanBnXkFtZTgwMDAwNDUxNjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NzcwMTkzMF5BMl5BanBnXkFtZTgwMDAwNDUxNjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"The Perfect Guy","genre":"crime,british", "plot":"After breaking up with her boyfriend, a professional woman gets involved with a man who seems almost too good to be true", "mpaa":"18"}) 

    Add_Dir(name='No Good Deed', url='http://greeksattv.co.uk/Mario/No.Good.Deed.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/3/34/No_Good_Deed_2014_movie_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/3/34/No_Good_Deed_2014_movie_poster.jpg',
        info_labels={"originaltitle":"No Good Deed","genre":"crime,british", "plot":"An unstable escaped convict terrorizes a woman who is alone with her two children", "mpaa":"18"})

    Add_Dir(name='Godzilla 1998', url='http://greeksattv.co.uk/Mario/Godzilla.1998.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images2.coveralia.com/dvd/g/Godzilla-Interior_Frontal.jpg',
        fanart='http://images2.coveralia.com/dvd/g/Godzilla-Interior_Frontal.jpg',
        info_labels={"originaltitle":"Godzilla 1998","genre":"crime,british", "plot":"A giant, reptilian monster surfaces, leaving destruction in its wake. To stop the monster (and its babies), an earthworm scientist, his reporter ex-girlfriend, and other unlikely heroes team up to save their city", "mpaa":"18"})

    Add_Dir(name='Godzilla 2014', url='http://greeksattv.co.uk/Mario/Godzilla.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://cdn.traileraddict.com/content/warner-bros-pictures/godzilla2014-8.jpg',
        fanart='https://cdn.traileraddict.com/content/warner-bros-pictures/godzilla2014-8.jpg',
        info_labels={"originaltitle":"Godzilla 2014","genre":"crime,british", "plot":"The world is beset by the appearance of monstrous creatures, but one of them may be the only one who can save humanity", "mpaa":"18"}) 

    Add_Dir(name='Pixels', url='http://greeksattv.co.uk/Mario/Pixels.2015.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/thumb/f/f0/PixelsOfficialPoster.jpg/220px-PixelsOfficialPoster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/thumb/f/f0/PixelsOfficialPoster.jpg/220px-PixelsOfficialPoster.jpg',
        info_labels={"originaltitle":"Pixels","genre":"crime,british", "plot":"When aliens misinterpret video feeds of classic arcade games as a declaration of war, they attack the Earth in the form of the video games", "mpaa":"18"})

    Add_Dir(name='The Conjuring 2', url='http://greeksattv.co.uk/Mario/The.Conjuring.2.2016.720p.BluRay.x265.ShAaNiG.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/b/b9/Conjuring_2.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/b/b9/Conjuring_2.jpg',
        info_labels={"originaltitle":"The Conjuring 2","genre":"crime,british", "plot":"Lorraine and Ed Warren travel to north London to help a single mother raising four children alone in a house plagued by a malicious spirit", "mpaa":"18"}) 
		
    Add_Dir(name='Hitman Agent 47', url='http://greeksattv.co.uk/Mario/Hitman.Agent.47.2015.720p.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://hitman.com/assets-bin/images/pages/index/pack.jpg',
        fanart='https://hitman.com/assets-bin/images/pages/index/pack.jpg',
        info_labels={"originaltitle":"Hitman Agent 47","genre":"crime,british", "plot":"An assassin teams up with a woman to help her find her father and uncover the mysteries of her ancestry", "mpaa":"18"})

    Add_Dir(name='Transporter Refueled', url='http://greeksattv.co.uk/Mario/The.Transporter.Refueled.2015.720p.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/2/2c/%22The_Transporter_Refueled%22_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/2/2c/%22The_Transporter_Refueled%22_poster.jpg',
        info_labels={"originaltitle":"Transporter Refueled","genre":"crime,british", "plot":"In the south of France, former special-ops mercenary Frank Martin enters into a game of chess with a femme-fatale and her three sidekicks who are looking for revenge against a sinister Russian kingpin", "mpaa":"18"}) 	

    Add_Dir(name='Fantastic Four 2015', url='http://greeksattv.co.uk/Mario/Fantastic.Four.2015.720p.BluRay.x264.YIFY.%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.collider.com/wp-content/uploads/2015/07/fantastic-four-poster-international.jpg',
        fanart='http://cdn.collider.com/wp-content/uploads/2015/07/fantastic-four-poster-international.jpg',
        info_labels={"originaltitle":"Fantastic Four 2015","genre":"crime,british", "plot":"Four young outsiders teleport to an alternate and dangerous universe which alters their physical form in shocking ways. The four must learn to harness their new abilities and work together to save Earth from a former friend turned enemy", "mpaa":"18"})

    Add_Dir(name='Fantastic Four', url='http://greeksattv.co.uk/Mario/Fantastic%20Four%202005.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://thewatcherblog1.files.wordpress.com/2015/08/ff_poster.jpg',
        fanart='https://thewatcherblog1.files.wordpress.com/2015/08/ff_poster.jpg',
        info_labels={"originaltitle":"Fantastic Four","genre":"crime,british", "plot":"A group of astronauts gain superpowers after a cosmic radiation exposure and must use them to oppose the plans of their enemy, Doctor Victor Von Doom", "mpaa":"18"}) 

    Add_Dir(name='Fantastic Four Rise Of The Silver Surfer', url='http://greeksattv.co.uk/Mario/Fantastic%204%20Rise%20of%20the%20Silver%20Surfer%202007.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.firstshowing.net/img/new-blue-ff2.jpg',
        fanart='http://www.firstshowing.net/img/new-blue-ff2.jpg',
        info_labels={"originaltitle":"Fantastic Four Rise Of The Silver Surfer","genre":"crime,british", "plot":"The Fantastic Four learn that they aren't the only super-powered beings in the universe when they square off against the powerful Silver Surfer and the planet-eating Galactus", "mpaa":"18"})
		
    Add_Dir(name='Taken', url='http://greeksattv.co.uk/Mario/Taken%202008%20Extended%20Cut%20720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGViOGVkYmEtNDBmNC00ZmQwLWJiZmItZWJhYzQzY2EyNGNlL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_SX675_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGViOGVkYmEtNDBmNC00ZmQwLWJiZmItZWJhYzQzY2EyNGNlL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_SX675_AL_.jpg',
        info_labels={"originaltitle":"Taken","genre":"crime,british", "plot":"A retired CIA agent travels across Europe and relies on his old skills to save his estranged daughter, who has been kidnapped while on a trip to Paris", "mpaa":"18"})	
		
    Add_Dir(name='Taken 2', url='http://greeksattv.co.uk/Mario/Taken.2.2012.UNRATED.EXTENDED.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.filmofilia.com/wp-content/uploads/2012/10/taken_21.jpg',
        fanart='http://www.filmofilia.com/wp-content/uploads/2012/10/taken_21.jpg',
        info_labels={"originaltitle":"Taken 2","genre":"crime,british", "plot":"In Istanbul, retired CIA operative Bryan Mills and his wife are taken hostage by the father of a kidnapper Mills killed while rescuing his daughter", "mpaa":"18"})	
		
    Add_Dir(name='Taken 3', url='http://greeksattv.co.uk/Mario/Taken.3.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://image.tmdb.org/t/p/original/zZHozAJDzVe9oiWUxbnNkDxh5Lc.jpg',
        fanart='https://image.tmdb.org/t/p/original/zZHozAJDzVe9oiWUxbnNkDxh5Lc.jpg',
        info_labels={"originaltitle":"Taken 3","genre":"crime,british", "plot":"Ex-government operative Bryan Mills is accused of a ruthless murder he never committed or witnessed. As he is tracked and pursued, Mills brings out his particular set of skills to find the true killer and clear his name", "mpaa":"18"})	
		
    Add_Dir(name='Mission Impossible 3', url='http://greeksattv.co.uk/Mario/Mission.Impossible.III.2006.720p.BrRip.x264-YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://media.hollywood.com/images/666x1000/7311337.jpg',
        fanart='http://media.hollywood.com/images/666x1000/7311337.jpg',
        info_labels={"originaltitle":"Mission Impossible 3","genre":"crime,british", "plot":"Agent Ethan Hunt comes into conflict with a dangerous and sadistic arms dealer who threatens his life and his fianceé in response", "mpaa":"18"})
		
    Add_Dir(name='Mission Impossible Ghost Protocol', url='http://greeksattv.co.uk/Mario/Mission.Impossible.Ghost.Protocol.2011.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.collider.com/wp-content/uploads/mission-impossible-ghost-protocol-movie-poster-02.jpg',
        fanart='http://cdn.collider.com/wp-content/uploads/mission-impossible-ghost-protocol-movie-poster-02.jpg',
        info_labels={"originaltitle":"Mission Impossible Ghost Protocol","genre":"crime,british", "plot":"The IMF is shut down when it's implicated in the bombing of the Kremlin, causing Ethan Hunt and his new team to go rogue to clear their organization's name", "mpaa":"18"})	
		
    Add_Dir(name='Mission Impossible Rogue Nation', url='http://greeksattv.co.uk/Mario/Mission.Impossible.Rogue.Nation.2015.720p.BluRay.x264.VPPV.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/78/c2/59/78c259ae19ce186f749998baf428d9e4.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/78/c2/59/78c259ae19ce186f749998baf428d9e4.jpg',
        info_labels={"originaltitle":"Mission Impossible Rogue Nation","genre":"crime,british", "plot":"Ethan and team take on their most impossible mission yet, eradicating the Syndicate - an International rogue organization as highly skilled as they are, committed to destroying the IMF", "mpaa":"18"})
				
    Add_Dir(name='Resident Evil The Final Chapter', url='http://greeksattv.co.uk/Mario/Resident.Evil.The.Final.Chapter.2017.720p.WEBRip.x264.AAC-ETRG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn1-www.comingsoon.net/assets/uploads/gallery/resident-evil-the-final-chapter/last-resident-evil-poster.jpg',
        fanart='http://cdn1-www.comingsoon.net/assets/uploads/gallery/resident-evil-the-final-chapter/last-resident-evil-poster.jpg',
        info_labels={"originaltitle":"Resident Evil The Final Chapter","genre":"crime,british", "plot":"Alice returns to where the nightmare began: The Hive in Raccoon City, where the Umbrella Corporation is gathering its forces for a final strike against the only remaining survivors of the apocalypse", "mpaa":"18"})
				
    Add_Dir(name='Angels And Demons', url='http://greeksattv.co.uk/Mario/Angels.%26.Demons.2009.720p.BrRip.x264.YIFY%2BHI.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/4/44/Angels_and_demons.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/4/44/Angels_and_demons.jpg',
        info_labels={"originaltitle":"Angels And Demons","genre":"crime,british", "plot":"Harvard symbologist Robert Langdon works with a nuclear physicist to solve a murder and prevent a terrorist act against the Vatican during one of the significant events within the church", "mpaa":"18"})
				
    Add_Dir(name='The Da Vinci Code', url='http://greeksattv.co.uk/Mario/The.Da.Vinci.Code.2006.720p.EXTENDED.x264.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxMjQyMTc3Nl5BMl5BanBnXkFtZTcwMTA1MDUzMw@@._V1_UY1200_CR88,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxMjQyMTc3Nl5BMl5BanBnXkFtZTcwMTA1MDUzMw@@._V1_UY1200_CR88,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"The Da Vinci Code","genre":"crime,british", "plot":"A murder inside the Louvre and clues in Da Vinci paintings lead to the discovery of a religious mystery protected by a secret society for two thousand years -- which could shake the foundations of Christianity", "mpaa":"18"})
				
    Add_Dir(name='Inferno', url='http://greeksattv.co.uk/Mario/Inferno.2016.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.movienewz.com/img/films/inferno_movie_poster.jpg',
        fanart='http://www.movienewz.com/img/films/inferno_movie_poster.jpg',
        info_labels={"originaltitle":"Inferno","genre":"crime,british", "plot":"When Robert Langdon wakes up in an Italian hospital with amnesia, he teams up with Dr. Sienna Brooks, and together they must race across Europe against the clock to foil a deadly global plot", "mpaa":"18"})
				
    Add_Dir(name='London Has Fallen', url='http://greeksattv.co.uk/Mario/London.Has.Fallen.2016.720p.BluRay.H264.AAC-RARBG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/27/69/8b/27698b1e6589f8bba63ae6c89858ac95---movies-good-movies.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/27/69/8b/27698b1e6589f8bba63ae6c89858ac95---movies-good-movies.jpg',
        info_labels={"originaltitle":"London Has Fallen","genre":"crime,british", "plot":"In London for the Prime Minister's funeral, Mike Banning discovers a plot to assassinate all the attending world leaders", "mpaa":"18"})
				
    Add_Dir(name='Olympus Has Fallen', url='http://greeksattv.co.uk/Mario/Olympus.Has.Fallen.2013.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/ab/51/f3/ab51f3ab1ef21b2c74924b8cad2ef28c.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/ab/51/f3/ab51f3ab1ef21b2c74924b8cad2ef28c.jpg',
        info_labels={"originaltitle":"Olympus Has Fallen","genre":"crime,british", "plot":"Disgraced Secret Service agent (and former presidential guard) Mike Banning finds himself trapped inside the White House in the wake of a terrorist attack; using his inside knowledge, Banning works with national security to rescue the President from his kidnappers", "mpaa":"18"})
				
    Add_Dir(name='Now You See Me 2', url='http://greeksattv.co.uk/Mario/Now.You.See.Me.2.2016.720p.BluRay.x264.ShAaNiG.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.ramascreen.com/wp-content/uploads/2016/05/Now-You-See-Me-2-poster-image.jpg',
        fanart='http://www.ramascreen.com/wp-content/uploads/2016/05/Now-You-See-Me-2-poster-image.jpg',
        info_labels={"originaltitle":"Now You See Me 2","genre":"crime,british", "plot":"The Four Horsemen resurface and are forcibly recruited by a tech genius to pull off their most impossible heist yet", "mpaa":"18"})
						
    Add_Dir(name='Back To The Future Part 1', url='http://greeksattv.co.uk/Mario/Back.to.the.Future.1985.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.heyuguys.com/images/2010/08/Back-to-the-Future-Re-Release-Poster.jpg',
        fanart='http://www.heyuguys.com/images/2010/08/Back-to-the-Future-Re-Release-Poster.jpg',
        info_labels={"originaltitle":"Back To The Future Part 1","genre":"crime,british", "plot":"Marty McFly, a 17-year-old high school student, is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his close friend, the maverick scientist Doc Brown", "mpaa":"18"})
						
    Add_Dir(name='Back To The Future Part 2', url='http://greeksattv.co.uk/Mario/Back.to.the.Future.II.1989.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://keyartdesigns.com/wp-content/uploads/2010/08/back_to_the_future1.jpg',
        fanart='http://keyartdesigns.com/wp-content/uploads/2010/08/back_to_the_future1.jpg',
        info_labels={"originaltitle":"Back To The Future Part 2","genre":"crime,british", "plot":"After visiting 2015, Marty McFly must repeat his visit to 1955 to prevent disastrous changes to 1985...without interfering with his first trip", "mpaa":"18"})
						
    Add_Dir(name='Back To The Future Part 3', url='http://greeksattv.co.uk/Mario/Back.to.the.Future.III.1990.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://barkerhost.com/wp-content/uploads/sites/4/2015/04/6DmgPTZYaug7QNDjOhUDWyjOQDl-0.jpg',
        fanart='http://barkerhost.com/wp-content/uploads/sites/4/2015/04/6DmgPTZYaug7QNDjOhUDWyjOQDl-0.jpg',
        info_labels={"originaltitle":"Back To The Future Part 3","genre":"crime,british", "plot":"Enjoying a peaceable existence in 1885, Doctor Emmet Brown is about to be killed by Buford Mad Dog Tannen. Marty McFly travels back in time to save his friend", "mpaa":"18"})
						
    Add_Dir(name='Think Like A Man', url='http://greeksattv.co.uk/Mario/Think.Like.A.Man.2012.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://fanart.tv/fanart/movies/67660/movieposter/think-like-a-man-52c9486f2be94.jpg',
        fanart='https://fanart.tv/fanart/movies/67660/movieposter/think-like-a-man-52c9486f2be94.jpg',
        info_labels={"originaltitle":"Think Like A Man","genre":"crime,british", "plot":"Four friends conspire to turn the tables on their women when they discover the ladies have been using Steve Harvey's relationship advice against them", "mpaa":"18"})
						
    Add_Dir(name='Think Like A Man Too', url='http://greeksattv.co.uk/Mario/Think.Like.a.Man.Too.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://fanart.tv/fanart/movies/184098/movieposter/think-like-a-man-too-54066277a4946.jpg',
        fanart='https://fanart.tv/fanart/movies/184098/movieposter/think-like-a-man-too-54066277a4946.jpg',
        info_labels={"originaltitle":"Think Like A Man Too","genre":"crime,british", "plot":"All the couples are back for a wedding in Las Vegas, but plans for a romantic weekend go awry when their various misadventures get them into some compromising situations that threaten to derail the big event", "mpaa":"18"})
						
    Add_Dir(name='James Bond Skyfall', url='http://greeksattv.co.uk/Mario/Skyfall.2012.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://jamesbondbrasil.com/wp-content/uploads/2012/09/SF_UK_ONE-SHEET_MVK_EXCLUSIVE.jpg',
        fanart='http://jamesbondbrasil.com/wp-content/uploads/2012/09/SF_UK_ONE-SHEET_MVK_EXCLUSIVE.jpg',
        info_labels={"originaltitle":"James Bond Skyfall","genre":"crime,british", "plot":"Bond's loyalty to M is tested when her past comes back to haunt her. Whilst MI6 comes under attack, 007 must track down and destroy the threat, no matter how personal the cost", "mpaa":"18"})
						
    Add_Dir(name='James Bond Spectre', url='http://greeksattv.co.uk/Mario/Spectre.2015.Bluray.720p.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.jbsuits.com/blog/wp-content/uploads/2015/07/James-Bond-is-Back-with-SPECTRE.jpg',
        fanart='http://www.jbsuits.com/blog/wp-content/uploads/2015/07/James-Bond-is-Back-with-SPECTRE.jpg',
        info_labels={"originaltitle":"James Bond Spectre","genre":"crime,british", "plot":"A cryptic message from Bond's past sends him on a trail to uncover a sinister organization. While M battles political forces to keep the secret service alive, Bond peels back the layers of deceit to reveal the terrible truth behind SPECTRE", "mpaa":"18"})
						
    Add_Dir(name='James Bond Quantum Of Solace', url='http://greeksattv.co.uk/Mario/James.Bond.Quantum.of.Solace.2008.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://eosfitness.com/wp-content/uploads/2015/03/Quantum-of-solace.jpg',
        fanart='http://eosfitness.com/wp-content/uploads/2015/03/Quantum-of-solace.jpg',
        info_labels={"originaltitle":"James Bond Quantum Of Solace","genre":"crime,british", "plot":"James Bond descends into mystery as he tries to stop a mysterious organization from eliminating a country's most valuable resource. All the while, he still tries to seek revenge over the death of his love", "mpaa":"18"})
						
    Add_Dir(name='James Bond Casino Royale', url='http://greeksattv.co.uk/Mario/Casino.Royale.2006.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://fontmeme.com/images/Casino-Royale-Poster.jpg',
        fanart='https://fontmeme.com/images/Casino-Royale-Poster.jpg',
        info_labels={"originaltitle":"James Bond Casino Royale","genre":"crime,british", "plot":"Armed with a licence to kill, Secret Agent James Bond sets out on his first mission as 007 and must defeat a weapons dealer in a high stakes game of poker at Casino Royale, but things are not what they seem", "mpaa":"18"})
						
    Add_Dir(name='James Bond Die Another Day', url='http://greeksattv.co.uk/Mario/James.Bond.Die.Another.Day.2002.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/die-another-day-james-bond-007.19680.jpg',
        fanart='https://i.jeded.com/i/die-another-day-james-bond-007.19680.jpg',
        info_labels={"originaltitle":"James Bond Die Another Day","genre":"crime,british", "plot":"James Bond is sent to investigate the connection between a North Korean terrorist and a diamond mogul who is funding the development of an international space weapon", "mpaa":"18"})
						
    Add_Dir(name='James Bond The World Is Not Enough', url='http://greeksattv.co.uk/Mario/James.Bond.The.World.Is.Not.Enough.1999.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.posterbobs.com/007_world_is_not_enough.jpg',
        fanart='http://www.posterbobs.com/007_world_is_not_enough.jpg',
        info_labels={"originaltitle":"James Bond The World Is Not Enough","genre":"crime,british", "plot":"James Bond uncovers a nuclear plot when he protects an oil heiress from her former kidnapper, an international terrorist who can't feel pain", "mpaa":"18"})
						
    Add_Dir(name='James Bond Tomorrow Never Dies', url='http://greeksattv.co.uk/Mario/James.Bond.Tomorrow.Never.Dies.1997.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://img07.deviantart.net/e8c5/i/2013/161/1/9/tomorrow_never_dies_poster_by_comandercool22-d68ldad.jpg',
        fanart='http://img07.deviantart.net/e8c5/i/2013/161/1/9/tomorrow_never_dies_poster_by_comandercool22-d68ldad.jpg',
        info_labels={"originaltitle":"","genre":"crime,british", "plot":"James Bond heads to stop a media mogul's plan to induce war between China and the UK in order to obtain exclusive global media coverage", "mpaa":"18"})
						
    Add_Dir(name='Matrix', url='http://greeksattv.co.uk/Mario/The.Matrix.1999.720p.BrRip.264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://thebitplayers.net/wp-content/uploads/2015/08/the-matrix-movie-poster.jpg',
        fanart='http://thebitplayers.net/wp-content/uploads/2015/08/the-matrix-movie-poster.jpg',
        info_labels={"originaltitle":"James Bond Tomorrow Never Dies","genre":"crime,british", "plot":"A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers", "mpaa":"18"})
								
    Add_Dir(name='Matrix Reloaded', url='http://greeksattv.co.uk/Mario/The.Matrix.Reloaded.2003.720p.BrRip.264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/95/4d/2b/954d2ba64597ba26c0705d54c5663bec.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/95/4d/2b/954d2ba64597ba26c0705d54c5663bec.jpg',
        info_labels={"originaltitle":"Matrix Reloaded","genre":"crime,british", "plot":"Neo and the rebel leaders estimate that they have 72 hours until 250,000 probes discover Zion and destroy it and its inhabitants. During this, Neo must decide how he can save Trinity from a dark fate in his dreams", "mpaa":"18"})
								
    Add_Dir(name='Matrix Revolutions', url='http://greeksattv.co.uk/Mario/The.Matrix.Revolutions.2003.720p.BrRip.264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/2f/84/c0/2f84c049b905eddddedd72e4425ca432.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/2f/84/c0/2f84c049b905eddddedd72e4425ca432.jpg',
        info_labels={"originaltitle":"Matrix Revolutions","genre":"crime,british", "plot":"The human city of Zion defends itself against the massive invasion of the machines as Neo fights to end the war at another front while also opposing the rogue Agent Smith", "mpaa":"18"})
								
    Add_Dir(name='300', url='http://greeksattv.co.uk/Mario/300.2006.BluRay.720p.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://womenwriteaboutcomics.com/wp-content/uploads/2014/12/300.-Directed-by-Zack-Snyder.-2006.-Movie-Poster..jpg',
        fanart='http://womenwriteaboutcomics.com/wp-content/uploads/2014/12/300.-Directed-by-Zack-Snyder.-2006.-Movie-Poster..jpg',
        info_labels={"originaltitle":"300","genre":"crime,british", "plot":"King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C", "mpaa":"18"})
								
    Add_Dir(name='300 Rise Of An Empire', url='http://greeksattv.co.uk/Mario/300.Rise.of.an.Empire.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BMTEwNTU2MjAwMDdeQTJeQWpwZ15BbWU3MDk2Njc2Njk@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMTEwNTU2MjAwMDdeQTJeQWpwZ15BbWU3MDk2Njc2Njk@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"300 Rise Of An Empire","genre":"crime,british", "plot":"Greek general Themistokles leads the charge against invading Persian forces led by mortal-turned-god Xerxes and Artemisia, vengeful commander of the Persian navy", "mpaa":"18"})
								
    Add_Dir(name='Austin Powers International Man Of Mystery', url='http://greeksattv.co.uk/Mario/Austin.Powers.International.Man.of.Mystery.1997.720p.Brrip.x264.Deceit.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/a1/ec/5c/a1ec5c1c8676c25224d645e9d305b678--s-movies--films.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/a1/ec/5c/a1ec5c1c8676c25224d645e9d305b678--s-movies--films.jpg',
        info_labels={"originaltitle":"Austin Powers International Man Of Mystery","genre":"crime,british", "plot":"A 1960s hipster secret agent is brought out of cryofreeze to oppose his greatest enemy in the 1990s, where his social attitudes are glaringly out of place", "mpaa":"18"})
								
    Add_Dir(name='Austin Powers The Spy Who Shagged Me', url='http://greeksattv.co.uk/Mario/Austin.Powers.The.Spy.Who.Shagged.Me.1999.720p.Brrip.x264.Deceit.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/79/79a3308b13cd31f096d8a4a34f96b66b_500x735.jpg',
        fanart='https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/79/79a3308b13cd31f096d8a4a34f96b66b_500x735.jpg',
        info_labels={"originaltitle":"Austin Powers The Spy Who Shagged Me","genre":"crime,british", "plot":"Dr. Evil is back...and has invented a new time machine that allows him to go back to the 60s and steal Austin Powers's mojo, inadvertently leaving him shagless", "mpaa":"18"})
								
    Add_Dir(name='Austin Powers Goldmember', url='http://greeksattv.co.uk/Mario/Austin.Powers.Goldmember.2002.720p.Brrip.x264.Deceit.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/70/70117ee3c0b15a2950f1e82a215e812b_500x735.jpg',
        fanart='https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/70/70117ee3c0b15a2950f1e82a215e812b_500x735.jpg',
        info_labels={"originaltitle":"Austin Powers Goldmember","genre":"crime,british", "plot":"Upon learning that his father has been kidnapped, Austin Powers must travel to 1975 and defeat the aptly named villain Goldmember - who is working with Dr. Evil", "mpaa":"18"})
								
    Add_Dir(name='American Pie', url='http://greeksattv.co.uk/Mario/American.Pie.1999.720p.x264.Br.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/d7/5c/d9/d75cd93350c00910fd25fec6b8bf0278.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/d7/5c/d9/d75cd93350c00910fd25fec6b8bf0278.jpg',
        info_labels={"originaltitle":"American Pie","genre":"crime,british", "plot":"Four teenage boys enter a pact to lose their virginity by prom night", "mpaa":"18"})
								
    Add_Dir(name='American Pie 2', url='http://greeksattv.co.uk/Mario/American.Pie.2.2001.720p.Br.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/24/19/f1/2419f1b82deb7aa9d1292741ccbfa19a--movieposter-pies.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/24/19/f1/2419f1b82deb7aa9d1292741ccbfa19a--movieposter-pies.jpg',
        info_labels={"originaltitle":"American Pie 2","genre":"crime,british", "plot":"In this sequel to the hit comedy American Pie 1999, the high school students are now in college. These close friends decide to meet up at the beach house for some fun", "mpaa":"18"})
								
    Add_Dir(name='American Pie Band Camp', url='http://greeksattv.co.uk/Mario/American.Pie.Band.Camp.720p.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/08/d1/1a/08d11a4461240abf0d0876cb8d6cc58b.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/08/d1/1a/08d11a4461240abf0d0876cb8d6cc58b.jpg',
        info_labels={"originaltitle":"American Pie Band Camp","genre":"crime,british", "plot":"Matt Stifler wants to be just like his big bro, making porn movies and having a good time in college. After sabotaging the school band, he gets sent to band camp where he really doesn't like it at first but then learns how to deal with the bandeez", "mpaa":"18"})
								
    Add_Dir(name='American Pie Beta House', url='http://greeksattv.co.uk/Mario/American.Pie.Beta.House.720p.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://blueprintreview.co.uk/wp-content/uploads/2012/05/600full-american-pie-presents-beta-house-poster.jpg',
        fanart='http://blueprintreview.co.uk/wp-content/uploads/2012/05/600full-american-pie-presents-beta-house-poster.jpg',
        info_labels={"originaltitle":"American Pie Beta House","genre":"crime,british", "plot":"Erik, and Cooze start college and pledge the Beta House fraternity, presided over by none other than legendary Dwight Stifler. But chaos ensues when a fraternity of geeks threatens to stop the debauchery and the Betas have to make a stand for their right to party", "mpaa":"18"})
								
    Add_Dir(name='American Pie The Book Of Love', url='http://greeksattv.co.uk/Mario/American.Pie.7-Presents.The.Book.of.Love.720p.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/0f/9f/26/0f9f2665716047977ef5b6de3c6291b8.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/0f/9f/26/0f9f2665716047977ef5b6de3c6291b8.jpg',
        info_labels={"originaltitle":"American Pie The Book Of Love","genre":"crime,british", "plot":"Three new hapless virgins discover the Bible hidden in the school library at East Great Falls High. Unfortunately for them, the book is ruined, and with incomplete advice, the Bible leads them on a hilarious journey to lose their virginity", "mpaa":"18"})
								
    Add_Dir(name='American Pie The Naked Mile', url='http://greeksattv.co.uk/Mario/American.Pie.The.Naked.Mile.720p.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/95/c0/24/95c024c43882a6157f2060ce3dec398d--pie-movie-comedy-movies.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/95/c0/24/95c024c43882a6157f2060ce3dec398d--pie-movie-comedy-movies.jpg',
        info_labels={"originaltitle":"American Pie The Naked Mile","genre":"crime,british", "plot":"When Erik Stifler gets a free pass to do whatever he wants from his girlfriend, he and his two best friends head to see his cousin Dwight for the Naked Mile and a weekend they will never forget", "mpaa":"18"})
								
    Add_Dir(name='American Pie Reunion', url='http://greeksattv.co.uk/Mario/American%20Pie%20Reunion%202012%20Unrated%20720p%20BRrip%20x264%20%5BECLiPSE%20HD%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/American-Reunion-Poster.jpg',
        fanart='https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/American-Reunion-Poster.jpg',
        info_labels={"originaltitle":"American Pie Reunion","genre":"crime,british", "plot":"Jim, Michelle, Stifler, and their friends reunite in East Great Falls, Michigan for their high school reunion", "mpaa":"18"})
										
    Add_Dir(name='Mechanic Resurrection', url='http://greeksattv.co.uk/Mario/Mechanic.Resurrection.2016.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BMjYwODExNzUwMV5BMl5BanBnXkFtZTgwNTgwNjUyOTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMjYwODExNzUwMV5BMl5BanBnXkFtZTgwNTgwNjUyOTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Mechanic Resurrection","genre":"crime,british", "plot":"Arthur Bishop thought he had put his murderous past behind him, until his most formidable foe kidnaps the love of his life. Now he is forced to travel the globe to complete three impossible assassinations, and do what he does best: make them look like accidents", "mpaa":"18"})
										
    Add_Dir(name='Scream', url='http://greeksattv.co.uk/Mario/Scream%201996.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/c2/60/26/c26026ea822c42c6325a046f31fbc2bf--scream-series-scream-movie.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/c2/60/26/c26026ea822c42c6325a046f31fbc2bf--scream-series-scream-movie.jpg',
        info_labels={"originaltitle":"Scream","genre":"crime,british", "plot":"A year after the murder of her mother, a teenage girl is terrorized by a new killer, who targets the girl and her friends by using horror films as part of a deadly game", "mpaa":"18"})
										
    Add_Dir(name='Scream 2', url='http://greeksattv.co.uk/Mario/Scream%202%201997.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/7/7f/Scream_2.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/7/7f/Scream_2.jpg',
        info_labels={"originaltitle":"Scream 2","genre":"crime,british", "plot":"Two years after the first series of murders, a new psychopath dons the Ghostface costume and a new string of killings begins", "mpaa":"18"})
										
    Add_Dir(name='Scream 3', url='http://greeksattv.co.uk/Mario/Scream%203%202000.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://ryancshowers.files.wordpress.com/2013/08/521936_493969627351248_1423471281_n.jpg',
        fanart='https://ryancshowers.files.wordpress.com/2013/08/521936_493969627351248_1423471281_n.jpg',
        info_labels={"originaltitle":"Scream 3","genre":"crime,british", "plot":"While Sidney and her friends visit the Hollywood set of Stab 3, the third film based on the Woodsboro murders, a new Ghostface begins to terrorize them once again", "mpaa":"18"})
										
    Add_Dir(name='Scream 4', url='http://greeksattv.co.uk/Mario/scream.4.2011.720p.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://addictedtohorrormovies.files.wordpress.com/2014/08/scream4fanposter_themadbutcher_classic.jpg',
        fanart='https://addictedtohorrormovies.files.wordpress.com/2014/08/scream4fanposter_themadbutcher_classic.jpg',
        info_labels={"originaltitle":"Scream 4","genre":"crime,british", "plot":"Ten years have passed, and Sidney Prescott, who has put herself back together thanks in part to her writing, is visited by the Ghostface Killer", "mpaa":"18"})
										
    Add_Dir(name='Men In Black', url='http://greeksattv.co.uk/Mario/Men.In.Black.1997.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.dvdsreleasedates.com/posters/800/M/Men-in-Black-movie-poster.jpg',
        fanart='http://www.dvdsreleasedates.com/posters/800/M/Men-in-Black-movie-poster.jpg',
        info_labels={"originaltitle":"Men In Black","genre":"crime,british", "plot":"A police officer joins a secret organization that polices and monitors extraterrestrial interactions on Earth", "mpaa":"18"})
										
    Add_Dir(name='Men In Black 2', url='http://greeksattv.co.uk/Mario/Men.In.Black.II.2002.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/a5/21/54/a5215448328ce09bc288e9ad92414dc4.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/a5/21/54/a5215448328ce09bc288e9ad92414dc4.jpg',
        info_labels={"originaltitle":"Men In Black 2","genre":"crime,british", "plot":"Agent J needs help so he is sent to find Agent K and restore his memory", "mpaa":"18"})
										
    Add_Dir(name='Men In Black 3', url='http://greeksattv.co.uk/Mario/Men.In.Black.3.2012.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.collider.com/wp-content/uploads/men-in-black-3-movie-poster-jones.jpg',
        fanart='http://cdn.collider.com/wp-content/uploads/men-in-black-3-movie-poster-jones.jpg',
        info_labels={"originaltitle":"Men In Black 3","genre":"crime,british", "plot":"Agent J travels in time to M.I.B.'s early days in 1969 to stop an alien from assassinating his friend Agent K and changing history", "mpaa":"18"})
										
    Add_Dir(name='Oceans Eleven', url='http://greeksattv.co.uk/Mario/Oceans%20Eleven%202001.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/10/fa/80/10fa80f776e452bcd304ee1dacc217af.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/10/fa/80/10fa80f776e452bcd304ee1dacc217af.jpg',
        info_labels={"originaltitle":"Oceans Eleven","genre":"crime,british", "plot":"Danny Ocean and his eleven accomplices plan to rob three Las Vegas casinos simultaneously", "mpaa":"18"})
										
    Add_Dir(name='Oceans Twelve', url='http://greeksattv.co.uk/Mario/Oceans%20Twelve%202004.720p.BrRip.YIFY.mp', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ3NTIyMzczMF5BMl5BanBnXkFtZTYwMjgzNTg2._V1_UY1200_CR90,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ3NTIyMzczMF5BMl5BanBnXkFtZTYwMjgzNTg2._V1_UY1200_CR90,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Oceans Twelve","genre":"crime,british", "plot":"Daniel Ocean recruits one more team member so he can pull off three major European heists in this sequel to Ocean's 11", "mpaa":"18"})
										
    Add_Dir(name='Oceans Thirteen', url='http://greeksattv.co.uk/Mario/Oceans%20Thirteen%202007.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://zuts.files.wordpress.com/2013/06/oceans-thirteen-poster.jpg',
        fanart='https://zuts.files.wordpress.com/2013/06/oceans-thirteen-poster.jpg',
        info_labels={"originaltitle":"Oceans Thirteen","genre":"crime,british", "plot":"Danny Ocean rounds up the boys for a third heist, after casino owner Willy Bank double-crosses one of the original eleven, Reuben Tishkoff", "mpaa":"18"})
										
    Add_Dir(name='Piranha', url='http://greeksattv.co.uk/Mario/Piranha.2010.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://farm8.staticflickr.com/7026/13665815784_bc774d69e5_b.jpg',
        fanart='https://farm8.staticflickr.com/7026/13665815784_bc774d69e5_b.jpg',
        info_labels={"originaltitle":"Piranha","genre":"crime,british", "plot":"After a sudden underwater tremor sets free scores of the prehistoric man-eating fish, an unlikely group of strangers must band together to stop themselves from becoming fish food for the area's new razor-toothed residents", "mpaa":"18"})
										
    Add_Dir(name='Piranha 3DD', url='http://greeksattv.co.uk/Mario/Piranha.3DD.2012.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://img.cinemablend.com/cb/9/4/7/1/4/6/94714660aec02d04a6f505cef430710152b594bb296904a561aaea6fac2dafa8.jpg',
        fanart='http://img.cinemablend.com/cb/9/4/7/1/4/6/94714660aec02d04a6f505cef430710152b594bb296904a561aaea6fac2dafa8.jpg',
        info_labels={"originaltitle":"Piranha 3DD","genre":"crime,british", "plot":"After the events at Lake Victoria, the pre-historic school of blood-thirsty piranhas make their way into a newly opened waterpark", "mpaa":"18"})
										
    Add_Dir(name='Bean', url='http://greeksattv.co.uk/Mario/Mr.Bean.1997.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/3/37/Bean_movie_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/3/37/Bean_movie_poster.jpg',
        info_labels={"originaltitle":"Bean","genre":"crime,british", "plot":"The bumbling Mr. Bean travels to America when he is given the responsibility of bringing a highly valuable painting to a Los Angeles museum", "mpaa":"18"})
										
    Add_Dir(name='Mr Beans Holiday', url='http://greeksattv.co.uk/Mario/Mr.Beans.Holiday.2007.720p.BRrip.x264.GAZ.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://fanart.tv/fanart/movies/1268/movieposter/mr-beans-holiday-531c3fdbc679d.jpg',
        fanart='https://fanart.tv/fanart/movies/1268/movieposter/mr-beans-holiday-531c3fdbc679d.jpg',
        info_labels={"originaltitle":"Mr Beans Holiday","genre":"crime,british", "plot":"Mr. Bean wins a trip to Cannes where he unwittingly separates a young boy from his father and must help the two come back together. On the way he discovers France, bicycling, and true love, among other things", "mpaa":"18"})
										
    Add_Dir(name='Die Hard', url='http://greeksattv.co.uk/Mario/Die.Hard.1988.720p.BrRip.x264.bitloks.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BMzNmY2IwYzAtNDQ1NC00MmI4LThkOTgtZmVhYmExOTVhMWRkXkEyXkFqcGdeQXVyMTk5NDA3Nw@@._V1_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMzNmY2IwYzAtNDQ1NC00MmI4LThkOTgtZmVhYmExOTVhMWRkXkEyXkFqcGdeQXVyMTk5NDA3Nw@@._V1_.jpg',
        info_labels={"originaltitle":"Die Hard","genre":"crime,british", "plot":"John McClane, officer of the NYPD, tries to save his wife Holly Gennaro and several others that were taken hostage by German terrorist Hans Gruber during a Christmas party at the Nakatomi Plaza in Los Angeles", "mpaa":"18"})
										
    Add_Dir(name='Die Hard 2', url='http://greeksattv.co.uk/Mario/Die.Hard.2.1990.720p.BrRip.x264.bitloks.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://fanart.tv/fanart/movies/1573/movieposter/die-hard-2-578ef7e68c11c.jpg',
        fanart='https://fanart.tv/fanart/movies/1573/movieposter/die-hard-2-578ef7e68c11c.jpg',
        info_labels={"originaltitle":"Die Hard 2","genre":"crime,british", "plot":"John McClane attempts to avert disaster as rogue military operatives seize control of Dulles International Airport in Washington, D.C", "mpaa":"18"})
												
    Add_Dir(name='Die Hard 3', url='http://greeksattv.co.uk/Mario/Die.Hard.3.1995.720p.BrRip.x264.bitloks.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://manilovefilms.com/wp-content/uploads/2012/01/diehard3-poster.jpg',
        fanart='http://manilovefilms.com/wp-content/uploads/2012/01/diehard3-poster.jpg',
        info_labels={"originaltitle":"Die Hard 3","genre":"crime,british", "plot":"John McClane and a Harlem store owner are targeted by German terrorist Simon Gruber in New York City, where he plans to rob the Federal Reserve Building", "mpaa":"18"})
												
    Add_Dir(name='Die Hard 4', url='http://greeksattv.co.uk/Mario/Die.Hard.4.2007.720p.BrRip.x264.bitloks.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/94/7e/2a/947e2af24c01bb5d73d48f6d81348f06.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/94/7e/2a/947e2af24c01bb5d73d48f6d81348f06.jpg',
        info_labels={"originaltitle":"Die Hard 4","genre":"crime,british", "plot":"John McClane and a young hacker join forces to take down master cyber-terrorist Thomas Gabriel in Washington D.C", "mpaa":"18"})
												
    Add_Dir(name='Johnny English', url='http://greeksattv.co.uk/Mario/Johnny.English.2003.720p.BrRip.264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://static.rogerebert.com/uploads/movie/movie_poster/johnny-english-2003/large_oSsisFLSeRJJaTX5l13jMqDKpwH.jpg',
        fanart='http://static.rogerebert.com/uploads/movie/movie_poster/johnny-english-2003/large_oSsisFLSeRJJaTX5l13jMqDKpwH.jpg',
        info_labels={"originaltitle":"Johnny English","genre":"crime,british", "plot":"After a sudden attack on the MI5, Johnny English, Britain's most confident yet unintelligent spy, becomes Britain's only spy", "mpaa":"18"})
												
    Add_Dir(name='Johnny English Reborn', url='http://greeksattv.co.uk/Mario/Johnny.English.Reborn.2011.720p.BrRip.x264.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://fanart.tv/fanart/movies/58233/movieposter/johnny-english-reborn-54a3f281940d6.jpg',
        fanart='https://fanart.tv/fanart/movies/58233/movieposter/johnny-english-reborn-54a3f281940d6.jpg',
        info_labels={"originaltitle":"Johnny English Reborn","genre":"crime,british", "plot":"Johnny English goes up against international assassins hunting down the Chinese premier", "mpaa":"18"})
												
    Add_Dir(name='The Inbetweeners', url='http://greeksattv.co.uk/Mario/The.Inbetweeners.Movie.2011.EXTENDED.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://is4.mzstatic.com/image/thumb/Video69/v4/07/46/29/07462946-66e6-3e27-d2a1-e3f39ecc283c/source/1200x630bb.jpg',
        fanart='http://is4.mzstatic.com/image/thumb/Video69/v4/07/46/29/07462946-66e6-3e27-d2a1-e3f39ecc283c/source/1200x630bb.jpg',
        info_labels={"originaltitle":"The Inbetweeners","genre":"crime,british", "plot":"Four socially troubled 18-year-olds from the south of England go on holiday to Malia", "mpaa":"18"})
												
    Add_Dir(name='The Inbetweeners 2', url='http://greeksattv.co.uk/Mario/The.Inbetweeners.2.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/cd/40/9c/cd409c14eca887e987227a8f27109d1e.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/cd/40/9c/cd409c14eca887e987227a8f27109d1e.jpg',
        info_labels={"originaltitle":"The Inbetweeners 2","genre":"crime,british", "plot":"Jay, Neil, Simon, and Will reunite in Australia for a holiday", "mpaa":"18"})
												
    Add_Dir(name='Wrong Turn', url='http://greeksattv.co.uk/Mario/Wrong.Turn.UNRATED.2003.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/8/85/Wrong_Turn_movie.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/8/85/Wrong_Turn_movie.jpg',
        info_labels={"originaltitle":"Wrong Turn","genre":"crime,british", "plot":"Six people find themselves trapped in the woods of West Virginia, hunted down by cannibalistic mountain men grossly disfigured through generations of in-breeding", "mpaa":"18"})
												
    Add_Dir(name='Wrong Turn 2', url='http://greeksattv.co.uk/Mario/Wrong.Turn.2.Dead.End.UNRATED.2007.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/4c/f8/2c/4cf82c5eefe3f872d11b78042dc91cba.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/4c/f8/2c/4cf82c5eefe3f872d11b78042dc91cba.jpg',
        info_labels={"originaltitle":"Wrong Turn 2","genre":"crime,british", "plot":"A group of reality show contestants find themselves fighting for their survival against a family of hideously deformed inbred cannibals who plan to ruthlessly butcher them all", "mpaa":"18"})
												
    Add_Dir(name='Wrong Turn 3', url='http://greeksattv.co.uk/Mario/Wrong.Turn.3.Left.For.Dead.UNRATED.2009.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/6f/08/ce/6f08ce0e6f801a97e9aeaa52ea16294b--scary-movies-good-movies.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/6f/08/ce/6f08ce0e6f801a97e9aeaa52ea16294b--scary-movies-good-movies.jpg',
        info_labels={"originaltitle":"Wrong Turn 3","genre":"crime,british", "plot":"When their transfer bus crashes in a West Virginia forest, a group of convicts and a corrections officer meet a rafter who is on the run from cannibalistic hillbillies who have murdered her friends", "mpaa":"18"})
												
    Add_Dir(name='Wrong Turn 4', url='http://greeksattv.co.uk/Mario/Wrong.Turn.4.Bloody.Beginnings.UNRATED.2011.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.heyuguys.com/images/2011/08/Wrong-Turn-4.jpg',
        fanart='http://www.heyuguys.com/images/2011/08/Wrong-Turn-4.jpg',
        info_labels={"originaltitle":"Wrong Turn 4","genre":"crime,british", "plot":"A group of college students gets lost in a storm during their snowmobiling trip and takes shelter in an abandoned sanitarium which, unbeknown to them, is home to three deformed cannibals", "mpaa":"18"})
														
    Add_Dir(name='Wrong Turn 5', url='http://greeksattv.co.uk/Mario/Wrong.Turn.5.UNRATED.2012.720p.BRrip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/fc/43/6d/fc436d00310adf7a3a05f292e475a5ea.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/fc/43/6d/fc436d00310adf7a3a05f292e475a5ea.jpg',
        info_labels={"originaltitle":"Wrong Turn 5","genre":"crime,british", "plot":"A group of college students, on a trip to the Mountain Man Festival on Halloween in West Virginia, encounter a clan of cannibals", "mpaa":"18"})
														
    Add_Dir(name='Wrong Turn 6', url='http://greeksattv.co.uk/Mario/Wrong.Turn.6.Last.Resort.2014.DVDRip.XviD-EVO.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/wrong-turn-6-last-resort.32412.jpg',
        fanart='https://i.jeded.com/i/wrong-turn-6-last-resort.32412.jpg',
        info_labels={"originaltitle":"Wrong Turn 6","genre":"crime,british", "plot":"An inheritance leads a young man and his friends to an abandoned resort inhabited by two sketchy caretakers and a clan of mutant cannibals", "mpaa":"18"})
														
    Add_Dir(name='Texas Chainsaw Massacre 2003', url='http://greeksattv.co.uk/Mario/The.Texas.Chainsaw.Massacre.2003.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/8f/20/44/8f2044b7cc87b82401b071504db7b2d6--film-horror-horror-movies.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/8f/20/44/8f2044b7cc87b82401b071504db7b2d6--film-horror-horror-movies.jpg',
        info_labels={"originaltitle":"Texas Chainsaw Massacre 2003","genre":"crime,british", "plot":"After picking up a traumatized young hitchhiker, five friends find themselves stalked and hunted by a deformed chainsaw-wielding killer and his family of equally psychopathic killers", "mpaa":"18"})
														
    Add_Dir(name='Texas Chainsaw Massacre The Beginning', url='http://greeksattv.co.uk/Mario/The.Texas.Chainsaw.Massacre.The.Beginning.2006.1080p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.michalak.org/fh/tcm/tcm_beginning_pstr.jpg',
        fanart='http://www.michalak.org/fh/tcm/tcm_beginning_pstr.jpg',
        info_labels={"originaltitle":"Texas Chainsaw Massacre The Beginning","genre":"crime,british", "plot":"Before being sent to serve in Vietnam, two brothers and their girlfriends take one last road trip, but when they get into an accident, a terrifying experience will take them to a secluded house of horrors, with a chainsaw-wielding killer", "mpaa":"18"})
														
    Add_Dir(name='Texas Chainsaw 2013', url='http://greeksattv.co.uk/Mario/Texas.Chainsaw.2013.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://fanart.tv/fanart/movies/76617/movieposter/texas-chainsaw-3d-5240b66d0cbd7.jpg',
        fanart='https://fanart.tv/fanart/movies/76617/movieposter/texas-chainsaw-3d-5240b66d0cbd7.jpg',
        info_labels={"originaltitle":"Texas Chainsaw","genre":"crime,british", "plot":"A young woman travels to Texas to collect an inheritance; little does she know that an encounter with a chainsaw-wielding killer is part of the reward", "mpaa":"18"})
														
    Add_Dir(name='Super Mario Bros', url='http://greeksattv.co.uk/Mario/Super.Mario.Bros..1993.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.ohhaitrebor.com/wp-content/uploads/2015/07/super-mario-bros-movie-poster.jpg',
        fanart='http://www.ohhaitrebor.com/wp-content/uploads/2015/07/super-mario-bros-movie-poster.jpg',
        info_labels={"originaltitle":"Super Mario Bros","genre":"crime,british", "plot":"Two Brooklyn plumbers, Mario and Luigi, must travel to another dimension to rescue a princess from the evil dictator King Koopa and stop him from taking over the world", "mpaa":"18"})
														
    Add_Dir(name='Final Destination', url='http://greeksattv.co.uk/Mario/4.%20The%20Final%20Destination%20BRRip.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://horrordaily.files.wordpress.com/2011/07/final-destination-2000.jpg',
        fanart='https://horrordaily.files.wordpress.com/2011/07/final-destination-2000.jpg',
        info_labels={"originaltitle":"Final Destination","genre":"crime,british", "plot":"After a teenager has a terrifying vision of him and his friends dying in a plane crash, he prevents the accident only to have Death hunt them down, one by one", "mpaa":"18"})
														
    Add_Dir(name='Final Destination 2', url='http://greeksattv.co.uk/Mario/Final.Destination.2.2003.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://image.tmdb.org/t/p/original/pWY6Cjr11Wv2zzxrhnKB86AZKHI.jpg',
        fanart='https://image.tmdb.org/t/p/original/pWY6Cjr11Wv2zzxrhnKB86AZKHI.jpg',
        info_labels={"originaltitle":"Final Destination 2","genre":"crime,british", "plot":"When Kimberly has a violent premonition of a highway pileup she blocks the freeway, keeping a few others meant to die, safe...Or are they? The survivors mysteriously start dying and it's up to Kimberly to stop it before she's next", "mpaa":"18"})
																
    Add_Dir(name='Final Destination 3', url='http://greeksattv.co.uk/Mario/Final.Destination.3.2006.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/38/cb/a9/38cba959ef0a31bcc767ab09e5a3aded.png',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/38/cb/a9/38cba959ef0a31bcc767ab09e5a3aded.png',
        info_labels={"originaltitle":"Final Destination 3","genre":"crime,british", "plot":"A student's premonition of a deadly rollercoaster ride saves her life and a lucky few, but not from Death itself, which seeks out those who escaped their fate", "mpaa":"18"})
																
    Add_Dir(name='Final Destination 4', url='http://greeksattv.co.uk/Mario/The.Final.Destination.2009.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/61veHBe-s5L.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/61veHBe-s5L.jpg',
        info_labels={"originaltitle":"Final Destination 4","genre":"crime,british", "plot":"After a young man's premonition of a deadly race-car crash helps saves the lives of his peers, Death sets out to collect those who evaded their end.", "mpaa":"18"})
																
    Add_Dir(name='Final Destination 5', url='http://greeksattv.co.uk/Mario/Final.Destination.5%20.2011.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn1-www.comingsoon.net/assets/uploads/2011/06/file_79138_0_finaldestination5poster.jpg',
        fanart='http://cdn1-www.comingsoon.net/assets/uploads/2011/06/file_79138_0_finaldestination5poster.jpg',
        info_labels={"originaltitle":"Final Destination 5","genre":"crime,british", "plot":"Survivors of a suspension-bridge collapse learn there's no way you can cheat Death", "mpaa":"18"})
																
    Add_Dir(name='Scary Movie 1', url='http://greeksattv.co.uk/Mario/Scary.Movie.2000.BrRip.720p.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/2/29/Movie_poster_for_%22Scary_Movie%22.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/2/29/Movie_poster_for_%22Scary_Movie%22.jpg',
        info_labels={"originaltitle":"Scary Movie 1","genre":"crime,british", "plot":"A year after disposing of the body of a man they accidentally killed, a group of dumb teenagers are stalked by a bumbling serial killer", "mpaa":"18"})
																
    Add_Dir(name='Scary Movie 2', url='http://greeksattv.co.uk/Mario/Scary.Movie.2.BrRip.720p.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BMTM5MTY3MDk5OF5BMl5BanBnXkFtZTcwMjc0ODQ4NA@@._V1_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMTM5MTY3MDk5OF5BMl5BanBnXkFtZTcwMjc0ODQ4NA@@._V1_.jpg',
        info_labels={"originaltitle":"Scary Movie 2","genre":"crime,british", "plot":"Four teens are tricked by their professor into visiting a haunted house for a school project", "mpaa":"18"})
																
    Add_Dir(name='Scary Movie 3', url='http://greeksattv.co.uk/Mario/Scary.Movie.3.BrRip.720p.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.impdb.org/images/6/6c/Scary_Movie_3_Poster.jpg',
        fanart='http://www.impdb.org/images/6/6c/Scary_Movie_3_Poster.jpg',
        info_labels={"originaltitle":"Scary Movie 3","genre":"crime,british", "plot":"Cindy must investigate mysterious crop circles and video tapes, and help the President in preventing an alien invasion", "mpaa":"18"})
																
    Add_Dir(name='Scary Movie 4', url='http://greeksattv.co.uk/Mario/Scary.Movie.4.UNRATED.DVDRip.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://secure.netflix.com/us/boxshots/ghd/70044701.jpg',
        fanart='https://secure.netflix.com/us/boxshots/ghd/70044701.jpg',
        info_labels={"originaltitle":"Scary Movie 4","genre":"crime,british", "plot":"Cindy finds out the house she lives in is haunted by a little boy and goes on a quest to find out who killed him and why. Also, Alien Tr-iPods are invading the world and she has to uncover the secret in order to stop them", "mpaa":"18"})
																
    Add_Dir(name='Scary Movie 5', url='http://greeksattv.co.uk/Mario/Scary.MoVie.2013.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://static1.squarespace.com/static/50c3d74fe4b0112a45d6e97b/t/51683a0be4b0f45e71bfc208/1365785100272/scary+movie+5+poster.jpg',
        fanart='https://static1.squarespace.com/static/50c3d74fe4b0112a45d6e97b/t/51683a0be4b0f45e71bfc208/1365785100272/scary+movie+5+poster.jpg',
        info_labels={"originaltitle":"Scary Movie 5","genre":"crime,british", "plot":"A couple begin to experience some unusual activity after bringing their lost nieces and nephew home. With the help of home-surveillance cameras, they learn they're being stalked by a nefarious demon", "mpaa":"18"})
				
    Add_Dir(name='Cabin In The Woods', url='http://greeksattv.co.uk/Mario/The.Cabin.In.The.Woods.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.bigredbarrel.com/blog/wp-content/uploads/2012/09/cabin-in-the-woods-poster.jpg',
        fanart='http://www.bigredbarrel.com/blog/wp-content/uploads/2012/09/cabin-in-the-woods-poster.jpg',
        info_labels={"originaltitle":"Cabin In The Woods","genre":"crime,british", "plot":"Five friends go for a break at a remote cabin, where they get more than they bargained for, discovering the truth behind the cabin in the woods", "mpaa":"18"}) 
				
    Add_Dir(name='The Bunny House', url='http://greeksattv.co.uk/Mario/The.House.Bunny.2008.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://klling.files.wordpress.com/2013/05/the-house-bunny-poster.jpg',
        fanart='https://klling.files.wordpress.com/2013/05/the-house-bunny-poster.jpg',
        info_labels={"originaltitle":"The Bunny House","genre":"crime,british", "plot":"After Playboy bunny Shelley is kicked out of the playboy mansion, she finds a job as the house mother for a sorority full of socially awkward girls", "mpaa":"18"}) 
				
    Add_Dir(name='The Day After Tomorrow', url='http://greeksattv.co.uk/Mario/The.Day.After.Tomarrow.2004.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://meansheets.files.wordpress.com/2011/01/the-day-after-tomorrow-movie-poster.jpg',
        fanart='https://meansheets.files.wordpress.com/2011/01/the-day-after-tomorrow-movie-poster.jpg',
        info_labels={"originaltitle":"The Day After Tomorrow","genre":"crime,british", "plot":"Jack Hall, paleoclimatologist, must make a daring trek across America to reach his son, trapped in the cross-hairs of a sudden international storm which plunges the planet into a new Ice Age", "mpaa":"18"}) 
				
    Add_Dir(name='Hollow Man', url='http://greeksattv.co.uk/Mario/Hollow.Man.2000.DC.720p.BRRip.x264.YIFY.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://img.moviepostershop.com/hollow-man-movie-poster-2000-1020211303.jpg',
        fanart='http://img.moviepostershop.com/hollow-man-movie-poster-2000-1020211303.jpg',
        info_labels={"originaltitle":"Hollow Man","genre":"crime,british", "plot":"Scientists discover how to make people invisible, but their test subject becomes an insane killer who stalks them", "mpaa":"18"}) 
		
    Add_Dir(name='Payback Season', url='http://greeksattv.co.uk/Mario/payback.season-taste.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.mymovies.net/images/film/cin/350x522/fid11542.jpg',
        fanart='http://images.mymovies.net/images/film/cin/350x522/fid11542.jpg',
        info_labels={"originaltitle":"Payback Season","genre":"crime,british", "plot":"Jerome Davies (Adam Deacon) is a successful and wealthy professional football player; When his old friends come back on the scene Jerome's life becomes complicated and dangerous when his old friends Baron (David Ajala) promptly keeps asking Jerome for payouts after Baron looked out for him as a youngster. Baron threatens Jerome and his brother unless Jerome pays Baron large sums of money on a regular basis. Will Jerome have the courage and mentality to confront and put an end to Baron's blackmail?", "mpaa":"18"})
				
    Add_Dir(name='Iron Monkey', url='http://greeksattv.co.uk/Mario/Iron%20Monkey.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.asianmovieweb.com/de/pictures/movie/iron_monkey/fullsize_poster.jpg',
        fanart='http://www.asianmovieweb.com/de/pictures/movie/iron_monkey/fullsize_poster.jpg',
        info_labels={"originaltitle":"Iron Monkey","genre":"crime,british", "plot":"A martial artist/doctor steals from the corrupt authorities as a masked thief to give to the poor while another martial artist/doctor is forced to hunt him down. But a major threat unites them as a powerful and traitorous shaolin monk takes over the authorities", "mpaa":"18"})
				
    Add_Dir(name='Kingsman Secret Service', url='http://greeksattv.co.uk/Mario/Kingsman.The.Secret.Service.2014.720p.BluRay.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/45/df/6a/45df6a4bb96e76827bdaaf2897d77212.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/45/df/6a/45df6a4bb96e76827bdaaf2897d77212.jpg',
        info_labels={"originaltitle":"Kingsman Secret Service","genre":"crime,british", "plot":"A spy organization recruits an unrefined, but promising street kid into the agency's ultra-competitive training program, just as a global threat emerges from a twisted tech genius", "mpaa":"18"})
				
    Add_Dir(name='Saw', url='http://greeksattv.co.uk/Mario/Saw.I.2004.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/5/56/Saw_official_poster.jpg',
        fanart='https://upload.wikimedia.org/wikipedia/en/5/56/Saw_official_poster.jpg',
        info_labels={"originaltitle":"Saw","genre":"crime,british", "plot":"Two strangers awaken in a room with no recollection of how they got there or why, and soon discover they are pawns in a deadly game perpetrated by a notorious serial killer", "mpaa":"18"})
				
    Add_Dir(name='Saw 2', url='http://greeksattv.co.uk/Mario/Saw.II.2005.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.adweek.com/files/adfreak/Saw2a.jpg',
        fanart='http://www.adweek.com/files/adfreak/Saw2a.jpg',
        info_labels={"originaltitle":"Saw 2","genre":"crime,british", "plot":"A detective and his team must rescue 8 people trapped in a factory by the twisted serial killer known as Jigsaw", "mpaa":"18"})
				
    Add_Dir(name='Saw 3', url='http://greeksattv.co.uk/Mario/Saw.III.2006.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images4.fanpop.com/image/photos/21900000/Saw-3-poster-saw-3-21958465-350-500.jpg',
        fanart='http://images4.fanpop.com/image/photos/21900000/Saw-3-poster-saw-3-21958465-350-500.jpg',
        info_labels={"originaltitle":"Saw 3","genre":"crime,british", "plot":"Jigsaw kidnaps a doctor to keep him alive while he watches his new apprentice put an unlucky citizen through a brutal test", "mpaa":"18"})
				
    Add_Dir(name='Saw 4', url='http://greeksattv.co.uk/Mario/Saw.IV.2007.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.adweek.com/files/adfreak/Saw4b.jpg',
        fanart='http://www.adweek.com/files/adfreak/Saw4b.jpg',
        info_labels={"originaltitle":"Saw 4","genre":"crime,british", "plot":"Despite Jigsaw's death, and in order to save the lives of two of his colleagues, Lieutenant Rigg is forced to take part in a new game, which promises to test him to the limit", "mpaa":"18"})
				
    Add_Dir(name='Saw 5', url='http://greeksattv.co.uk/Mario/Saw.V.2008.720p.BrRip.x264.YIFY.mp4.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images4.fanpop.com/image/photos/20900000/Saw-5-Poster-saw-5-20960311-400-565.jpg',
        fanart='http://images4.fanpop.com/image/photos/20900000/Saw-5-Poster-saw-5-20960311-400-565.jpg',
        info_labels={"originaltitle":"Saw 5","genre":"crime,british", "plot":"Following Jigsaw's grisly demise, Mark Hoffman is commended as a hero, but Agent Strahm is suspicious, and delves into Hoffman's past. Meanwhile, another group of people are put through a series of gruesome tests", "mpaa":"18"})
				
    Add_Dir(name='Saw 6', url='http://greeksattv.co.uk/Mario/Saw.VI.2009.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://cdn.movieweb.com/img.teasers.posters/FIg69glkDJ3Rjh_362_a.jpg',
        fanart='http://cdn.movieweb.com/img.teasers.posters/FIg69glkDJ3Rjh_362_a.jpg',
        info_labels={"originaltitle":"Saw 6","genre":"crime,british", "plot":"Agent Strahm is dead, and FBI agent Erickson draws nearer to Hoffman. Meanwhile, a pair of insurance executives find themselves in another game set by Jigsaw", "mpaa":"18"})
				
    Add_Dir(name='Saw 7', url='http://greeksattv.co.uk/Mario/Saw.VII.2010.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images4.fanpop.com/image/photos/21100000/Saw-VII-saw-3d-21148802-718-1111.jpg',
        fanart='http://images4.fanpop.com/image/photos/21100000/Saw-VII-saw-3d-21148802-718-1111.jpg',
        info_labels={"originaltitle":"Saw 7","genre":"crime,british", "plot":"As a deadly battle rages over Jigsaw's brutal legacy, a group of Jigsaw survivors gathers to seek the support of self-help guru and fellow survivor Bobby Dagen, a man whose own dark secrets unleash a new wave of terror", "mpaa":"18"})
				
    Add_Dir(name='Police Academy', url='http://greeksattv.co.uk/Mario/Police.Academy.1984.720p.BrRip.x264.YIFY.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/8d/8dd291cbea8f231982db0fb1716dfc55_500x735.jpg',
        fanart='https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/8d/8dd291cbea8f231982db0fb1716dfc55_500x735.jpg',
        info_labels={"originaltitle":"Police Academy","genre":"crime,british", "plot":"A group of good-hearted but incompetent misfits enter the police academy, but the instructors there are not going to put up with their pranks", "mpaa":"18"})
				
    Add_Dir(name='Police Academy Their First Assignment', url='http://greeksattv.co.uk/Mario/Police.Academy.2.Their.First.Assignment.1985.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/01/f9/bc/01f9bcc195432ec88fc5408e204ca3de.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/01/f9/bc/01f9bcc195432ec88fc5408e204ca3de.jpg',
        info_labels={"originaltitle":"Police Academy Their First Assignment","genre":"crime,british", "plot":"When a new gang moves into town it's up to the screwball police team to stop them", "mpaa":"18"})
				
    Add_Dir(name='Police Academy Back In Training', url='http://greeksattv.co.uk/Mario/Police.Academy.3.Back.In.Training.1986.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/715u1j8QRlL._SL1111_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/715u1j8QRlL._SL1111_.jpg',
        info_labels={"originaltitle":"Police Academy Back In Training","genre":"crime,british", "plot":"The alumni of Commandant Lassard's Police Academy (1984) return to the school to train new recruits and prevent its closure", "mpaa":"18"})
				
    Add_Dir(name='Police Academy Citizens On Patrol', url='http://greeksattv.co.uk/Mario/Police.Academy.4.Citizens.On.Patrol.1987.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/f8/ec/d8/f8ecd84c8b0a49836e54784fd9f50546.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/f8/ec/d8/f8ecd84c8b0a49836e54784fd9f50546.jpg',
        info_labels={"originaltitle":"Police Academy Citizens On Patrol","genre":"crime,british", "plot":"The misfit Police Academy (1984) graduates now are assigned to train a group of civilian volunteers to fight crime once again plaguing the streets", "mpaa":"18"})
				
    Add_Dir(name='Police Academy Assignment Miami Beach', url='http://greeksattv.co.uk/Mario/Police.Academy.5.Assignment.Miami.Beach.1988.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/police-academy-5-assignment-miami-beach.10531.jpg',
        fanart='https://i.jeded.com/i/police-academy-5-assignment-miami-beach.10531.jpg',
        info_labels={"originaltitle":"Police Academy Assignment Miami Beach","genre":"crime,british", "plot":"The Police Academy misfits travel to Miami, Florida for their academy's commanding officer, Lassard, to receive a prestigious lifetime award pending his retirement, which takes a turn involving a group of jewel thieves after their stolen loot that Lassard unknowingly has in his possession.", "mpaa":"18"})
						
    Add_Dir(name='Police Academy City Under Siege', url='http://greeksattv.co.uk/Mario/Police.Academy.6.City.Under.Siege.1989.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/2a/2a/67/2a2a674cfc1779cd1d0b1044b169525d--police-academy-comedy-movies.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/2a/2a/67/2a2a674cfc1779cd1d0b1044b169525d--police-academy-comedy-movies.jpg',
        info_labels={"originaltitle":"Police Academy City Under Siege","genre":"crime,british", "plot":"Those bumbling cadets take to the streets when three inept goons successfully orchestrate a metropolitan crime wave", "mpaa":"18"})
						
    Add_Dir(name='Police Academy Mission To Moscow', url='http://greeksattv.co.uk/Mario/Police.Academy.Mission.To.Moscow.1994.720p.BluRay.x264-%5BYTS.AG%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://3.bp.blogspot.com/-dEGcGqyU3HQ/VQWWucc0XxI/AAAAAAAATq8/1pHdxPi6les/s1600/968full-police-academy-7%2B-mission-to-moscow-poster.jpg',
        fanart='http://3.bp.blogspot.com/-dEGcGqyU3HQ/VQWWucc0XxI/AAAAAAAATq8/1pHdxPi6les/s1600/968full-police-academy-7%2B-mission-to-moscow-poster.jpg',
        info_labels={"originaltitle":"Police Academy Mission To Moscow","genre":"crime,british", "plot":"The Russian government hires the veterans of the Police Academy to help deal with the Mafia", "mpaa":"18"})
#-----------------------------
@route(mode="video_exam")
def Video_Exam():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='The Walking Dead Season 7 Episode 1', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E01.HDTV.x264-KILLERS%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"01", "genre":"Kids", "plot":"Having been brutally overpowered by Negan and his Saviors, Rick and the group kneel helplessly as they suffer heavy losses that will haunt them forever", "mpaa":"U"})

    Add_Dir(name='The Walking Dead Season 7 Episode 2', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E02.WEB-DL.x264-FUM%5Bettv%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"02", "genre":"Kids", "plot":"Carol and Morgan are brought to a community called the Kingdom, led by the eccentric King Ezekiel", "mpaa":"U"})   

    Add_Dir(name='The Walking Dead Season 7 Episode 3', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E03.WEB-DL.x264-RARBG.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"03", "genre":"Kids", "plot":"Daryl is taken by Negan to the Sanctuary, home of the Saviors. Meanwhile, Dwight is sent on a mission to bring back a runaway member of his group", "mpaa":"U"}) 

    Add_Dir(name='The Walking Dead Season 7 Episode 4', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E04.720p.HDTV.x265.ShAaNiG.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"04", "genre":"Kids", "plot":"Still mourning from the recent tragic losses, Rick and the people of Alexandria receive a sobering visit from Negan and his Saviors", "mpaa":"U"}) 

    Add_Dir(name='The Walking Dead Season 7 Episode 5', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E05.INTERNAL.HDTV.x264-FUM%5Bettv%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"05", "genre":"Kids", "plot":"Maggie and Sasha recover from their grief at the Hilltop.", "mpaa":"U"})

    Add_Dir(name='The Walking Dead Season 7 Episode 6', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E06.HDTV.x264-DEFiNE%5BPRiME%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"06", "genre":"Kids", "plot":"Tara encounters a group of female survivors living near the coast after being separated from Heath during their two-week supply run", "mpaa":"U"}) 

    Add_Dir(name='The Walking Dead Season 7 Episode 7', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E07.HDTV.x264-FLEET%5BPRiME%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"07", "genre":"Kids", "plot":"As Eugene and Rosita head to the bullet factory, Rick and Aaron search for supplies for Negan. Meanwhile, Carl and Jesus find themselves on their way to the Sanctuary", "mpaa":"U"})

    Add_Dir(name='The Walking Dead Season 7 Episode 8', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E08.720p.x264-MvGee.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"08", "genre":"Kids", "plot":"Negan's unwelcome visit to Alexandria continues as other members scavenge for supplies; things quickly spin out of control", "mpaa":"U"}) 

    Add_Dir(name='The Walking Dead Season 7 Episode 9', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E09.HDTV.x264-FUM%5Bettv%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"09", "genre":"Kids", "plot":"Jesus leads Rick and the group to the Kingdom, to convince King Ezekiel in joining Alexandria and the Hilltop in the incoming fight against Negan", "mpaa":"U"}) 

    Add_Dir(name='The Walking Dead Season 7 Episode 10', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E10.HDTV.x264-SVA%5BPRiME%5D.mk', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"10", "genre":"Kids", "plot":"While searching for Father Gabriel, the group comes across a mysterious a new collective of survivors. Back at the Kingdom, Carol and Daryl have an emotional reunion", "mpaa":"U"}) 

    Add_Dir(name='The Walking Dead Season 7 Episode 11', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E11.WEB-DL.x264-FUM%5Bettv%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"11", "genre":"Kids", "plot":"Eugene unwillingly begins to work for Negan and the Saviors at the Sanctuary. Meanwhile, Dwight pays a visit to a place from his past", "mpaa":"U"}) 

    Add_Dir(name='The Walking Dead Season 7 Episode 12', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E12.INTERNAL.HDTV.x264-FUM%5Bettv%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"12", "genre":"Kids", "plot":"The group scavenge for supplies. Back in Alexandria, Tara must make a morally challenging decision", "mpaa":"U"}) 

    Add_Dir(name='The Walking Dead Season 7 Episode 13', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E13.WEB-DL.x264-FUM%5Bettv%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"13", "genre":"Kids", "plot":"Things don't go as planned, when a group of Kingdommers delivers goods to the Saviors during a routine supply drop-off", "mpaa":"U"}) 

    Add_Dir(name='The Walking Dead Season 7 Episode 14', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E14.WEB-DL.x264-FUM%5Bettv%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"14", "genre":"Kids", "plot":"The Saviors visit the Hilltop unexpectedly, surprising everyone, with plans of taking more than supplies", "mpaa":"U"}) 

    Add_Dir(name='The Walking Dead Season 7 Episode 15', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E15.WEB-DL.x264-FUM%5Bettv%5D.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"15", "genre":"Kids", "plot":"A group of Alexandrians embark on a journey; One member of the group must make a heartbreaking decision", "mpaa":"U"}) 

    Add_Dir(name='The Walking Dead Season 7 Episode 16', url='http://greeksattv.co.uk/Mario/Walking%20Dead/Walking%20Dead%20Season%207/The.Walking.Dead.S07E16.HDTV.x264-KILLERS%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.scifibloggers.com/wp-content/uploads/the-walking-dead-season-7-negan-morgan-key-art-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"07", "episode":"16", "genre":"Kids", "plot":"The stakes continue to grow higher as paths cross; The group enacts an intricate plan as the saviors arrive in Alexandria", "mpaa":"U"}) 		
#-----------------------------
@route(mode="video_ex")
def Video_Ex():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='Fear The Walking Dead Season 3 Episode 1', url='http://greeksattv.co.uk/Mario/Walking%20Dead/FearTheWalkingDeadSeason3/Fear.the.Walking.Dead.S03E01.HDTV.x264-SVA%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.amcnetworks.com/amc.com/wp-content/uploads/2017/04/fear-the-walking-dead-season-3-key-art-nick-dillane-400x600.jpg',
        fanart='http://1.bp.blogspot.com/-RiPNTkEF1C8/VXXF11LEr_I/AAAAAAABsH8/Ukysec9xDuA/s1600/ftwd-header.jpg',
        info_labels={"season":"03", "episode":"01", "genre":"Kids", "plot":"The Clark family find themselves in a dire predicament and must work together to discover a path to safety", "mpaa":"U"})
		
    Add_Dir(name='Fear The Walking Dead Season 3 Episode 2', url='http://greeksattv.co.uk/Mario/Walking%20Dead/FearTheWalkingDeadSeason3/Fear.the.Walking.Dead.S03E02.HDTV.x264-SVA%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.amcnetworks.com/amc.com/wp-content/uploads/2017/04/fear-the-walking-dead-season-3-key-art-nick-dillane-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"03", "episode":"02", "genre":"Kids", "plot":"Strand faces resistance as he attempts to hold power over his domain", "mpaa":"U"})
				
    Add_Dir(name='Fear The Walking Dead Season 3 Episode 3', url='http://greeksattv.co.uk/Mario/Walking%20Dead/FearTheWalkingDeadSeason3/Fear.the.Walking.Dead.S03E03.HDTV.x264-SVA%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.amcnetworks.com/amc.com/wp-content/uploads/2017/04/fear-the-walking-dead-season-3-key-art-nick-dillane-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"03", "episode":"03", "genre":"Kids", "plot":"Alicia and Nick fall in with new crowds. Madison discovers Otto's past mimics her own", "mpaa":"U"})
				
    Add_Dir(name='Fear The Walking Dead Season 3 Episode 4', url='http://greeksattv.co.uk/Mario/Walking%20Dead/FearTheWalkingDeadSeason3/Fear.the.Walking.Dead.S03E04.HDTV.x264-SVA%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.amcnetworks.com/amc.com/wp-content/uploads/2017/04/fear-the-walking-dead-season-3-key-art-nick-dillane-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"03", "episode":"04", "genre":"Kids", "plot":"A mysterious character searches for purpose and becomes tied to the struggle over a resource. ", "mpaa":"U"})
				
    Add_Dir(name='Fear The Walking Dead Season 3 Episode 5', url='http://greeksattv.co.uk/Mario/Walking%20Dead/FearTheWalkingDeadSeason3/Fear.the.Walking.Dead.S03E05.HDTV.x264-SVA%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.amcnetworks.com/amc.com/wp-content/uploads/2017/04/fear-the-walking-dead-season-3-key-art-nick-dillane-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"03", "episode":"05", "genre":"Kids", "plot":"An oncoming threat disrupts peace; Madison and Troy search for answers; Alicia must reconcile with her past", "mpaa":"U"})
				
    Add_Dir(name='Fear The Walking Dead Season 3 Episode 6', url='http://greeksattv.co.uk/Mario/Walking%20Dead/FearTheWalkingDeadSeason3/Fear.the.Walking.Dead.S03E06.HDTV.x264-SVA%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.amcnetworks.com/amc.com/wp-content/uploads/2017/04/fear-the-walking-dead-season-3-key-art-nick-dillane-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"03", "episode":"06", "genre":"Kids", "plot":"News of danger spreads throughout the community as Madison struggles to keep everyone together", "mpaa":"U"})
				
    Add_Dir(name='Fear The Walking Dead Season 3 Episode 7', url='http://greeksattv.co.uk/Mario/Walking%20Dead/FearTheWalkingDeadSeason3/Fear.the.Walking.Dead.S03E07.PROPER.HDTV.x264-KILLERS%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.amcnetworks.com/amc.com/wp-content/uploads/2017/04/fear-the-walking-dead-season-3-key-art-nick-dillane-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"03", "episode":"07", "genre":"Kids", "plot":"A new arrival sows a divide within the ranch and Alicia forms a relationship to maintain peace", "mpaa":"U"})
				
    Add_Dir(name='Fear The Walking Dead Season 3 Episode 8', url='http://greeksattv.co.uk/Mario/Walking%20Dead/FearTheWalkingDeadSeason3/Fear.the.Walking.Dead.S03E08.HDTV.x264-SVA%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.amcnetworks.com/amc.com/wp-content/uploads/2017/04/fear-the-walking-dead-season-3-key-art-nick-dillane-400x600.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"season":"03", "episode":"08", "genre":"Kids", "plot":"Madison must negotiate the terms of an agreement in the midst of ranch-wide turmoil; Nick and Alicia challenge their mother's motives", "mpaa":"U"})
#-----------------------------
@route(mode="video_e")
def Video_E():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='Game Of Thrones Season 7 Episode 1', url='http://greeksattv.co.uk/Mario/Walking%20Dead/GameOfThronesS7/game.of.thrones.s07e01.web.h264-tbs%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/10/3f/30/103f3043108706357715dca2af460cdc.jpg',
        fanart='http://2.bp.blogspot.com/-udP8Z8fK0ic/UM5O50vJ7RI/AAAAAAACKG8/MAqX3KunEF8/s1600/game_of_thrones_poster70.jpg',
        info_labels={"season":"07", "episode":"01", "genre":"Kids", "plot":"Jon organizes the defense of the North. Cersei tries to even the odds. Sam adapts to his new life in Oldtown. Daenerys comes home. Night King makes his way south. Arya reminds the Freys the North remembers", "mpaa":"U"})
										
    Add_Dir(name='Game Of Thrones Season 7 Episode 2', url='http://greeksattv.co.uk/Mario/Walking%20Dead/GameOfThronesS7/Game.of.Thrones.S07E02.HDTV.x264-SVA%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/10/3f/30/103f3043108706357715dca2af460cdc.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/10/3f/30/103f3043108706357715dca2af460cdc.jpg',
        info_labels={"season":"07", "episode":"01", "genre":"Kids", "plot":"Daenerys receives an unexpected visitor. Jon faces a revolt. Tyrion plans the conquest of Westeros", "mpaa":"U"})
#-----------------------------
@route(mode="video_live")
def Video_Live():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='BBC One', url='http://vs-hls-uk-live.akamaized.net/pool_30/live/bbc_one_hd/bbc_one_hd.isml/bbc_one_hd-pa4%3d128000-video%3d5070016.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://ichef.bbci.co.uk/images/ic/480x270/p02lrnkz.jpg',
        fanart='https://fanart.tv/fanart/tv/72514/showbackground/looney-tunes-521f73c2c3165.jpg',
        info_labels={"season":"03", "episode":"21", "genre":"Kids", "plot":"Get your cares away, worries for another day...", "mpaa":"U"})
								
    Add_Dir(name='BBC Two', url='http://a.files.bbci.co.uk/media/live/manifesto/audio_video/simulcast/hls/uk/abr_hdtv/llnw/bbc_two_hd.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://orig07.deviantart.net/126d/f/2016/100/c/0/bbc2_by_jok3rb0ytothereturn-d9ygruf.png',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='BBC Four', url='http://vs-hls-uk-live.akamaized.net/pool_33/live/bbc_four_hd/bbc_four_hd.isml/bbc_four_hd-pa4%3d128000-video%3d5070016.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://pbs.twimg.com/profile_images/816968331823644672/xkhhrXT0.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='ITV', url='http://itv1liveios-i.akamaihd.net/hls/live/203437/itvlive/ITV1MN/master_Main1800.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://static.wixstatic.com/media/d44f29_83a85c006ff24374bff7782f6c49a32e~mv2.png',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='ITV 2', url='http://itv2liveios-i.akamaihd.net/hls/live/203495/itvlive/ITV2MN/master_Main1800.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://static.wixstatic.com/media/d44f29_83a85c006ff24374bff7782f6c49a32e~mv2.png',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='ITV 3', url='http://itv3liveios-i.akamaihd.net/hls/live/207262/itvlive/ITV3MN/master_Main1800.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://simtdesign.files.wordpress.com/2013/03/new-itv-3-logo.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='ITV 4', url='http://itv4liveios-i.akamaihd.net/hls/live/207266/itvlive/ITV4MN/master_Main1800.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.tvlive.org.uk/media/resources/itv4.png',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='BT Sports ESPN', url='http://185.142.239.164:3135/BT/Espn/index.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://sport.bt.com/s/assets/ucl/images/btsportespn.png',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='BT Sports 2', url='http://iptv.ndasat.com:88/live/safin/**WhZR5qA/10.ts', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://www.thelogodb.com/images/media/logo/vsuvvu1433963716.png',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
												
    Add_Dir(name='Fox Sports 1', url='http://185.142.239.164:3135/1/FOX/index.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://bangshift.com/wp-content/uploads/2015/07/fox.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
												
    Add_Dir(name='Fox Sports 2', url='http://185.142.239.164:3135/2/FOX/index.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://www.montagecabletv.com/sites/default/files/Fox_Sports_2.png',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Rik Sat', url='http://player.webvideocore.net/CL1olYogIrDWvwqiIKK7eLBkzvO18gwo9ERMzsyXzwt_t-ya8ygf2kQBZww38JJT/eq473601t9w8.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.ytimg.com/vi/EJeB0Mab-nM/hqdefault.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																
    Add_Dir(name='Alpha CY', url='http://l4.cloudskep.com/alphacy/acy/playlist.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.newsbomb.com.cy/media/com_news/story/2016/01/28/640475/main/alpha-cyprus.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																
    Add_Dir(name='Alpha TV', url='http://193.92.37.235:1935/LiveEdgeTV/live@720/chunklist_w298877283.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://yt3.ggpht.com/-5GZmPEO20oM/AAAAAAAAAAI/AAAAAAAAAAA/3_p0lQRCPQY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																
    Add_Dir(name='Sigma CY', url='http://81.21.47.74/hls/live.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://assets.nav.mtn.com.cy/mtntv/sigma-3d-jpg-BJYufGFyb.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																
    Add_Dir(name='ANT 1', url='http://antglantennatv-lh.akamaihd.net/i/live_1@421307/master.m3u8', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://www.livetvswatch.com/uploads/ant1-tv-live-from-greece-1442907362.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
#-----------------------------	
@route(mode="video_grand")
def Video_Grand():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='The Grand Tour S01E01', url='http://greeksattv.co.uk/Mario/GrandTour/The.Grand.Tour.S01E01.WEBRip.X264-DEFLATE%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='https://www.applausestore.com/images/showlarge/TheGrandTourLarge2017.jpg',
        info_labels={"season":"03", "episode":"21", "genre":"Kids", "plot":"Get your cares away, worries for another day...", "mpaa":"U"})
																		
    Add_Dir(name='The Grand Tour S01E02', url='http://greeksattv.co.uk/Mario/GrandTour/The%20Grand%20Tour%20S01E02%20HDTV%20x264-RMTeam.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='The Grand Tour S01E03', url='http://greeksattv.co.uk/Mario/GrandTour/The.Grand.Tour.S01E03.WEBRip.X264-DEFLATE%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='The Grand Tour S01E04', url='http://greeksattv.co.uk/Mario/GrandTour/The.grand.tour.s01e04.720p.webrip.x264-NBY-%5Bmoviezplanet.in%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='The Grand Tour S01E05', url='http://greeksattv.co.uk/Mario/GrandTour/The.Grand.Tour.S01E05.WEBRip.X264-DEFLATE%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='The Grand Tour S01E06', url='http://greeksattv.co.uk/Mario/GrandTour/The.Grand.Tour.S01E06.720p.WEBRip.470MB.MkvCage.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='The Grand Tour S01E07', url='http://greeksattv.co.uk/Mario/GrandTour/The.Grand.Tour.S01E07.720p.WEBRip.370MB.MkvCage.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='The Grand Tour S01E08', url='http://greeksattv.co.uk/Mario/GrandTour/The.Grand.Tour.S01E08.WEBRip.X264-DEFLATE%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='The Grand Tour S01E09', url='http://greeksattv.co.uk/Mario/GrandTour/The.Grand.Tour.S01E09.WEBRip.X264-DEFLATE%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='The Grand Tour S01E10', url='http://greeksattv.co.uk/Mario/GrandTour/The.Grand.Tour.S01E10.WEBRip.X264-DEFLATE%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='The Grand Tour S01E11', url='http://greeksattv.co.uk/Mario/GrandTour/The.Grand.Tour.S01E11.WEBRip.X264-DEFLATE%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='The Grand Tour S01E12', url='http://greeksattv.co.uk/Mario/GrandTour/The.Grand.Tour.S01E12.WEBRip.X264-DEFLATE%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='The Grand Tour S01E13', url='http://greeksattv.co.uk/Mario/GrandTour/The.Grand.Tour.S01E13.WEBRip.X264-DEFLATE%5Bettv%5D.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/the-grand-tour-first-season.59873.jpg',
        fanart='http://www.radicalscene.com/wp-content/uploads/2017/02/The_Walking_Dead_title_card-1.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
#-----------------------------	
@route(mode="video_gear")
def Video_Gear():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='Top Gear Polar Special', url='http://greeksattv.co.uk/Mario/TopGear/Top.Gear.Polar.Special.HDTV.XviD-BiA.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://1.bp.blogspot.com/_DjocL3t0xUk/TVMFtbhiBiI/AAAAAAAAAKk/O9bLkfkoRTI/s1600/Top_Gear_Polar_Special_Season5_Custom-%255Bcdcovers_cc%255D-front.jpg',
        fanart='https://wallpaperscraft.com/image/top_gear_richard_khammond_dzheremi_klarkson_dzhejms_mej_103664_1920x1080.jpg',
        info_labels={"season":"03", "episode":"21", "genre":"Kids", "plot":"Get your cares away, worries for another day...", "mpaa":"U"})
								
    Add_Dir(name='Top Gear Botswana Special', url='http://greeksattv.co.uk/Mario/TopGear/Top%20Gear%20Botswana%20Special.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/thumb/6/66/TopGearBotswanaSpecial.jpg/250px-TopGearBotswanaSpecial.jpg',
        fanart='https://wallpaperscraft.com/image/top_gear_richard_khammond_dzheremi_klarkson_dzhejms_mej_103664_1920x1080.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Top Gear Middle East Special', url='http://greeksattv.co.uk/Mario/TopGear/Top.Gear.Middle.East.Special.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/top-gear-middle-east-special.61458.jpg',
        fanart='https://wallpaperscraft.com/image/top_gear_richard_khammond_dzheremi_klarkson_dzhejms_mej_103664_1920x1080.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
												
    Add_Dir(name='Top Gear India Special', url='http://greeksattv.co.uk/Mario/TopGear/Top.Gear.India.Special.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://i.jeded.com/i/top-gear-the-india-special.65554.jpg',
        fanart='https://wallpaperscraft.com/image/top_gear_richard_khammond_dzheremi_klarkson_dzhejms_mej_103664_1920x1080.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Top Gear Bolivia Special', url='http://greeksattv.co.uk/Mario/TopGear/Top.Gear.14x06.Bolivia%20Special.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://image.tmdb.org/t/p/w300_and_h450_bestv2/kGlhGwNnHYa2WmvegYosZiw7pKu.jpg',
        fanart='https://wallpaperscraft.com/image/top_gear_richard_khammond_dzheremi_klarkson_dzhejms_mej_103664_1920x1080.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Top Gear Vietnam Special', url='http://greeksattv.co.uk/Mario/TopGear/Top%20Gear%20Vietnam%20Special.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/41ZXKJ6YOnL.jpg',
        fanart='https://wallpaperscraft.com/image/top_gear_richard_khammond_dzheremi_klarkson_dzhejms_mej_103664_1920x1080.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Top Gear Africa Special Part 1', url='http://greeksattv.co.uk/Mario/TopGear/Top.Gear.19x06.HDTV.x264-FoV.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s3.thcdn.com/productimg/0/960/960/75/10784575-1366909285-905372.jpg',
        fanart='https://wallpaperscraft.com/image/top_gear_richard_khammond_dzheremi_klarkson_dzhejms_mej_103664_1920x1080.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Top Gear Africa Special Part 2', url='http://greeksattv.co.uk/Mario/TopGear/Top.Gear.19x07.HDTV.x264-FoV.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s3.thcdn.com/productimg/0/960/960/75/10784575-1366909285-905372.jpg',
        fanart='https://wallpaperscraft.com/image/top_gear_richard_khammond_dzheremi_klarkson_dzhejms_mej_103664_1920x1080.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Top Gear Burma Special', url='http://greeksattv.co.uk/Mario/TopGear/top_gear%20Burma%20Special.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s2.thcdn.com/productimg/0/600/600/59/10906159-1401297640-597818.jpg',
        fanart='https://wallpaperscraft.com/image/top_gear_richard_khammond_dzheremi_klarkson_dzhejms_mej_103664_1920x1080.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Top Gear Patagonia Special', url='http://greeksattv.co.uk/Mario/TopGear/Top.Gear.Patagonia.Special.2015.720p.BRRip.1GB.MkvCage.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://upload.wikimedia.org/wikipedia/en/thumb/8/81/Top_Gear_Patagonia_Special_DVD.jpg/250px-Top_Gear_Patagonia_Special_DVD.jpg',
        fanart='https://wallpaperscraft.com/image/top_gear_richard_khammond_dzheremi_klarkson_dzhejms_mej_103664_1920x1080.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
#-----------------------------	
@route(mode="video_may")
def Video_May():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='James May Things You Need To Know About The Human Body', url='http://greeksattv.co.uk/Mario/BBC.2011.James.Mays.Things.You.Need.to.Know.S01E01.About.The.Human.Body.720p_x264_aac.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://datas.series-tv-shows.com/pic/tvdb/42454/poster.jpg',
        fanart='http://image.tmdb.org/t/p/original/3ZcIFOaEJoYnFA1bhiLTspBSmJD.jpg',
        info_labels={"season":"03", "episode":"21", "genre":"Kids", "plot":"Get your cares away, worries for another day...", "mpaa":"U"})
								
    Add_Dir(name='James May Things You Need To Know About The Universe', url='http://greeksattv.co.uk/Mario/BBC.2011.James.Mays.Things.You.Need.to.Know.S01E02.About.The.Universe.720p_x264_aac.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://datas.series-tv-shows.com/pic/tvdb/42454/poster.jpg',
        fanart='http://image.tmdb.org/t/p/original/3ZcIFOaEJoYnFA1bhiLTspBSmJD.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='James May Things You Need To Know About The Weather', url='http://greeksattv.co.uk/Mario/James%20Mays%20Things%20You%20Need%20To%20Know%20about%20the%20weather.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://datas.series-tv-shows.com/pic/tvdb/42454/poster.jpg',
        fanart='http://image.tmdb.org/t/p/original/3ZcIFOaEJoYnFA1bhiLTspBSmJD.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='James May Things You Need To Know About Evolution', url='http://greeksattv.co.uk/Mario/HD%20James%20Mays%20Things%20You%20Need%20To%20Know%20S02E03%20Evolution%20720x480.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://datas.series-tv-shows.com/pic/tvdb/42454/poster.jpg',
        fanart='http://image.tmdb.org/t/p/original/3ZcIFOaEJoYnFA1bhiLTspBSmJD.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='James May Things You Need To Know About Einstein', url='http://greeksattv.co.uk/Mario/James%20Mays%20Things%20You%20Need%20To%20Know%20%20%20Einstein.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://datas.series-tv-shows.com/pic/tvdb/42454/poster.jpg',
        fanart='http://image.tmdb.org/t/p/original/3ZcIFOaEJoYnFA1bhiLTspBSmJD.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																
    Add_Dir(name='James May Things You Need To Know About The Brain', url='http://greeksattv.co.uk/Mario/James%20Mays%20Things%20You%20Need%20To%20Know%20The%20Brain.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://datas.series-tv-shows.com/pic/tvdb/42454/poster.jpg',
        fanart='http://image.tmdb.org/t/p/original/3ZcIFOaEJoYnFA1bhiLTspBSmJD.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																
    Add_Dir(name='James May Things You Need To Know About Engineering', url='http://greeksattv.co.uk/Mario/James%20Mays%20Things%20You%20Need%20To%20Know%20-%20Series%202%20-%20Episode%205%20-%20Engineering%20(S02E05).mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://datas.series-tv-shows.com/pic/tvdb/42454/poster.jpg',
        fanart='http://image.tmdb.org/t/p/original/3ZcIFOaEJoYnFA1bhiLTspBSmJD.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																
    Add_Dir(name='James May Things You Need To Know About Chemistry', url='http://greeksattv.co.uk/Mario/James%20Mays%20Things%20You%20Need%20To%20Know%20About%20Chemistry%20%20%20S02E06.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://datas.series-tv-shows.com/pic/tvdb/42454/poster.jpg',
        fanart='http://image.tmdb.org/t/p/original/3ZcIFOaEJoYnFA1bhiLTspBSmJD.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																		
    Add_Dir(name='James May Things You Need To Know About Speed', url='http://greeksattv.co.uk/Mario/James%20Mays%20Things%20You%20Need%20To%20Know%20%20%20Speed.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://datas.series-tv-shows.com/pic/tvdb/42454/poster.jpg',
        fanart='http://image.tmdb.org/t/p/original/3ZcIFOaEJoYnFA1bhiLTspBSmJD.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
#-----------------------------	
@route(mode="video_peters")
def Video_Peters():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='Russell Peters Green Card Tour 2011', url='http://greeksattv.co.uk/Mario/Russell%20Peters%20Green%20Card%20Tour%5B2011%5DDVDRip%20XviD-ExtraTorrentRG.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://3.bp.blogspot.com/-p3htywzdaJw/TqfYp-uLRYI/AAAAAAAAAo4/VG8GPU84cEs/s1600/Russell+Peters+The+Green+Card+Tour+-+Live+from+The+O2+Arena.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"season":"03", "episode":"21", "genre":"Kids", "plot":"Get your cares away, worries for another day...", "mpaa":"U"})	
																		
    Add_Dir(name='Russell Peters Notorious 2013', url='http://greeksattv.co.uk/Mario/Russell%20Peters%20Notorious%20720p%20WEBRip%20x264-TheRival.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://exclaim.ca/images/Russell_Peters_Notorious.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																		
    Add_Dir(name='Russell Peters Almost Famous 2016', url='http://greeksattv.co.uk/Mario/Russell%20Peters%20-%20Almost%20Famous%202016%20720p%20WEBRip%20x264-TheRival.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://art-2.nflximg.net/6b85d/685fe5a2678ec4d3b6493e87dfc7438c4b96b85d.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
#-----------------------------	
@route(mode="video_brown")
def Video_Brown():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='The Heist', url='http://greeksattv.co.uk/Mario/Derren%20Brown%20-%20The%20Heist.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/15/c4/25/15c425c3ae72f4b2bc1bfe7ae7f403fb.jpg',
        fanart='https://www.royalandderngate.co.uk/wp-content/uploads/2017/04/DerrenBrown_underground-Brochure-Landscape-PR.jpg',
        info_labels={"season":"03", "episode":"21", "genre":"Kids", "plot":"Get your cares away, worries for another day...", "mpaa":"U"})
																				
    Add_Dir(name='Derren Brown The System', url='http://greeksattv.co.uk/Mario/Derren%20Brown%20-%20The%20System%20(FULL).mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/15/c4/25/15c425c3ae72f4b2bc1bfe7ae7f403fb.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																						
    Add_Dir(name='Derren Brown The great Art Robbery', url='http://greeksattv.co.uk/Mario/Derren%20Brown%20the%20great%20art%20robbery.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/15/c4/25/15c425c3ae72f4b2bc1bfe7ae7f403fb.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																						
    Add_Dir(name='Derren Brown The Gathering', url='http://greeksattv.co.uk/Mario/Derren%20Brown%20The%20Gathering%20%20(full%20episode).mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/15/c4/25/15c425c3ae72f4b2bc1bfe7ae7f403fb.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																						
    Add_Dir(name='Derren Brown Evening Of Wonders', url='http://greeksattv.co.uk/Mario/Derren%20Brown%20Evening%20Of%20Wonders.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://contact25.com/uploads/7_602988.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																						
    Add_Dir(name='Derren Brown Something Wicked This Way Comes', url='http://greeksattv.co.uk/Mario/Derren%20Brown%20-%20Something%20Wicked%20This%20Way%20Comes%20(FULL).mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images.bigcartel.com/product_images/162598129/something_wicked12978706854d5bef5d0397c.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																						
    Add_Dir(name='Derren Brown Enigma', url='http://greeksattv.co.uk/Mario/Derren%20Brown%20Enigma.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://ilarge.lisimg.com/image/6109102/1050full-derren-brown%3A-enigma-poster.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																						
    Add_Dir(name='Derren Brown Infamous', url='http://greeksattv.co.uk/Mario/Derren%20Brown%20Infamous.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://derrenbrown.co.uk/wp-content/uploads/2013/01/DB_infamous_blog1.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																						
    Add_Dir(name='Derren Brown The Svengali', url='http://greeksattv.co.uk/Mario/derren.brown.svengali.2012.hdtv.x264-c4tv.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/51OCIK6DU-L.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																						
    Add_Dir(name='Derren Brown Miricale', url='http://greeksattv.co.uk/Mario/Derren.Brown-Miracle.2016.720p.HDTV.x264-DEADPOOL.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://pbs.twimg.com/media/B1GhhAoIIAAbbPG.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																						
    Add_Dir(name='Derren Brown Pushed To The Edge', url='http://greeksattv.co.uk/Mario/Derren%20Brown%20Pushed%20To%20The%20Edge%20HDTV%20x264-TASTETV.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/15/c4/25/15c425c3ae72f4b2bc1bfe7ae7f403fb.jpg',
        fanart='https://i.ytimg.com/vi/3gD1woa_Cbw/maxresdefault.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
#-----------------------------	
@route(mode="video_doc")
def Video_Doc():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='Found The Second Earth National Geographic The Universe Space Discovery', url='http://greeksattv.co.uk/Mario/SpaceDocs/Found%20The%20Second%20Earth%20-%20National%20Geographic%20The%20Universe%20-%20Space%20Discovery%20Documentary%202017.mp4', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"season":"03", "episode":"21", "genre":"Kids", "plot":"Get your cares away, worries for another day...", "mpaa":"U"})	
				
    Add_Dir(name='Aliens On The Moon And Earth', url='http://greeksattv.co.uk/Mario/SpaceDocs/New_Space_Documentary_2016._Aliens_on_the_Moon_and_Earth.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"season":"03", "episode":"21", "genre":"Kids", "plot":"Get your cares away, worries for another day...", "mpaa":"U"})
		
    Add_Dir(name='Edge Of The Solar System', url='http://greeksattv.co.uk/Mario/SpaceDocs/How.the.Universe.Works.Series.4.4of8.Edge.of.the.Solar.System.720p.HDTV.x264.AAC.MVGroup.org.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"season":"03", "episode":"21", "genre":"Kids", "plot":"Get your cares away, worries for another day...", "mpaa":"U"})
		
    Add_Dir(name='Birth Of The Earth', url='http://greeksattv.co.uk/Mario/SpaceDocs/Discovery.Ch.How.the.Universe.Works.Series.2.8of8.Birth.of.the.Earth.PDTV.XviD.AC3.MVGroup.org.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18"})

    Add_Dir(name='BBC Documentary History National Geographic Milky Way Galaxy Universe Documentary', url='http://greeksattv.co.uk/Mario/SpaceDocs/BBC%20Documentary%20History%20%20National%20Geographic%20%20Milky%20Way%20Galaxy%20-%20Universe%20documentary.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"SPACE!!!","genre":"crime,british", "plot":"SPACE!!!", "mpaa":"18"})

    Add_Dir(name='BBC Documentary 2017 Journey to Space New Documentary Adventure', url='http://greeksattv.co.uk/Mario/SpaceDocs/BBC%20Documentary%202017%20-%20%20Journey%20to%20Space%20-%20New%20Documentary%20Adventure.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='The Universe Alien Planets Space Documentary', url='http://greeksattv.co.uk/Mario/SpaceDocs/The%20Universe%20Alien%20Planets%20-%20Space%20Documentary%202017%20HD.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='The Universe New Discoveries In Space', url='http://greeksattv.co.uk/Mario/SpaceDocs/The%20Universe%D7%83%20new%20discoveries%20in%20space%20documentary%20HD%201080p%2060k.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='National Geographic Astrobiology Space Travel', url='http://greeksattv.co.uk/Mario/SpaceDocs/National%20Geographic%20%20Astrobiology%20%20Space%20Travel%20-%20Documentary%202016%20HD%20720p.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Mysteries of SPACE exploration that will FREAK YOU OUT', url='http://greeksattv.co.uk/Mario/SpaceDocs/Mysteries%20of%20SPACE%20exploration%20that%20will%20FREAK%20YOU%20OUT%20-%20Full%20Documentary%202017.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Wonderful Solar System Secrets of Space Documentary National Geography', url='http://greeksattv.co.uk/Mario/SpaceDocs/Wonderful%20Solar%20System%20Secrets%20of%20Space%20Documentary%20National%20Geography%202017.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																										
    Add_Dir(name='The Universe Disasters in Deep Space Full Documentary', url='http://greeksattv.co.uk/Mario/SpaceDocs/The%20Universe%20%20Disasters%20in%20Deep%20Space%20Full%20Documentary%20HD%201080p.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																										
    Add_Dir(name='Explore The Milky Way Galaxy', url='http://greeksattv.co.uk/Mario/SpaceDocs/Explore%20The%20Milky%20Way%20Galaxy%20-%20Documentary%20HD.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																										
    Add_Dir(name='Supermassive funnel of death in space Documentary National Geographic', url='http://greeksattv.co.uk/Mario/SpaceDocs/Supermassive%20funnel%20of%20death%20in%20space%20Documentary%20National%20Geographic%202017%20Hd.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																										
    Add_Dir(name='From The Beginning of Time to The Present Day Documentary', url='http://greeksattv.co.uk/Mario/SpaceDocs/From%20The%20Beginning%20of%20Time%20to%20The%20Present%20Day%20%20%20Documentary%202017%20HD%201080p.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																												
    Add_Dir(name='Finding Life Beyond Earth Documentary', url='http://greeksattv.co.uk/Mario/SpaceDocs/Finding%20Life%20Beyond%20Earth%20Documentary%202017%20HD%20720p.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/f4/b1/74/f4b1747fcfc417817c965f66322e0e61--space-theme-space-space.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='The Beginning Making Star Wars Episode I The Phantom Menace (Full Version)', url='http://greeksattv.co.uk/Mario/StarWarsDocs/The%20Beginning%20Making%20Star%20Wars%20Episode%20I%20The%20Phantom%20Menace%20(Full%20Version).mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://wallaroomedia.com/wp-content/uploads/2015/12/StarWars-Header-mobile.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Star Wars Episode 2 Attack of The Clones (The Making of Documentary)', url='http://greeksattv.co.uk/Mario/StarWarsDocs/Star%20Wars%20Episode%202%20Attack%20of%20The%20Clones%20(The%20Making%20of%20Documentary).mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://wallaroomedia.com/wp-content/uploads/2015/12/StarWars-Header-mobile.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Star Wars Within A Minute The Making Of Episode III Documentary', url='http://greeksattv.co.uk/Mario/StarWarsDocs/Star%20Wars%20Within%20A%20Minute%20The%20Making%20Of%20Episode%20III%20Documentary.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://wallaroomedia.com/wp-content/uploads/2015/12/StarWars-Header-mobile.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Making of Star Wars I-III  (World building  Set Design)', url='http://greeksattv.co.uk/Mario/StarWarsDocs/Making%20of%20Star%20Wars%20I-III%20%20(World%20building%20%20Set%20Design).mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://wallaroomedia.com/wp-content/uploads/2015/12/StarWars-Header-mobile.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Star Wars The Force Within Making Star Wars Episode 7', url='http://greeksattv.co.uk/Mario/StarWarsDocs/Star%20Wars%20The%20Force%20Within.mp4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://wallaroomedia.com/wp-content/uploads/2015/12/StarWars-Header-mobile.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='The Secrets Of Star Wars The Force Awakens', url='http://greeksattv.co.uk/Mario/StarWarsDocs/The.Secrets.of.the.Force.Awakens.720p.BRRip.600MB.MkvCage.mkv', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://wallaroomedia.com/wp-content/uploads/2015/12/StarWars-Header-mobile.jpg',
        fanart='https://whickersworldfoundation.com/wp-content/uploads/2016/03/9711113509_def1dba3bf_k.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
#-----------------------------	
@route(mode="video_mvids")
def Video_Mvids():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='Micheal Jackson Smooth Criminal', url='https://www.youtube.com/watch?v=h_D3VFfhvs4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://img00.deviantart.net/ef95/i/2015/125/b/a/smooth_criminal_by_sherlingtondunnen-d1f6f7s.jpg',
        fanart='http://img00.deviantart.net/ef95/i/2015/125/b/a/smooth_criminal_by_sherlingtondunnen-d1f6f7s.jpg',
        info_labels={"originaltitle":"Micheal Jackson","genre":"crime,british", "plot":"Shhhh while the king speaks!!!", "mpaa":"U"})		
		
    Add_Dir(name='Micheal Jackson Thriller', url='https://www.youtube.com/watch?v=Tugf-vteliI', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://img00.deviantart.net/ef95/i/2015/125/b/a/smooth_criminal_by_sherlingtondunnen-d1f6f7s.jpg',
        fanart='http://img00.deviantart.net/ef95/i/2015/125/b/a/smooth_criminal_by_sherlingtondunnen-d1f6f7s.jpg',
        info_labels={"originaltitle":"Micheal Jackson","genre":"crime,british", "plot":"Shhhh while the king speaks!!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Micheal Jackson Bad', url='https://www.youtube.com/watch?v=dsUXAEzaC3Q', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://d298698jupi3ov.cloudfront.net/endless/037776E9-25F4-46CB-802E-3894446061A3.jpg',
        fanart='http://d298698jupi3ov.cloudfront.net/endless/037776E9-25F4-46CB-802E-3894446061A3.jpg',
        info_labels={"originaltitle":"Micheal Jackson","genre":"crime,british", "plot":"Shhhh while the king speaks!!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Micheal Jackson Beat It', url='https://www.youtube.com/watch?v=oRdxUFDoQe0', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://68.media.tumblr.com/d9d205b9ed0469fad1bd88b27a3379da/tumblr_muh0vumJBR1rjplc4o2_400.jpg',
        fanart='http://68.media.tumblr.com/d9d205b9ed0469fad1bd88b27a3379da/tumblr_muh0vumJBR1rjplc4o2_400.jpg',
        info_labels={"originaltitle":"Micheal Jackson","genre":"crime,british", "plot":"Shhhh while the king speaks!!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Micheal Jackson Leave Me Alone', url='https://www.youtube.com/watch?v=crbFmpezO4A', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.eil.com/large_image/MICHAEL_JACKSON_MICHAEL%2BJACKSON%2B-%2BLEAVE%2BME%2BALONE-624471.jpg',
        fanart='http://images.eil.com/large_image/MICHAEL_JACKSON_MICHAEL%2BJACKSON%2B-%2BLEAVE%2BME%2BALONE-624471.jpg',
        info_labels={"originaltitle":"Micheal Jackson","genre":"crime,british", "plot":"Shhhh while the king speaks!!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Micheal Jackson Ghost', url='https://www.youtube.com/watch?v=Xh9Cp4rd7mI', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://michaeljackson8x10photos.com/michaeljacksonphotosghostsposterjun2811a.jpg',
        fanart='http://michaeljackson8x10photos.com/michaeljacksonphotosghostsposterjun2811a.jpg',
        info_labels={"originaltitle":"Micheal Jackson","genre":"crime,british", "plot":"Shhhh while the king speaks!!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Micheal Jackson In The Closet', url='https://www.youtube.com/watch?v=4qLY0vbrT8Q', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.eil.com/large_image/MICHAEL_JACKSON_MICHAEL%2BJACKSON%2B-%2BLEAVE%2BME%2BALONE-624471.jpg',
        fanart='http://images.eil.com/large_image/MICHAEL_JACKSON_MICHAEL%2BJACKSON%2B-%2BLEAVE%2BME%2BALONE-624471.jpg',
        info_labels={"originaltitle":"Micheal Jackson","genre":"crime,british", "plot":"Shhhh while the king speaks!!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Micheal Jackson The way You Make Me Feel', url='https://www.youtube.com/watch?v=HzZ_urpj4As', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/originals/f9/39/fe/f939fef7b0c588edfc7f3fe4ceeb2e49.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/originals/f9/39/fe/f939fef7b0c588edfc7f3fe4ceeb2e49.jpg',
        info_labels={"originaltitle":"Micheal Jackson","genre":"crime,british", "plot":"Shhhh while the king speaks!!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
		
    Add_Dir(name='Micheal Jackson Billie Jean', url='https://www.youtube.com/watch?v=Zi_XLOBDo_Y', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://img.desmotivaciones.es/201207/MichaelJacksonBillieJean.jpg',
        fanart='http://img.desmotivaciones.es/201207/MichaelJacksonBillieJean.jpg',
        info_labels={"originaltitle":"Micheal Jackson","genre":"crime,british", "plot":"Shhhh while the king speaks!!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Micheal Jackson You Rock My World', url='https://www.youtube.com/watch?v=g4tpuu-Up90', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.eil.com/large_image/MICHAEL_JACKSON_MICHAEL%2BJACKSON%2B-%2BLEAVE%2BME%2BALONE-624471.jpg',
        fanart='http://images.eil.com/large_image/MICHAEL_JACKSON_MICHAEL%2BJACKSON%2B-%2BLEAVE%2BME%2BALONE-624471.jpg',
        info_labels={"originaltitle":"Micheal Jackson","genre":"crime,british", "plot":"Shhhh while the king speaks!!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Micheal Jackson Who Is It', url='https://www.youtube.com/watch?v=PfrV_6yWbEg', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://images.eil.com/large_image/MICHAEL_JACKSON_MICHAEL%2BJACKSON%2B-%2BLEAVE%2BME%2BALONE-624471.jpg',
        fanart='http://images.eil.com/large_image/MICHAEL_JACKSON_MICHAEL%2BJACKSON%2B-%2BLEAVE%2BME%2BALONE-624471.jpg',
        info_labels={"originaltitle":"Micheal Jackson","genre":"crime,british", "plot":"Shhhh while the king speaks!!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Tupac Hit Em Up', url='https://www.youtube.com/watch?v=41qC3w3UUkU', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://escobar300.files.wordpress.com/2016/06/hit-em-up-3.jpg',
        fanart='https://escobar300.files.wordpress.com/2016/06/hit-em-up-3.jpg',
        info_labels={"originaltitle":"Tupac","genre":"crime,british", "plot":"This is what you call rap!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
		
    Add_Dir(name='Tupac Changes', url='https://www.youtube.com/watch?v=uS4CvCGFyqc', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        info_labels={"originaltitle":"Tupac","genre":"crime,british", "plot":"This is what you call rap!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
		
    Add_Dir(name='Tupac I Get Around', url='https://www.youtube.com/watch?v=YqJAnQTwmJs', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        info_labels={"originaltitle":"Tupac","genre":"crime,british", "plot":"This is what you call rap!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
		
    Add_Dir(name='Tupac To Live And Die In L.A', url='https://www.youtube.com/watch?v=Wz2wVLyTar4', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        info_labels={"originaltitle":"Tupac","genre":"crime,british", "plot":"This is what you call rap!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
		
    Add_Dir(name='Tupac Amerikaz Most Wanted', url='https://www.youtube.com/watch?v=BL6dWDfs5x8', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        info_labels={"originaltitle":"Tupac","genre":"crime,british", "plot":"This is what you call rap!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Tupac Toss It Up', url='https://www.youtube.com/watch?v=ONyV610j4sU', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        info_labels={"originaltitle":"Tupac","genre":"crime,british", "plot":"This is what you call rap!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Tupac California Love', url='https://www.youtube.com/watch?v=5wBTdfAkqGU', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        info_labels={"originaltitle":"Tupac","genre":"crime,british", "plot":"This is what you call rap!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Tupac How Do You Want It', url='https://www.youtube.com/watch?v=ZZJ6BfNuaCw', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        info_labels={"originaltitle":"Tupac","genre":"crime,british", "plot":"This is what you call rap!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Tupac Made Niggaz', url='https://www.youtube.com/watch?v=WuoC04OXe9M', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        info_labels={"originaltitle":"Tupac","genre":"crime,british", "plot":"This is what you call rap!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})

    Add_Dir(name='Tupac Letter To My Unborn', url='https://www.youtube.com/watch?v=SPmNQmmMZ84', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        fanart='https://s-media-cache-ak0.pinimg.com/736x/6a/a0/3f/6aa03fa0b2dd51b914d37715b3b3e811--pac-poster-pac-changes.jpg',
        info_labels={"originaltitle":"Tupac","genre":"crime,british", "plot":"This is what you call rap!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
#-----------------------------	
@route(mode="video_towers")
def Video_Towers():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='Fawlty Towers A Touch Of Class', url='http://greeksattv.co.uk/Mario/FawltyTowers/Fawlty%20Towers%20-%20A%20touch%20of%20class.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        fanart='http://www.limelightmagazine.com.au/sites/www.limelightmagazine.com.au/files/fawlty_2745808a.jpg',
        info_labels={"originaltitle":"Fawlty Towers","genre":"crime,british", "plot":"Basil Making a Hash Of Everything", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})	
		
    Add_Dir(name='Fawlty Towers The Builders', url='http://greeksattv.co.uk/Mario/FawltyTowers/Fawlty%20Towers%20-%20The%20builders.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        fanart='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        info_labels={"originaltitle":"Fawlty Towers","genre":"crime,british", "plot":"Basil Making a Hash Of Everything", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='Fawlty Towers The Hotel Inspector', url='http://greeksattv.co.uk/Mario/FawltyTowers/Fawlty%20Towers%20-%20The%20hotel%20inspectors.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        fanart='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        info_labels={"originaltitle":"Fawlty Towers","genre":"crime,british", "plot":"Basil Making a Hash Of Everything", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='Fawlty Towers The Weeding Party', url='http://greeksattv.co.uk/Mario/FawltyTowers/Fawlty%20Towers%20-%20The%20wedding%20party.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        fanart='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        info_labels={"originaltitle":"Fawlty Towers","genre":"crime,british", "plot":"Basil Making a Hash Of Everything", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='Fawlty Towers Gourmet Night', url='http://greeksattv.co.uk/Mario/FawltyTowers/Fawlty%20Towers%20-%20Gourmet%20night.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        fanart='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        info_labels={"originaltitle":"Fawlty Towers","genre":"crime,british", "plot":"Basil Making a Hash Of Everything", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='Fawlty Towers Communication Problems', url='http://greeksattv.co.uk/Mario/FawltyTowers/Fawlty%20Towers%20-%20Communication%20problems.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        fanart='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        info_labels={"originaltitle":"Fawlty Towers","genre":"crime,british", "plot":"Basil Making a Hash Of Everything", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='Fawlty Towers The Germans', url='http://greeksattv.co.uk/Mario/FawltyTowers/Fawlty%20Towers%20-%20The%20Germans.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        fanart='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        info_labels={"originaltitle":"Fawlty Towers","genre":"crime,british", "plot":"Basil Making a Hash Of Everything", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='Fawlty Towers The Psychiatrist', url='http://greeksattv.co.uk/Mario/FawltyTowers/Fawlty%20Towers%20-%20The%20psychiatrist.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        fanart='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        info_labels={"originaltitle":"Fawlty Towers","genre":"crime,british", "plot":"Basil Making a Hash Of Everything", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='Fawlty Towers Basil The Rat', url='http://greeksattv.co.uk/Mario/FawltyTowers/Fawlty%20Towers%20-%20Basil%20the%20rat.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        fanart='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        info_labels={"originaltitle":"Fawlty Towers","genre":"crime,british", "plot":"Basil Making a Hash Of Everything", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='Fawlty Towers The Anniversary', url='http://greeksattv.co.uk/Mario/FawltyTowers/Fawlty%20Towers%20-%20The%20anniversary.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        fanart='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        info_labels={"originaltitle":"Fawlty Towers","genre":"crime,british", "plot":"Basil Making a Hash Of Everything", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='Fawlty Towers The Kipper And The Corpse', url='http://greeksattv.co.uk/Mario/FawltyTowers/Fawlty%20Towers%20-%20The%20kipper%20and%20the%20corpse.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        fanart='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        info_labels={"originaltitle":"Fawlty Towers","genre":"crime,british", "plot":"Basil Making a Hash Of Everything", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='Fawlty Towers Waldorf Salad', url='http://greeksattv.co.uk/Mario/FawltyTowers/Fawlty%20Towers%20-%20Waldorf%20salad.avi', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        fanart='https://art-s.nflximg.net/d644c/148ab05cb88f5ab555a8d7dab5c15438d60d644c.jpg',
        info_labels={"originaltitle":"Fawlty Towers","genre":"crime,british", "plot":"Basil Making a Hash Of Everything", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
#-----------------------------	
@route(mode="video_tube")
def Video_Tube():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='Yarael Poof Complete Robot Chicken Star Wars', url='https://www.youtube.com/watch?v=2emv5A7OlVM', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/51WGPtiberL.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/51WGPtiberL.jpg',
        info_labels={"originaltitle":"Robot Chicken","genre":"crime,british", "plot":"Does Anyone Realise I Love This Shit!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='The Best of Yoda Robot Chicken Star Wars', url='https://www.youtube.com/watch?v=6S3rfDnhO3o', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/51WGPtiberL.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/51WGPtiberL.jpg',
        info_labels={"originaltitle":"Robot Chicken","genre":"crime,british", "plot":"Does Anyone Realise I Love This Shit!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})	
				
    Add_Dir(name='Robot Chicken Star Wars Episode II & III Funniest Moments', url='https://www.youtube.com/watch?v=GPria4lrLRc', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/51WGPtiberL.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/51WGPtiberL.jpg',
        info_labels={"originaltitle":"Robot Chicken","genre":"crime,british", "plot":"Does Anyone Realise I Love This Shit!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='Best of Darth Vader Robot Chicken Star Wars', url='https://www.youtube.com/watch?v=0u_iqh7Dt8M', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/51WGPtiberL.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/51WGPtiberL.jpg',
        info_labels={"originaltitle":"Robot Chicken","genre":"crime,british", "plot":"Does Anyone Realise I Love This Shit!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
				
    Add_Dir(name='The Best of the Dark Side Robot Chicken Star Wars', url='https://www.youtube.com/watch?v=AFcGcKjE5ME', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/I/51WGPtiberL.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/I/51WGPtiberL.jpg',
        info_labels={"originaltitle":"Robot Chicken","genre":"crime,british", "plot":"Does Anyone Realise I Love This Shit!!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})		
						
    Add_Dir(name='Everything Wrong With Men In Black In 16 Minutes Or Less', url='https://www.youtube.com/watch?v=QYouL4GBu5c', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
								
    Add_Dir(name='Everything Wrong With Ghostbusters 2016', url='https://www.youtube.com/watch?v=RoaS3-3ks2g&t=1209s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
								
    Add_Dir(name='Everything Wrong With Pirates Of The Caribbean: On Stranger Tides', url='https://www.youtube.com/watch?v=KJxoBVVCOos', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
								
    Add_Dir(name='Everything Wrong With Passengers In 16 Minutes Or Less', url='https://www.youtube.com/watch?v=jz_gA1IjDW4', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
								
    Add_Dir(name='Everything Wrong With Dr. Strange In 15 Minutes Or Less', url='https://www.youtube.com/watch?v=8ZKmRpV9OFg', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
								
    Add_Dir(name='Everything Wrong With Suicide Squad In 20 Minutes Or Less', url='https://www.youtube.com/watch?v=NH5YLq412Wc&t=529s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
								
    Add_Dir(name='Everything Wrong With Now You See Me 2', url='https://www.youtube.com/watch?v=eK1wlA7SWFs', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
								
    Add_Dir(name='Everything Wrong With Angels & Demons In 17 Minutes Or Less', url='https://www.youtube.com/watch?v=szgSi4GEiHw&t=365s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
								
    Add_Dir(name='Everything Wrong With Captain America: Civil War', url='https://www.youtube.com/watch?v=FbWOEpLFYbU&t=390s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
								
    Add_Dir(name='Everything Wrong With Batman v Superman: Dawn of Justice', url='https://www.youtube.com/watch?v=X5tSpgU96WY', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
								
    Add_Dir(name='Everything Wrong With Star Wars: Episode VII The Force Awakens', url='https://www.youtube.com/watch?v=H6_zvQQ5P8w&t=307s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With The Martian With Dr. Neil deGrasse Tyson', url='https://www.youtube.com/watch?v=HzNyMUuQfmE&t=703s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With Olympus Has Fallen In 15 Minutes', url='https://www.youtube.com/watch?v=ECeaa60DCkY', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With Mission Impossible Rogue Nation', url='https://www.youtube.com/watch?v=PHRtNJhNvMY&t=833s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With Star Wars Episode III: Revenge of the Sith, Part 1', url='https://www.youtube.com/watch?v=m0TGcvtzjUs&t=578s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With Star Wars Episode III: Revenge of the Sith, Part 2', url='https://www.youtube.com/watch?v=hD7xZFLhTq8&t=634s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With Star Wars Episode II: Attack of the Clones Part 1', url='https://www.youtube.com/watch?v=ln7HQCbonho', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With Star Wars Episode II: Attack of the Clones Part 2', url='https://www.youtube.com/watch?v=-Iw_CZtq4LI&t=694s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With Star Wars Episode I: The Phantom Menace, Part 1', url='https://www.youtube.com/watch?v=XeXDrvPB5rI', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With Star Wars Episode I: The Phantom Menace, Part 2', url='https://www.youtube.com/watch?v=K8ea7OiaLWo&t=661s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With Return of the Jedi', url='https://www.youtube.com/watch?v=7LMsOPeeOUM&t=1s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With The Empire Strikes Back', url='https://www.youtube.com/watch?v=g_0yLbcV3U8&t=737s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With Star Wars Episode IV A New Hope', url='https://www.youtube.com/watch?v=l6sdpH5N1c0', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
										
    Add_Dir(name='Everything Wrong With Jurassic World In 15 Minutes Or Less', url='https://www.youtube.com/watch?v=73dPzpQ-qsU', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
												
    Add_Dir(name='Everything Wrong With Scream in 16 Minutes Or Less', url='https://www.youtube.com/watch?v=BFKTuXb5eKI', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
												
    Add_Dir(name='Everything Wrong With Back to the Future 2', url='https://www.youtube.com/watch?v=kdU7xk8TISk', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
												
    Add_Dir(name='Everything Wrong With Pirates of the Caribbean: At Worlds End', url='https://www.youtube.com/watch?v=IdUhQFXhQUM', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
												
    Add_Dir(name='Everything Wrong With Super Mario Bros. In 21 Minutes Or Less', url='https://www.youtube.com/watch?v=PYQHnPOYc5Q', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
												
    Add_Dir(name='Everything Wrong With Batman Forever In 18 Minutes Or Less', url='https://www.youtube.com/watch?v=mAGG9w4QzQo', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
												
    Add_Dir(name='Everything Wrong With I Know What You Did Last Summer', url='https://www.youtube.com/watch?v=44D3O2LoCgY', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
												
    Add_Dir(name='Everything Wrong With Non-Stop In 12 Minutes Or Less', url='https://www.youtube.com/watch?v=fo7YtjQOg9Q', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
												
    Add_Dir(name='Everything Wrong With Guardians Of The Galaxy', url='https://www.youtube.com/watch?v=hHO984ysBJQ', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
												
    Add_Dir(name='Everything Wrong With Pirates of the Caribbean: Dead Mans Chest', url='https://www.youtube.com/watch?v=XZtfERCwQO8&t=797s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Everything Wrong With Edge Of Tomorrow', url='https://www.youtube.com/watch?v=Yd4exe1aPfA&t=51s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Everything Wrong With Transformers: Age of Extinction Part 1', url='https://www.youtube.com/watch?v=c97NAlvu3n0', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Everything Wrong With Transformers: Age of Extinction Part 2', url='https://www.youtube.com/watch?v=wHZHSt1CSgo', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Everything Wrong With Childs Play In 16 Minutes Or Less', url='https://www.youtube.com/watch?v=zXSmZhr6_uQ', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Everything Wrong With Transformers: Dark Of The Moon', url='https://www.youtube.com/watch?v=4ORoPgZLeuc&t=437s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Everything Wrong With Transformers: Revenge of the Fallen', url='https://www.youtube.com/watch?v=Xoe1p_NrFwg', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Everything Wrong With Spider-Man 3', url='https://www.youtube.com/watch?v=GrDwtLl1p0A', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Everything Wrong With Spider-Man 2 In 11 Minutes Or Less', url='https://www.youtube.com/watch?v=Ua8C_vsEc50', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Everything Wrong With Spider-Man In 11 Minutes Or Less', url='https://www.youtube.com/watch?v=1aphO1Zd2kg', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Everything Wrong With Saw In 8 Minutes Or Less', url='https://www.youtube.com/watch?v=NSR8WLrl8CQ', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
														
    Add_Dir(name='Everything Wrong With Thor In 8 Minutes Or Less', url='https://www.youtube.com/watch?v=tppBPrjSsOw&t=37s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																
    Add_Dir(name='Everything Wrong With Iron Man 3', url='https://www.youtube.com/watch?v=YNcJPxjoxF0&t=179s', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																
    Add_Dir(name='Everything Wrong With World War Z In 6 Minutes Or Less', url='https://www.youtube.com/watch?v=tss--a2XxMY', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																
    Add_Dir(name='Everything Wrong With Pirates Of The Caribbean - The Curse Of The Black Pearl', url='https://www.youtube.com/watch?v=ze6YqV-mRTI', mode='scrape_sites', folder=False, content_type='Video',
        icon='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        fanart='http://2.bp.blogspot.com/-mYmq0P596ac/U6DOv9xgw3I/AAAAAAAAAVg/bIW05cHisnw/s1600/CS.jpg',
        info_labels={"originaltitle":"Everything Wrong With","genre":"crime,british", "plot":"Movie Mistakes And Plot Holes", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																
    Add_Dir(name='Magics Biggest Secrets Finally Revealed S01E01', url='https://www.youtube.com/watch?v=JT4YFHB-mvc', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																
    Add_Dir(name='Breaking the Magicians Code: Magics Biggest Secrets Finally Revealed S01E02', url='https://www.youtube.com/watch?v=QMbDYW3OaiQ&t=5s', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																		
    Add_Dir(name='Breaking the Magicians Code: Magics Biggest Secrets Finally Revealed S01E03', url='https://www.youtube.com/watch?v=dsXs_YOfnCs', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																		
    Add_Dir(name='Breaking the Magicians Code: Magics Biggest Secrets Finally Revealed S01E04', url='https://www.youtube.com/watch?v=bhyac8LWzOU', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																		
    Add_Dir(name='Magics Biggest Secrets Finally Revealed S01E06', url='https://www.youtube.com/watch?v=PUhglavOi-o&t=7s', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																		
    Add_Dir(name='Magics Biggest Secrets Finally Revealed S01E07', url='https://www.youtube.com/watch?v=JQshYliIc0E&t=3s', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																		
    Add_Dir(name='Magics Biggest Secrets Finally Revealed S01E08', url='https://www.youtube.com/watch?v=YQ33cV9qcww', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																		
    Add_Dir(name='Magics Biggest Secrets Finally Revealed S01E09', url='https://www.youtube.com/watch?v=jbQYb9TaHJY', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																		
    Add_Dir(name='Breaking The Magicians Code: Magics Biggest Secrets Finally Revealed S02E02', url='https://www.youtube.com/watch?v=VnnsX3rzh54', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																		
    Add_Dir(name='Breaking The Magicians Code: Magics Biggest Secrets Finally Revealed S02E04', url='https://www.youtube.com/watch?v=PAe_30JER_c', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																		
    Add_Dir(name='Breaking The Magicians Code: Magics Biggest Secrets Finally Revealed S02E05', url='https://www.youtube.com/watch?v=-g4N1uMtu8o&t=5s', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='Breaking The Magicians Code Magics Biggest Secrets Finally Revealed S02E09', url='https://www.youtube.com/watch?v=rqQ8_OhUG-Y', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='Breaking The Magicians Code: Magics Biggest Secrets Finally Revealed S02E10', url='https://www.youtube.com/watch?v=PqUTGX5kJGQ', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='Breaking The Magicians Code: Magics Biggest Secrets Finally Revealed S02E11', url='https://www.youtube.com/watch?v=ubfgVcE69y8', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
																				
    Add_Dir(name='Breaking The Magicians Code: Magics Biggest Secrets Finally Revealed S02E12', url='https://www.youtube.com/watch?v=cKhjHnqE8WQ', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BZGM0MGVmMzYtZmFhMi00NDQ0LTlkNzQtOTIwNzdkMDkyNDE5XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UY1200_CR224,0,630,1200_AL_.jpg',
        info_labels={"originaltitle":"Breaking the Magicians Code","genre":"crime,british", "plot":"Magic Revealed!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
#-----------------------------		
@route(mode="music_examples")
def Music_Examples():
    """
This is an example of adding a song, there's a good chance the scaper will find no results for this song,
it's only here as an example to show how to set things like artwork.
    """
    Add_Dir(name='Sally Cinnamon - Stone Roses', url='song_dialog', mode='scrape_sites', folder=False,
        icon='http://images.rapgenius.com/7929026cc89ab0c77669dee5cc323da9.530x528x1.jpg',
        fanart='http://www.flickofthefinger.co.uk/wp-content/uploads/2016/03/the-stone-roses-1.jpg',
        info_labels={"genre":"Rock,Inde,British", "artist":"Stone Roses", "title":"Sally Cinnamon"})
#-----------------------------
@route(mode="scrape_sites", args=["url"])
def Scrape_Sites(list_type):
    """
This is just a very rough example showing how simple it is to make use of the NaN Scrapers module.
We send through details of what we want to find and NaN Scrapers will search multiple websites for this content.
    """
    content = ''
    if list_type == 'movie_dialog':
        content = nanscrapers.scrape_movie_with_dialog(title='Trainspotting', year='1996', imdb='tt0117951', host=None, include_disabled=False, timeout=30)
    elif list_type == 'episode_dialog':
        content = nanscrapers.scrape_episode_with_dialog(title='Fraggle Rock', show_year='1983', year='1985', season='3', episode='4', imdb='tt0085017', tvdb=None, host=None, include_disabled=False, timeout=30)
    elif list_type == 'song_dialog':
        content = nanscrapers.scrape_song_with_dialog(title='Fools Gold', artist='Stone Roses', host=None, include_disabled=False, timeout=30)

# If the item returned is a dictionary that's great we know we have a list to work with
    if koding.Data_Type(content) == 'dict':
        xbmc.log(repr(content),2)
        playback = koding.Play_Video(video=content["url"], showbusy=True)
 
# It may be a plugin or direct url has been sent through, if so lets use the list_type variable
    elif not list_type.endswith('_dialog'):
        playback = koding.Play_Video(video=list_type, showbusy=True)

# Nothing useful has been found, lets exit back to the list
    else:
        return

# If the playback returned as True then it was successful but if it was False we know we need to try again for another source
    if not playback:
        if dialog.yesno('PLAYBACK FAILED','The video may have been removed, the web host may have altered their code or this video may not be available in your region. [COLOR=dodgerblue]Would you like to try another source?[/COLOR]'):
            Scrape_Sites(list_type)

#----------------------------------------------------------------
"""
    SECTION 7:
    Essential if creating list items, this tells kodi we're done creating our list items.
    The list will not populate without this
"""
Run()
xbmcplugin.endOfDirectory(int(sys.argv[1]))