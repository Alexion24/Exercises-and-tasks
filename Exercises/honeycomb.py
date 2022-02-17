import turtle
turtle.speed(5)
turtle.Screen().addshape(r'C:\Users\alex2\Desktop\Pictures\DogePet.gif')  # регистрируем изображение
turtle.shape(r'C:\Users\alex2\Desktop\Pictures\DogePet.gif')

def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)


def bees_things(side):
    hexagon(side)
    turtle.setheading(240)
    hexagon(side)
    turtle.setheading(0)
    turtle.forward(side)
    turtle.setheading(300)
    hexagon(side)
    turtle.setheading(60)
    turtle.forward(side)
    turtle.setheading(0)
    hexagon(side)
    turtle.setheading(120)
    turtle.forward(side)
    turtle.setheading(60)
    hexagon(side)
    turtle.setheading(180)
    turtle.forward(side)
    turtle.setheading(120)
    hexagon(side)
    turtle.setheading(240)
    turtle.forward(side)
    turtle.setheading(180)
    hexagon(side)
    turtle.setheading(300)
    turtle.forward(side)


bees_things(100)

# import turtle as t
#
# def hexagon(side):
#     t.shape('turtle')
#     for _ in range(6):
#         t.forward(side)
#         t.left(60)
#     t.forward(side)
#     t.right(60)
#
#
# for _ in range(6):
#     hexagon(50)
