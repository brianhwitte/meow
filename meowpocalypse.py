'''to do:
    update inventory and room contents with contents function.
    make sure player can move from room to room
    fill out item descriptions
    write room descriptions
    
'''
from sys import exit
from random import randint


class Scene(object):
    # the parent class for each 'room' in the adventure

    # Can I rewrite the item control in one big dictionary? Items {mouse: { description: x, status: y, location: z}}
    mr_meow_happiness = 0
    pets = 0
    mouse = False
    box = False
    # the stuff carried by the main character
    inventory = ['thing 1', 'thing 2', 'thing 3']
    
    # a library that contains all the items found in each room
    room_contents = {
    "front_door": ['shoes', 'hatrack', 'mouse'],
    "living_room": ['chair', 'glass', 'rug'],
    "bed_room": ['blanket', 'pillow', 'magazine'],
    "bath_room": ['litter', 'scoop'],
    "kitchen": ['tuna', 'bowl', 'nip']
}
    # descriptions of each item in the game.
    descriptions = {
        'shoes': 'They\'re a ratty old pair of sneakers.  It looks likes someone has been nibbling on the laces.',
        'hatrack': 'The hat rack is empty.  This is unsurprising since you don\'t own any hats.',
        'mouse': 'This toy is an off-white, vaguely mouse-shaped plush toy. It is looking very well loved.  It has a pouch that you distinctly recall having filled with cat nip a few days ago.  The pouch is conspicuously empty.',
        'cat': 'Mr. Meow is your best friend and overlord.  He may be a bit pudgy from treat overload, but he\'s all the more pettable for that.'
    }
    items = {
        'cat': {
            'name': 'Mr. Meow',
            'description': 'Mr. Meow is the best cat ever.',
            'location': 'With you.',
            'mr_meow_happiness': 0,
            'pets': 0,
            'nip': False,
            'blanket': False,
            'dinner': False,
            'box': False
        },
        'mouse': {
            'name': 'mouse',
            'description': 'This toy is an off-white, vaguely mouse-shaped plush toy. It is looking very well loved.  It has a pouch that you distinctly recall having filled with cat nip a few days ago.  The pouch is conspicuously empty.',
            'location': 'front_door',
            'status': False
        },
        'blanket': {
            'name': 'blanket',
            'description': 'This is a very fuzzy fleece blanket covered in cat hair.  Clearly a favorite.',
            'location': 'bedroom',
            'status': False
        },
        'glass': {
            'name': 'water glass',
            'description': 'An empty pint glass.',
            'location': 'living_room'
        },
        'shoes': {
            'name': 'shoes',
            'description': 'They\'re a ratty old pair of sneakers.  It looks likes someone has been nibbling on the laces.',
            'location': 'front_door'
        },
        'hatrack': {
            'description': 'The hat rack is empty.  This is unsurprising since you don\'t own any hats.',
            'location': 'front_door'
            },
        'chair': {
            'description': 'The chair is old and comfy with an indentation exactly the size of your bum.  You remember many happy hours spent in this chair, a purring cat on the blanket on your lap.',
            'location': 'living_room'
            }
        }

    


    def enter(self):
        # the enter function handles the description of each room as well as unique actions that can only be done in each room
        print "some stuff happens"
        exit(1)

    def contents(self, place):
        # This function goes through all the items to dynamically generate a list of all the items in a particular location.
        stuff = []
        for x in self.items:
            if self.items[x]['location'] == place:
                stuff.append(self.items[x])

        return stuff

    def standard_actions(self, action, room):
        # This function handles actions that could happen in any room.  
        # The action parameter is the string input by the player in a particular room.
        # The room parameter is the room the player is currently in.
        
        commands = action.split()
        # changes the words of the player's last move into a list for easier matching

        if ('pet' in action) and (('cat' in action) or ('meow' in action)):
            # petting will only make Mr. Meow happy up to a point.  To win, you need to raise his happiness higher.
            if self.items['cat']['pets'] > 5:
                print "Mr. Meow accepts your touch, but he clearly wants something other than pets."
            else:
                print "Mr. Meow purrs. He looks a little happier."
                self.items['cat']['mr_meow_happiness'] += 1
                self.items['cat']['pets'] += 1

            # a list of what you're carrying.
        elif ('i' in commands) or ('inventory' in commands):

            print 'Your inventory contains ' + ', '.join(self.inventory[0:-1]) + ', and a ' + self.inventory[-1]

        elif ('look' in action) and (('cat' in action) or ('meow' in action)):
            if Engine.mr_meow_happiness < 5:
                print self.descriptions['cat'] + "\n" + "Mr. Meow is looking crabby.  He could really use some pettting."
            elif 5 <= Engine.mr_meow_happiness <= 10:
                print self.descriptions('cat') + "\n" + "Mr. Meow is dissatisfied.  What else could make a cat happier?"
            elif 10 < Engine.mr_meow_happiness <= 19:
                print self.descriptions('cat') + "\n" + "Mr. Meow is chirping with satisfaction, but something is still missing."
            else:
                print self.descriptions('cat') + "\n" + "Mr. Meow is as happy as a cat can be.  All he needs now is a lap in which to curl up."
            

            # the 'any' function checks for whether any of the words in command are also among the contents of the room.
            # If yes, the player can look at the item for a description, or take it with them.
        elif any(True for word in commands if word in self.room_contents[room]):
            item = [i for i in commands if i in self.room_contents[room]][0]
            if "look" in action:
            
                print self.descriptions[item]

            elif "take" in action:

                print "You take the %s" % item
                self.inventory.append(item)
                self.room_contents[room].remove(item)

            else:
                print "You can't do that with that!"

        elif "drop" in commands:
            item = [i for i in commands if i in self.inventory][0]
            if any(True for word in commands if word in self.inventory):
                self.inventory.remove(item)
                self.room_contents[room].append(item)
                print "You leave the %s in the %s." % (item, room)
            else:
                print "You don't have a %s" % item
           
        elif any(True for word in commands if word in self.inventory):
            item = [i for i in commands if i in self.inventory][0]
            print self.descriptions[item] + '\nYou are carrying the %s with you.' % item
        else:
            print 'Hwut?'
        
        


class Engine(object):


    
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')


        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Finished(Scene):
    
    def enter(self):
        print "Mr. Meow is satisfied.  He sits on your lap and purrs and purrs and purrs.  Soon it will be time for lunch..."
        exit(1)

class FrontDoor(Scene):

    def enter(self):
        things_in_room = self.contents('front_door')
        print "You open the front door after a long day at work.  You are greated by a large orange cat who swirls about your ankles."
        print "Mr. Meow wants something.  But what could it be?"
        print "\n"
        print "You see a " + ', a '.join(self.room_contents['front_door'][0:-1]) + ' and a ' + self.room_contents['front_door'][-1] + '\n'
        print "You can 'look' at items or the room, you can 'pet' Mr. Meow, you can 'take' items with you.  When you 'go' to the 'kitchen' the game will end.  No other rooms are currently functional."

        action = raw_input("> ")


        while True:
            
            if "look" and "room" in action:
                print "You see a kitchen, a living room, and further away, the bedroom."
                action = str.lower(raw_input("> "))
            elif "kitchen" and "go" in action:
                print "You walk into the kitchen.  Mr. Meow gets there just before you."
                return 'kitchen'
                break
            else:
                self.standard_actions(action, 'front_door')
                action = str.lower(raw_input("> "))

class LivingRoom(Scene):
    pass

class Kitchen(Scene):
    def enter(self):

        print "You made it to the kitchen!"
        return 'finished'

class BedRoom(Scene):
    pass


class Map(object):

    scenes = {
        'front_door': FrontDoor(),
        'living_room': LivingRoom(),
        'kitchen': Kitchen(),
        'bed_room': BedRoom(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('front_door')
a_game = Engine(a_map)
a_game.play()
