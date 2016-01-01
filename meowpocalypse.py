'''to do:
    Done: update inventory and room contents with contents function.
    make sure player can move from room to room
    Done: fill out item descriptions
    write room descriptions
    add comments

'''
from sys import exit
from random import randint


class Scene(object):
    # the parent class for each 'room' in the adventure

    # a library that contains all the items found in each room
    '''room_contents = {
    "front_door": ['shoes', 'hatrack', 'mouse'],
    "living_room": ['chair', 'glass', 'rug'],
    "bed_room": ['blanket', 'pillow', 'magazine'],
    "bath_room": ['litter', 'scoop'],
    "kitchen": ['tuna', 'bowl', 'nip']
    }
    '''

    '''
    # descriptions of each item in the game.
    descriptions = {
        'shoes': 'They\'re a ratty old pair of sneakers.  It looks likes someone has been nibbling on the laces.',
        'hatrack': 'The hat rack is empty.  This is unsurprising since you don\'t own any hats.',
        'mouse': 'This toy is an off-white, vaguely mouse-shaped plush toy. It is looking very well loved.  It has a pouch that you distinctly recall having filled with cat nip a few days ago.  The pouch is conspicuously empty.',
        'cat': 'Mr. Meow is your best friend and overlord.  He may be a bit pudgy from treat overload, but he\'s all the more pettable for that.'
    }
    '''

    items = {
        'cat': {
            'name': 'Mr. Meow',
            'description': 'Mr. Meow is the best cat ever.',
            'location': 'With you.',
            'mr_meow_happiness': 0,
            'pets': 0,
            'takeable': False
        },

        'mouse': {
            'name': 'mouse',
            'description': 'This toy is an off-white, vaguely mouse-shaped plush toy. It is looking very well loved.  It has a pouch that you distinctly recall having filled with cat nip a few days ago.  The pouch is conspicuously empty.',
            'location': 'front_door',
            'status': False,
            'takeable': True
        },

        'blanket': {
            'name': 'blanket',
            'description': 'This is a very fuzzy fleece blanket covered in cat hair.  Clearly a favorite.',
            'location': 'bedroom',
            'status': False,
            'takeable': True
        },

        'glass': {
            'name': 'water glass',
            'description': 'An empty pint glass.',
            'location': 'living_room',
            'takeable': True
        },

        'shoe': {
            'name': 'shoe',
            'description': 'This is a ratty old sneaker (just the left one).  It looks likes someone has been nibbling on the laces.',
            'location': 'front_door',
            'takeable': True
        },

        'hatrack': {
            'name': 'hatrack',
            'description': 'The hat rack is empty.  This is unsurprising since you don\'t own any hats.',
            'location': 'front_door',
            'takeable': False
            },

        'chair': {
            'name': 'chair',
            'description': 'The chair is old and comfy with an indentation exactly the size of your bum.  You remember many happy hours spent in this chair, a purring cat on the blanket on your lap.',
            'location': 'living_room',
            'takeable': False
            },

        'bowl': {
            'name': 'bowl',
            'description': 'The bowl is ceramic with a cartoon fish skeleton painted into the glaze.  It is resting on a little pedastal...approximately cat-nose-height off the floor.  It is painfully, glaringly empty.',
            'location': 'kitchen',
            'tuna': False,
            'takeable': False
            },

        'catnip': {
            'name': 'catnip',
            'description': 'A plastic bottle containing an ounce of the finest cat intoxicant.  Mr. Meow would be very grateful if you could put some of this into a cat toy.',
            'location': 'kitchen',
            'takeable': True
            },

        'bag': {
            'name': 'bag',
            'location': 'kitchen',
            'description': 'A plastic garbage bag.  It looks ideal for holding smelly things.',
            'contents': [],
            'takeable': True
            },

        'tuna': {
            'name': 'tuna',
            'location': 'kitchen',
            'open': False,
            'takeable': True,
            'description': 'A can of kitty ambrosia.  Mr. Meow is staring at it fixedly.  Never has a creature so devoutly wished for opposable thumbs.  Fortunately, you have thumbs that could be used to open it with the simple pull tab, and put the tuna in a bowl.'
        },

        'litter': {
            'name': 'litter',
            'location': 'bath_room',
            'description': 'The litter box clearly needs some attention.  A scoop and a garbage bag would be really useful here.',
            'clean': False,
            'takeable': False
        },

        'scoop': {
            'name': 'scoop',
            'description': 'A slotted plastic scoop.  It\'s conveniently stored near the litter box.  You can use the scoop to clean the litter box, provided you have a bag to collect the debris.',
            'location': 'bath_room',
            'takeable': True
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
                stuff.append(self.items[x]['name'])

        return stuff

    def standard_actions(self, action, room):
        # This function handles actions that could happen in any room.  
        # The action parameter is the string input by the player in a particular room.
        # The room parameter is the room the player is currently in.
        
        commands = action.split()
        # changes the words of the player's last move into a list for easier matching

        if ('pet' in action) and (('cat' in action) or ('meow' in action)):
            # petting will only make Mr. Meow happy up to a point.  To win, you need to raise his happiness higher.
            if self.items['cat']['pets'] >= 5:
                print "Mr. Meow accepts your touch, but he clearly wants something other than pets."
            else:
                print "Mr. Meow purrs. He looks a little happier."
                self.items['cat']['mr_meow_happiness'] += 1
                self.items['cat']['pets'] += 1

        # a list of what you're carrying. The 'contents' function is called using 'inventory' as the location.
        elif ('i' in commands) or ('inventory' in commands):
            inventory = self.contents('inventory')
            if len(inventory) == 0:
                print 'You aren\'t carrying anything important.'

            elif len(inventory) == 1:
                print 'Your inventory contains a ' + inventory[0]
            else:
                print 'Your inventory contains a ' + ', '.join(inventory[0:-1]) + ', and a ' + inventory[-1]

        # This elif reports on Mr. Meows appearance and general happiness.  It tests for overall happiness and # of pets
        # Could this better be handled by a cat_happiness function to make a less convoluted if-else?
        elif ('look' in action) and (('cat' in action) or ('meow' in action)):
            joy = self.items['cat']['mr_meow_happiness']
            cat_descr = ''
           
            if joy < 5:
                cat_descr = "Mr. Meow is looking pretty crabby."
            elif 5 <= joy <= 10:
                cat_descr = "Mr. Meow is dissatisfied.  What else could make a cat happier?"
            elif 10 < joy <= 19:
                cat_descr = "Mr. Meow is chirping with satisfaction, but something is still missing."
            else:
                cat_descr =  "Mr. Meow is as happy as a cat can be.  All he needs now is a lap in which to curl up."

            if self.items['cat']['pets'] < 5:
                print self.items['cat']['description'] + '\n' + cat_descr + ' He looks like he could use some petting.' + '\n'
            else:
                print self.items['cat']['description'] + '\n' + cat_descr + '\n'

        elif "look" in action:
            things_in_room = self.contents(room)
            inventory = self.contents('inventory')
            

            if any(True for word in commands if word in things_in_room):
                item = [i for i in commands if i in things_in_room][0]
                print self.items[item]['description']
            elif any(True for word in commands if word in inventory):
                item = [i for i in commands if i in inventory]
                print self.items[item]['description'] + '\n' + 'You are carrying the %s.' % item
            else:
                print "There's nothing much to say about thtat."
        
        # Take [item] first checks that the item is in the same room. If true, it then changes the item 'location' property to 'inventory.'    
        elif "take" in action:
            things_in_room = self.contents(room)
            item = [i for i in commands if i in things_in_room][0]
            
            if any(True for word in commands if word in things_in_room):
                if self.items[item]['takeable'] == True:
                    self.items[item]['location'] = 'inventory'
                    print "You take the %s" % item
                else:
                    print "You really don't have a place to put that."
                
            else:
                print "The %s is not in this room." % item

        # Drop [item] first checks that item 'location' property is 'inventory.' If True, it changes the 'item' location to 'room name'   
        elif "drop" in action:
            inventory = self.contents('inventory')
            
            if any(True for word in commands if word in inventory):
                item = [i for i in commands if i in inventory][0]
                self.items[item]['location'] = room
                print "You leave the %s in the %s." % (item, room)
            else:
                print "You don't have one of those."

        elif 'open' in action and ('tuna' in action or 'can' in action):

            if self.items['tuna']['location'] == 'inventory':
                if self.items['tuna']['open']:
                    print "The can is open already.  You wouldn't want Mr. Meow to cut his delicate pink tongue on the edge of the can, would you?"
                elif room == 'kitchen':
                    print 'Mr. Meow\'s ears perk up at the sound of the opening can.  He\'s a finicky kitty, though, and greatly prefers to eat from a bowl.'
                    self.items['tuna']['open'] = True
                else:
                    print 'You should probably wait until you\'re near the food bowl to do that.'
            else:
                print 'You need to take the can of tuna before you can open it.'

        # Only two things can be "put" places: tuna in the cat bowl (in the kitchen) or catnip into the mouse toy.
        elif 'put' in action:

            if ('tuna' in action or 'can' in action) and 'bowl' in action:
                if room != 'kitchen':
                    print 'You should probably be near the food bowl before you try that.'

                elif self.items['tuna']['location'] == 'inventory' and self.items['tuna']['open']:
                    print 'Mr. Meow practically pounces on the food.  He is somehow purring madly while nomming franticaly.  The food vanishes in moments, but your kitty is looking much happier.'
                    self.items['cat']['mr_meow_happiness'] += 5

                else:
                    print 'You need to have an open can of tuna before you can fill Mr. Meow\'s bowl.'

            elif 'catnip' in action:
                if self.items['catnip']['location'] != 'inventory':
                    print 'You need to take the catnip before you can do anything with it.'
                elif self.items['mouse']['location'] != 'inventory':
                    print 'You can\'t do much with the catnip without the toy mouse.  Mr. Meow is much too fancy to enjoy raw nip scattered on the floor.'

                elif 'mouse' in action or 'toy' in action:
                    if self.items['mouse']['status']:
                        print 'The mouse is already fully charged.  Mr. Meow is ready for you to give it to him now.'
                    else:
                        print 'You stuff a bit of catnip into the pouch in the Mr. Mouse toy.  Mr. Meow chirps happily as he sees you preparing his fix.'
                        self.items['mouse']['status'] = True
                else:
                    print 'You probably shouldn\'t do that with catnip.'
            else:
                print 'Putting that in there probably wouldn\'t be a good idea.'

        elif 'give' in action and ('cat' in action or 'meow' in action):
            if ('mouse' in action or 'toy' in action):
                if self.items['mouse']['status']:
                    print 'Mr. Meow pounces on his favorite toy.  He falls on his side, clutching the mouse between his front paws.'
                    print 'He delivers a series of vicious strokes from his hind claws. He appears to huff the sweet essence of nip from the eviscerated mouse.'
                    print 'Mr. Meow is looking much happier than he was.'
                    self.items['cat']['mr_meow_happiness'] += 5
                    self.items['mouse']['location'] = room
                else:
                    print 'Mr. Meow does not look very interested in a mouse toy with no catnip inside.  You pick it back up.  Now where could you have left that nip?'
            elif 'food' in action or 'tuna' in action or 'can' in action:
                print 'Mr. Meow prefers to eat tuna that has been put in his bowl, preferably from an open can.'

            else:
                print 'Mr. Meow doesn\'t look very interested in that.'
        # if use + scoop & in bathroom & garbage bag in inventory
        # if use blanket and sitting in chair & happiness = 20, finish
        # if put & tuna in inventory & bowl in action
        # if give item in inventory, & state = True, happiness +
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
        print "You see a " + ', a '.join(things_in_room[0:-1]) + ' and a ' + things_in_room[-1] + '\n'
        print "You can 'look' at items or the room, you can 'pet' Mr. Meow, you can 'take' items with you.  When you 'go' to the 'kitchen' the game will end.  No other rooms are currently functional."

        action = str.lower(raw_input("What would you like to do next?\n> "))


        while True:
            
            if "look" in action and "room" in action:
                new_things_in_room = self.contents('front_door') 
                print "You see a kitchen, a living room, and further away, the bedroom."
                if len(new_things_in_room) == 0:
                    print "There's nothing much lying around."
                elif len(new_things_in_room) == 1:
                    print "There is a %s here." % new_things_in_room[0]
                else:
                    print "You see a " + ', a '.join(new_things_in_room[0:-1]) + ' and a ' + new_things_in_room[-1] + '.\n'
                action = str.lower(raw_input("What now?\n> "))

            elif ('go' in action or 'open' in action) and ('exit' in action or 'door' in action):
                print 'You would feel terrible leaving while Mr. Meow is unhappy.'
                action = str.lower(raw_input('What now?\n> '))

            elif 'kitchen' in action and 'go' in action:
                print "You walk into the kitchen.  Mr. Meow gets there just before you."
                return 'kitchen'
                break

            elif 'bed' in action and 'go' in action:
                print 'You walk into the bed room.  Mr. Meow heads to the kitchen, before following you, meowing disconsolately.'
                return 'bed_room'
                break

            elif 'living' in action and 'go' in action:
                print 'You walk into the living room, closely followed by the cat.'
                return 'living_room'
                break

            else:
                self.standard_actions(action, 'front_door')
                action = str.lower(raw_input("What now? \n> "))

class LivingRoom(Scene):

    def enter(self):
        things_in_room = self.contents('living_room')

        print "The living room remains much as you left it.  There is a comfy chair in one corner, filled with many happy memories of a very happy Mr. Meow cuddled up on a fuzzy blanket on your lap."
        if len(things_in_room) == 0:
            print "There's nothing much lying around."
        elif len(things_in_room) == 1:
            print "There is a %s here." % things_in_room[0]
        else:
            print "You see a " + ', a '.join(things_in_room[0:-1]) + ' and a ' + things_in_room[-1] + '.\n'

        action = str.lower(raw_input("What now?\n> "))

        while True:
                
            if "look" in action and "room" in action:
                new_things_in_room = self.contents('living_room') 
                print "You see a kitchen, the front door, and further away, the bedroom."
                if len(new_things_in_room) == 0:
                    print "There's nothing much lying around."
                elif len(new_things_in_room) == 1:
                    print "There is a %s here." % new_things_in_room[0]
                else:
                    print "You see a " + ', a '.join(new_things_in_room[0:-1]) + ' and a ' + new_things_in_room[-1] + '.\n'
                action = str.lower(raw_input("What now?\n> "))

            elif 'sit' in action and 'chair' in action:
                if self.items['blanket']['location'] == 'inventory':
                    if self.items['cat']['mr_meow_happiness'] >= 20:
                        print 'You sit in the chair and spread the blanket over your lap.  Mr. Meow hops up onto your lap.'
                        return 'finished'
                        break
                    else:
                        print 'You could sit down, but Mr. Meow keeps trying to lead you somewhere.  What could you have forgotten?'
                        action = str.lower(raw_input("What now?\n> "))
                else:
                    print 'You\'re about to sit down in the comfy chair when you realize you\'ve misplaced the fuzzy blanket!  Where could it be?'
                    action = str.lower(raw_input("What now?\n> "))

            elif 'kitchen' in action and 'go' in action:
                print "You walk into the kitchen.  Mr. Meow gets there just before you."
                return 'kitchen'
                break

            elif 'bed' in action and 'go' in action:
                print 'You walk into the bed room.  Mr. Meow heads to the kitchen, before following you, meowing disconsolately.'
                return 'bed_room'
                break

            elif 'front_door' in action and 'go' in action:
                print 'You walk into the living room, closely followed by the cat.'
                return 'front_door'
                break

            else:
                self.standard_actions(action, 'living_room')
                action = str.lower(raw_input("What now? \n> "))    

class Kitchen(Scene):
    def enter(self):

        print "The kitchen is typical of most apartment kitchens.  There are appliances and storage areas and a sink."
        
        if len(things_in_room) == 0:
            print "There's nothing much lying around."
        elif len(things_in_room) == 1:
            print "There is a %s here." % things_in_room[0]
        else:
            print "You see a " + ', a '.join(things_in_room[0:-1]) + ' and a ' + things_in_room[-1] + '.\n'

        action = str.lower(raw_input("What now?\n> "))

        while True:
                
            if "look" in action and "room" in action:
                new_things_in_room = self.contents('kitchen') 
                print "You see the front door, the living room, and further away, the bedroom."
                if len(new_things_in_room) == 0:
                    print "There's nothing much lying around."
                elif len(new_things_in_room) == 1:
                    print "There is a %s here." % new_things_in_room[0]
                else:
                    print "You see a " + ', a '.join(new_things_in_room[0:-1]) + ' and a ' + new_things_in_room[-1] + '.\n'
                action = str.lower(raw_input("What now?\n> "))

            elif 'front_door' in action and 'go' in action:
                print "You walk to the front door.  Mr. Meow gets there just before you."
                return 'front_door'
                break

            elif 'bed' in action and 'go' in action:
                print 'You walk into the bed room.  Mr. Meow heads to the kitchen, before following you, meowing disconsolately.'
                return 'bed_room'
                break

            elif 'living' in action and 'go' in action:
                print 'You walk into the living room, closely followed by the cat.'
                return 'living_room'
                break

            else:
                self.standard_actions(action, 'front_door')
                action = str.lower(raw_input("What now? \n> "))       

class BedRoom(Scene):
    pass

class BathRoom(Scene):
    pass


class Map(object):

    scenes = {
        'front_door': FrontDoor(),
        'living_room': LivingRoom(),
        'kitchen': Kitchen(),
        'bed_room': BedRoom(),
        'bath_room': BathRoom(),
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
