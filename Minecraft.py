# This game is for enjoying, however if you want to know how I did it, here you go
'''First, we used a package called ursina and from it we imported FirstPersonController which is the package needed for movement of the player
Then we assigned the app variable to ursina() and player to FirstPersonController() and created a sky which was available in ursina engine'''
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
Sky()
''' Then we created used for loop to create the minecraft setup and set the parameters of the box like color, model, position, texture, parent and origin'''
boxes = []
for i in range(20):
    for j in range(20):
        box = Button(color=color.white, model='cube', position=(j,0,i), texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(box)
''' Then we defined a input key that is there in default for movement, you can use W,A,S,D keys then used for loop and under it we placed conditions like if left mouse
is clicked then boxes will add and if right mouse is clicked then boxes will remove'''
def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal, texture='grass.png', parent=scene, origin_y=0.5)
                boxes.append(new)
            if key == 'right mouse down':
                boxes.remove(box)
                destroy(box)
''' Then all you need is add app.run() and click the program and enjoy the game'''

app.run()


