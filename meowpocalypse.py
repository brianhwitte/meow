from sys import exit
from random import randint

inventory = []
character = {
    'inventory': inventory,
    'life': 10,
    'armor': 0
}

room_contents = {
    "room1": [],
    "room2": []
}

class Scene(object):
    def enter(self):
        print "some stuff happens"
        exit(1)

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

class Map(object):

    scenes = {

        'living_room': LivingRoom(),
        'kitchen': Kitchen(),
        'bed_room': BedRoom()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val