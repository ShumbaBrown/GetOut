import cocos
import pyglet
from cocos.actions import *
from cocos.director import director
from pyglet.gl import *
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite
from pyglet.window import key
import cocos.euclid as eu
import cocos.collision_model as cm

class Sprite1(cocos.layer.Layer):
    is_event_handler = True
    
    def __init__(self):
            super(Sprite1, self).__init__()

            spr = cocos.sprite.Sprite("Doors/RedDoor.png")

            spr.position = 900 , 260
            spr.scale = 1

            self.add(spr, z = 10)
            
            self.spriteHeight = spr.height
            print("sprite height: ", self.spriteHeight) #356
            self.spriteWidth = spr.width
            print("sprite width: ", self.spriteWidth) #154
            
            # self.collision_manager = CollisionManager()
            # self.collision_manager.add(self.spr)
            
    def on_mouse_motion (self, x, y, dx, dy):
        """Called when the mouse moves over the app window with no button pressed

        (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        """
        self.mouseX = x
        # print("mouseX: ", self.mouseX)
        self.mouseY = y
        # print("mouseY: ", self.mouseY)

    def on_mouse_press(self, x, y, buttons, modifiers):
        # print("self.mouseX + self.spriteWidth: ", self.mouseX + self.spriteWidth)
#         print("self.mouseY + self.spriteHeight: ", self.mouseY + self.spriteHeight)
        if(self.mouseX >= 400 and self.mouseX <= 490 
            and self.mouseY>=40 and self.mouseY <= 218):
            director.replace(Scene(TransitionScene()))
        
            
#
class TransitionScene(cocos.layer.Layer):
    def __init__(self):
        super(TransitionScene, self).__init__()

        spr1 = cocos.sprite.Sprite("Rooms/Bedroom.png")

        spr1.scale = 1
        self.position = 640, 400

        self.add(spr1)
        
class Sprite2(cocos.sprite.Sprite):
    def __init__(self):
        super(Sprite2, self).__init__("Rooms/LivingRoom.png")
        self.position = 640, 400


class Sprite4(cocos.layer.Layer):
    def __init__(self):
            super(Sprite4, self).__init__()

            spr4 = cocos.sprite.Sprite("Doors/YellowDoor.png")

            spr4.position = 560 , 300
            spr4.scale = 1

            self.add(spr4, z = 10)

class Sprite5(cocos.layer.Layer):
    def __init__(self):
            super(Sprite5, self).__init__()

            spr4 = cocos.sprite.Sprite("Doors/GreenDoor.png")

            spr4.position = 150 , 300
            spr4.scale = 1.5

            self.add(spr4, z = 10)

class Sprite6(cocos.layer.Layer):
    def __init__(self):
            super(Sprite6, self).__init__()

            spr6 = cocos.sprite.Sprite("Doors/PinkDoor.png")

            spr6.position = 1135, 300
            spr6.scale = 1.5

            self.add(spr6, z = 10)

class Sprite7(cocos.layer.Layer):
    def __init__(self):
            super(Sprite7, self).__init__()

            spr7 = cocos.sprite.Sprite("Doors/WhiteDoor.png")

            spr7.position = 740, 310
            spr7.scale = 0.75

            self.add(spr7, z = 10)

class Sprite8(cocos.layer.Layer):
    def __init__(self):
            super(Sprite8, self).__init__()

            spr8 = cocos.sprite.Sprite("Doors/BrownDoor.png")

            spr8.position = 380, 260

            spr8.scale = 1

            self.add(spr8, z = 10)

if __name__ == "__main__":
                director.init(width=1280, height = 920, caption="my cocos window")
                director.window.pop_handlers()
                spr1_layer = Sprite1()#red
                spr2_layer = Sprite2()
                spr4_layer = Sprite4()#yellow
                spr5_layer = Sprite5()#blue
                spr6_layer = Sprite6()#pink
                spr7_layer = Sprite7()#white
                spr8_layer = Sprite8()#/brown
                transition_scene = TransitionScene()

                test_scene = cocos.scene.Scene();
                test_scene.add(spr1_layer, z = 2)
                test_scene.add(spr4_layer, z = 2)
                test_scene.add(spr5_layer, z = 3)
                test_scene.add(spr6_layer, z = 3)
                test_scene.add(spr7_layer, z = 3)
                test_scene.add(spr8_layer, z = 2)
                test_scene.add(transition_scene)
                test_scene.add(spr2_layer, z = 0)

                director.run(test_scene)