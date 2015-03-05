from sys import exit
from random import randit

class Scene(object):
    
    def enter(self):
        print "This scene is not yet configured. Subclass it and"
        print "implement it enter()"
        exit(1)
        
class Engine(object):

    def __init__(self):
        self.scene_map = scene_map   # From self get scene_map attribute and set it to scene_map.
        
    def play(self):
        current_scene = self.scene_map.opening_scene()  # Beginning scene of the game is called.
        last_scene = self.scene_map.next('done')  # Last scene of game is when 'done' is returned.
        
        while current_scene != last_scene:
            next_scene = current_scene.enter()  # Set the next scene to an instance of class enter. 
            current_scene = self.scene_map.next_scene(next_scene_map) # 
            
        current_scene.enter()  # Print out the last scene.
              
class GameOver(Scene):

    violence = [
        "Before dying, your past and future flashes before your eyes. You are sorry for what you've done...",
        "If only you would have known that this was too dangerous...",
        "As your final thought, you think about your love, and whisper: 'I... am... sorry...'",
        "Peace finally enters your world as ascend to the heavens.",
        "Before your final breath, you pull out a picture of your wife from your pocket and kiss her.",
        "You struggle to stand up one last time, but you fail as you drop dead in a pool of blood.",
        "You die in a miserable way, and finally acknowledge you had a miserable life.",
        "There is no way this could have happened...",
        "As you are dying, you shout: 'WHY!? WHY DID THIS HAVE TO HAPPEN TO ME DAMMIT!!???'"     
    ]
    
    def enter(self):
        print GameOver.violence[randit(0, len(self.ways_death)-1)]
        exit(1)
        


class Done(object):
    
    def enter(self):           # Chapter 5 material to be removed from runtime.py
        print "Your journey through the unknown has sadly come to an end."
        print "Your love was very pleased to see you back and was"
        print "extremely grateful of hearing all of those adventure
        print "stories you experienced.\n"
        print "'A truly amazing rock 'n roll ride, %s!'" % first
        print "'Haha I had the most fun ever!'"
        print "'No kidding'"
        print "\n"
        print "You spot a red-and-blue blankets hiding something"
        print "on top of the table, but you turn your attention"
        print "away from it.\n"
        print "\nOnce everything settled down, you look at"
        print "the date and time."
        raw_input("Date?")
        print "December 20th 2012.
        raw_input("The time?")
        print "11:48pm"
        raw_input()
        print "Wow, just in time for the end."
        print "'Honey, in twelve minutes, the whole world will explode.'"
        print "'*Looks at time*"
        print "'Hell damn you are right %s!'" % first
        print "'Then let's celebrate MY arrival AND the end of"
        print "the world.'"
        print "'Annnnddd here's the alcohol! *Lover pulls the blankets from the surprise'"
        print "'Hell let's bring Robert into this.'"
        print "You wake Robert up, and bring him to the kitchen."
        raw_input()
        print "'Alright people! Let us celebrate MY successful ARRIVAL, and let us"
        print "celebrate ONE LAST TIME before we ALL die tomorrow!"
        print "Cheers and peace family! Let's drink 'till we drown so we can all die"
        print "together! CHEERS!'"
        print "'FOR YOUR SURVIVAL!'"
        print "'FOR YOUR VICTORY!'"
        print "'CHEERS!'"
        raw_input()
        
        
    def enter(self):    # Ending material, the true stuff
        print "
        print "
        
        
        return 'done'
        
        
class Map(object)

    scenes = {
        'airport_vien': AirportV(),
        'cat': CAT(),
        'dinner1_vien': DineVien1(),
        'sleep_vien': SleepVien(),
        'wake_up_day1_vien': WakeUp1Vien(),
        '
        '
        '
        '
        '
        
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
                
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
a_map = Map(' INSERT FIRST SCENE  ') # Set a_map to an instance of class map.
a_game = Engine(a_map)  # Set a_game to an instance of class Engine.
a_game.play() # Start the game up.
        
        
        
        

