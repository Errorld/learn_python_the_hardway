from sys import exit
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
        pass

class scene(object):
    pass
class a(scene):
    def enter(self):
        print "entered a"
        raw_input('> ')
        return 'b'
class b(scene):
    def enter(self):
        print "entered b"
        raw_input('> ')
        return 'finished'
class finished(scene):
    def enter(self):
        print "entered finished"
        exit(0)

class Map(object):
    scenes= {
        'a':a(),
        'b':b(),
        'finished':finished()
        }
    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    pass

a_map = Map('a')
engine = Engine(a_map)
engine.play()
