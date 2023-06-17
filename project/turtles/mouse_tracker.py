import turtle as t
import math
import time

"""
화면을 마우스로 클릭하면 거북이가 그 방향으로 움직입니다.
"""



# screen 만들기
screen = t.Screen()
screen.bgcolor("white")
screen.tracer(2)



# pen 만들기
mypen = t.Turtle()
mypen.penup()
mypen.setposition(-300, 300)
mypen.pendown()
mypen.pensize(3)

for x in range(4):
    mypen.forward(600)
    mypen.right(90)

mypen.hideturtle()



# 거북이 만들기
turtle = t.Turtle()
turtle.shape("turtle")
turtle_size = 1
turtle.turtlesize(turtle_size,turtle_size)
turtle.color("black")
turtle.penup()
turtle_speed = 1



# click했을 때(click 이벤트 때) 어떤 일을 정하기
def turnDirection(mouse_x, mouse_y):
    print(f'x:{mouse_x}, y:{mouse_y}')
    print("clicked")
    turtle_x, turtle_y = turtle.pos()
    delta_x, delta_y = mouse_x - turtle_x, mouse_y - turtle_y
    radian = math.atan2(delta_y, delta_x)
    degree = (180 / math.pi) * radian       # x rad = 180/pi * x deg
    turtle.setheading(degree)
    pass

screen.onclick(turnDirection)



# 게임 실행
screen.listen()
 
while True:
    turtle.forward(turtle_speed)
    time.sleep(0.01)
    
