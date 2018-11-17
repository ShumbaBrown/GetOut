import cocos
import pyglet
from cocos.actions import *
from cocos.director import director
from pyglet.gl import *
from cocos.layer import ColorLayer
from cocos.sprite import Sprite
from pyglet.window import key
from cocos.scenes import *

class Sprite1(cocos.layer.Layer):
    def __init__(self):
            super(Sprite1, self).__init__()

            spr = cocos.sprite.Sprite("RedDoor.png")

            spr.position = 1100 , 360
            spr.scale = 1

            self.add(spr, z = 10)

class Sprite2(cocos.sprite.Sprite):
    def __init__(self):
        super(Sprite2, self).__init__("hauntedhouse.png")
        self.position = 640, 400

class Sprite3(cocos.layer.Layer):
    def __init__(self):
            super(Sprite3, self).__init__()

            spr3 = cocos.sprite.Sprite("GreenDoor.png")

            spr3.position = 800 , 360
            spr3.scale = 1

            self.add(spr3, z = 10)

class Sprite4(cocos.layer.Layer):
    def __init__(self):
            super(Sprite4, self).__init__()

            spr4 = cocos.sprite.Sprite("YellowDoor.png")

            spr4.position = 500 , 360
            spr4.scale = 1

            self.add(spr4, z = 10)

class Sprite5(cocos.layer.Layer):
    def __init__(self):
            super(Sprite5, self).__init__()

            spr4 = cocos.sprite.Sprite("BlueDoor.png")

            spr4.position = 200 , 360
            spr4.scale = 1

            self.add(spr4, z = 10)

if __name__ == "__main__":
                director.init(width=1280, height = 920, caption="my cocos window")
                director.window.pop_handlers()
                spr1_layer = Sprite1()
                spr2_layer = Sprite2()
                spr3_layer = Sprite3()
                spr4_layer = Sprite4()
                spr5_layer = Sprite5()
                spr2_layer.do(RotateBy(360, duration = 2))
                test_scene = cocos.scene.Scene();
                test_scene.add(spr1_layer, z = 3)
                test_scene.add(spr3_layer, z = 3)
                test_scene.add(spr4_layer, z = 4)
                test_scene.add(spr5_layer, z = 3)
                test_scene.add(spr2_layer, z = 0)

                director.run(test_scene)
