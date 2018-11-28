import cocos
import pyglet
from cocos.actions import *
from cocos.director import director
from pyglet.gl import *
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.sprite import Sprite
from pyglet.window import key

class IntroSceneLayer(cocos.layer.Layer):
    
    is_event_handler = True
    space_counter = 1
    def __init__(self):
        
        super(IntroSceneLayer, self).__init__()

        spr = cocos.sprite.Sprite("logo.jpeg")

        spr.position = 640 , 400
        spr.scale = 1

        self.add(spr, z = 10)
                
        introtextLabel = cocos.text.Label(
                        "Press Space to start",  font_name= 'Times New Roman', font_size=32,
                        anchor_x = "center", anchor_y = "center")
        introtextLabel.position = 620, 60
        self.add(introtextLabel)
                
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            director.replace(Scene(FloorPlanLayer()))
                

class FloorPlanLayer(cocos.layer.Layer):
    is_event_handler = True
    
    def __init__(self):
        super(FloorPlanLayer, self).__init__()
        
        floorPlanSprite = cocos.sprite.Sprite("Rooms/FloorPlan.png")
        floorPlanSprite.scale = 1
        self.position = 640, 400
        self.add(floorPlanSprite)
        
        floorPlanTL = cocos.text.Label(
                        "There are 7 rooms in the House. Can you escape? Press Space to start",  font_name= 'Times New Roman', font_size=25,
                        anchor_x = "center", anchor_y = "bottom", color = (0,0,0,255))
        floorPlanTL.position = -100 , -305
        self.add(floorPlanTL, z = 2)
        
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            print("space was pressed in floor plan")
            director.replace(LivingRoomScene())
            
class LivingRoomScene(cocos.scene.Scene):
    def __init__(self, *args, **kwargs):
        super(LivingRoomScene, self).__init__()
        
        spr1_layer = Sprite1()#red
        spr2_layer = Sprite2()#living room 
        spr4_layer = Sprite4()#yellow
        spr5_layer = Sprite5()#blue
        spr6_layer = Sprite6()#pink
        spr7_layer = Sprite7()#white
        spr8_layer = Sprite8()#/brown
        transition_scene = TransitionScene()

                        
        self.add(spr1_layer, z = 2)
        self.add(spr2_layer, z = 0)
        self.add(spr4_layer, z = 2)
        self.add(spr5_layer, z = 3)
        self.add(spr6_layer, z = 3)
        self.add(spr7_layer, z = 3)
        self.add(spr8_layer, z = 2)
                
# Living room scene:
class LivingRoomLayer(cocos.layer.Layer):
    is_event_handler = True
    
    def __init__(self):
        super(LivingRoomLayer, self).__init__()
        
        LRspr = cocos.sprite.Sprite("Rooms/LivingRoom.png")
        LRspr.scale = 1
        self.position = 640, 400
        self.add(LRspr, z = 0)
        
        
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
        
        # RDspr = cocos.sprite.Sprite("Doors/RedDoor.png")
  #
  #       RDspr.position = 900 , 260
  #       RDspr.scale = 1
  #
  #       self.add(RDspr, z = 2)
  #
  #       self.RDspriteHeight = RDspr.height
  #       print("sprite height: ", self.spriteHeight) #356
  #       self.RDspriteWidth = RDspr.width
  #       print("sprite width: ", self.spriteWidth) #154
        
        # BRspr = cocos.sprite.Sprite("Rooms/Bedroom.png")
#
#         BRspr.scale = 1
#         BRspr.position = 640, 400
#
#         self.add(BRspr, z = 2)
        
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
        # print("self.mouseY + self.spriteHeight: ", self.mouseY + self.spriteHeight)
        if(self.mouseX >= 400 and self.mouseX <= 490 
            and self.mouseY>=40 and self.mouseY <= 218):
            director.replace(Scene(TransitionScene()))
        



        
            
# #
# class TransitionScene(cocos.layer.Layer):
#     def __init__(self):
#         super(TransitionScene, self).__init__()
#
#
#
# class Sprite4(cocos.layer.Layer):
#     def __init__(self):
#             super(Sprite4, self).__init__()
#
#             spr4 = cocos.sprite.Sprite("Doors/YellowDoor.png")
#
#             spr4.position = 560 , 300
#             spr4.scale = 1
#
#             self.add(spr4, z = 10)
#
# class Sprite5(cocos.layer.Layer):
#     def __init__(self):
#             super(Sprite5, self).__init__()
#
#             spr4 = cocos.sprite.Sprite("Doors/GreenDoor.png")
#
#             spr4.position = 150 , 300
#             spr4.scale = 1.5
#
#             self.add(spr4, z = 10)
#
# class Sprite6(cocos.layer.Layer):
#     def __init__(self):
#             super(Sprite6, self).__init__()
#
#             spr6 = cocos.sprite.Sprite("Doors/PinkDoor.png")
#
#             spr6.position = 1135, 300
#             spr6.scale = 1.5
#
#             self.add(spr6, z = 10)
#
# class Sprite7(cocos.layer.Layer):
#     def __init__(self):
#             super(Sprite7, self).__init__()
#
#             spr7 = cocos.sprite.Sprite("Doors/WhiteDoor.png")
#
#             spr7.position = 740, 310
#             spr7.scale = 0.75
#
#             self.add(spr7, z = 10)
#
# class Sprite8(cocos.layer.Layer):
#     def __init__(self):
#             super(Sprite8, self).__init__()
#
#             spr8 = cocos.sprite.Sprite("Doors/BrownDoor.png")
#
#             spr8.position = 380, 260
#
#             spr8.scale = 1
#
#             self.add(spr8, z = 10)

# if __name__ == "__main__":
#                 director.init(width=1280, height = 920, caption="my cocos window")
#                 director.window.pop_handlers()
#
#                 transition_scene = TransitionScene()
#
#                 test_scene = cocos.scene.Scene();
#
#
#                 director.run(test_scene)
#
if __name__ == "__main__":
                director.init(width=1280, height = 920, caption="my cocos window")
                director.window.pop_handlers()
                
                introSceneLayer = IntroSceneLayer()
                
                introScene = cocos.scene.Scene()
                introScene.add(introSceneLayer, z = 0)
                
                # livingRoomScene = cocos.scene.Scene()
#                 livingRoomLayer =LivingRoomLayer()
#                 spr1_layer = Sprite1()#red
#                 spr4_layer = Sprite4()#yellow
#                 spr5_layer = Sprite5()#blue
#                 spr6_layer = Sprite6()#pink
#                 spr7_layer = Sprite7()#white
#                 spr8_layer = Sprite8()#/brown
#
#                 livingRoomScene.add(livingRoomLayer, z = 0)
#                 livingRoomScene.add(spr1_layer, z = 2)
#                 livingRoomScene.add(spr4_layer, z = 2)
#                 livingRoomScene.add(spr5_layer, z = 3)
#                 livingRoomScene.add(spr6_layer, z = 3)
#                 livingRoomScene.add(spr7_layer, z = 3)
#                 livingRoomScene.add(spr8_layer, z = 2)
                
                director.run(introScene)
                # director.push(livingRoomScene)
            