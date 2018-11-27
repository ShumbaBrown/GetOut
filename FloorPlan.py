import cocos
import pyglet
from cocos.scene import Scene
from cocos.actions import *
from cocos.director import director
from pyglet.gl import *
from cocos.layer import Layer,ColorLayer
from cocos.sprite import Sprite
from pyglet.window import key
from cocos.scenes import *
import cocos.euclid as eu
import cocos.collision_model as cm

class FloorPlanSprite(cocos.sprite.Sprite):
    def __init__(self):
        super(FloorPlanSprite, self).__init__("Rooms/FloorPlan.png")
        self.position = 640, 400

if __name__ == "__main__":
                director.init(width=1280, height = 920, caption="my cocos window")
                director.window.pop_handlers()
                
                spr1_layer = FloorPlanSprite()

                test_scene = cocos.scene.Scene();
                test_scene.add(spr1_layer, z = 0) # background sprite

                director.run(test_scene)
