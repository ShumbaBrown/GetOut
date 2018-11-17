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

            spr.position = 880 , 260
            spr.scale = 1

            self.add(spr, z = 10)

class Sprite2(cocos.sprite.Sprite):
    def __init__(self):
        super(Sprite2, self).__init__("hauntedhouse2.png")
        self.position = 640, 400

class Sprite3(cocos.layer.Layer):
    def __init__(self):
            super(Sprite3, self).__init__()

            spr3 = cocos.sprite.Sprite("GreenDoor.png")

            spr3.position = 800 , 460
            spr3.scale = 1.25

            self.add(spr3, z = 10)

class Sprite4(cocos.layer.Layer):
    def __init__(self):
            super(Sprite4, self).__init__()

            spr4 = cocos.sprite.Sprite("YellowDoor.png")

            spr4.position = 500 , 300
            spr4.scale = 1

            self.add(spr4, z = 10)

class Sprite5(cocos.layer.Layer):
    def __init__(self):
            super(Sprite5, self).__init__()

            spr4 = cocos.sprite.Sprite("BlueDoor.png")

            spr4.position = 150 , 300
            spr4.scale = 1.5

            self.add(spr4, z = 10)

class Sprite6(cocos.layer.Layer):
    def __init__(self):
            super(Sprite6, self).__init__()

            spr6 = cocos.sprite.Sprite("PinkDoor.png")

            spr6.position = 1100, 300
            spr6.scale = 1.5

            self.add(spr6, z = 10)

class Sprite7(cocos.layer.Layer):
    def __init__(self):
            super(Sprite7, self).__init__()

            spr7 = cocos.sprite.Sprite("WhiteDoor.png")

            spr7.position = 690, 310
            spr7.scale = 0.75

            self.add(spr7, z = 10)

class Sprite8(cocos.layer.Layer):
    def __init__(self):
            super(Sprite8, self).__init__()

            spr8 = cocos.sprite.Sprite("BrownDoor.png")

            spr8.position = 360, 260

            spr8.scale = 1

            self.add(spr8, z = 10)

##########Defined the blinking actions #############
def Blink(times, duration):
    return (
        Hide() + Delay(duration/(times*2)) +
        Show() + Delay(duration/(times*2))
    ) * times


class FadeOut( IntervalAction ):
    def init( self, duration ):
        self.duration = duration

    def update( self, t ):
        self.target.opacity = 255 * (1-t)

    def __reversed__(self):
        return FadeIn( self.duration )


if __name__ == "__main__":
                director.init(width=1280, height = 920, caption="my cocos window")
                director.window.pop_handlers()
                spr1_layer = Sprite1()#red
                spr2_layer = Sprite2()
                # spr3_layer = Sprite3()#green
                spr4_layer = Sprite4()#yellow
                spr5_layer = Sprite5()#blue
                spr6_layer = Sprite6()#pink
                spr7_layer = Sprite7()#white
                spr8_layer = Sprite8()#/brown

                # spr2_layer.do( Twirl( grid=(1,3), duration=4) )
                #  spr3_layer.do( Lens3D( grid=(6,2), duration=4) + Liquid( grid=(6,2), duration=1 ) )
                spr4_layer.do( Waves( grid=(6,12), duration=4) + Liquid( grid=(16,12), duration=5 ) )
                spr6_layer.do( Waves( grid=(6,12), duration=4) + Liquid( grid=(16,12), duration=5 ) )
                spr5_layer.do( Waves( grid=(6,12), duration=4) + Liquid( grid=(16,12), duration=5 ) )
                spr2_layer.do( Waves( grid=(6,2), duration=4) + Liquid( grid=(6,2), duration=1 ) )
                spr8_layer.do( Twirl( grid=(4,2), duration=4) )
                spr1_layer.do( Twirl( grid=(4,2), duration=4) )
                spr7_layer.do(Blink(3,6))



                test_scene = cocos.scene.Scene();
                test_scene.add(spr1_layer, z = 2)
                # test_scene.add(spr3_layer, z = 2)
                test_scene.add(spr4_layer, z = 2)
                test_scene.add(spr5_layer, z = 3)
                test_scene.add(spr6_layer, z = 3)
                test_scene.add(spr7_layer, z = 3)
                test_scene.add(spr8_layer, z = 2)



                test_scene.add(spr2_layer, z = 0)

                director.run(test_scene)
