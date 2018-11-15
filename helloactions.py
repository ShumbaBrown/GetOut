import cocos
import pyglet
from cocos.actions import *
from cocos.director import director
from pyglet.gl import *
from cocos.layer import ColorLayer
from cocos.sprite import Sprite
from pyglet.window import key
from cocos.scenes import *

class IntroScene(cocos.scene.Scene):
    def __init__(self):
        super(IntroScene, self).__init__()
        label1 = cocos.text.Label(
                "Try to Get Out! Press Space to restart",  font_name= 'Times New Roman', font_size=32,
                anchor_x = "center", anchor_y = "center"
                )
        label1.position = 540, 60
        self.add(ColorLayer(240, 50, 50, 180))
        self.add(label1)
        self.add(SceneControlLayer())

class TestScene1(cocos.scene.Scene):
    def __init__(self):
        super(TestScene1, self).__init__()
        label1 = cocos.text.Label(
                "Try to Get Out! Press Space to restart",  font_name= 'Times New Roman', font_size=32,
                anchor_x = "center", anchor_y = "center"
                )
        label1.position = 540, 60
        self.add(ColorLayer(240, 50, 50, 180))
        self.add(label1)
        self.add(SceneControlLayer())

class HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):
        #blueish Color
        super(HelloWorld, self).__init__(104,764,224,155)

        label = cocos.text.Label('GetOut',
            font_name='Times New Roman',
            font_size=32)
            # anchor_x='center', anchor_y='center')
        #set the label in the center of the screen
        label.position = 620, 240
        self.add(label)
        #add a Sprite

        sprite = cocos.sprite.Sprite('logo.jpeg')
        sprite.position = 700, 650
        sprite.scale = 1
        self.add(sprite, z = 10)
        scale = ScaleBy(3.5, duration = 2)

        label.do(Repeat(scale + Reverse(scale)))
        sprite.do(Repeat(Reverse(scale) + scale))

class SceneControlLayer(cocos.layer.Layer):
    is_event_handler = True
    space_counter = 1 #numTimes space key is pressed
    active_scene = None
    def __init__(self):
        super(SceneControlLayer, self).__init__()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE and SceneControlLayer.space_counter == 0:
            SceneControlLayer.active_scene = HelloWorld()
            director.replace(FlipX3DTransition(SceneControlLayer.active_scene, duration = 2))

        if symbol == key.SPACE and SceneControlLayer.space_counter == 1:
            SceneControlLayer.active_scene = TestScene1()
            director.replace(FlipX3DTransition(SceneControlLayer.active_scene, duration = 2))

        if symbol == key.SPACE and SceneControlLayer.space_counter == 2:
            SceneControlLayer.active_scene = TestScene1()
            director.replace(FlipX3DTransition(SceneControlLayer.active_scene, duration = 2))

        if symbol == key.SPACE and SceneControlLayer.space_counter == 3:
            SceneControlLayer.active_scene = TestScene1()
            director.replace(FlipX3DTransition(SceneControlLayer.active_scene, duration = 2))
            SceneControlLayer.space_counter = 0
        SceneControlLayer.space_counter += 1
# cocos.director.director.init()
director.init(width=1280, height = 720, caption="my cocos window")
director.window.pop_handlers()

hello_layer = HelloWorld()
hello_layer.do(RotateBy(360, duration = 5))
main_scene = cocos.scene.Scene(hello_layer)
cocos.director.director.run(main_scene)

SceneControlLayer.active_scene = HelloWorld()
director.run(SceneControlLayer.active_scene)
cc.director.popScene()
#load a new scene
cc.director.loadScene(IntroScene)
SceneControlLayer.active_scene = IntroScene()
director.run(SceneControlLayer.active_scene)
