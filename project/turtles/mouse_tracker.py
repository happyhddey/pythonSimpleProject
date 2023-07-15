import turtle as t
import math
import time

"""
화면을 마우스로 클릭하면 거북이가 그 방향으로 움직입니다.
과제를 순서대로 해결해봅시다.
1번 과제: 정사각형 상자 밖을 클릭했을 때는 아무 일도 일어나지 않도록 수정해주세요.
2번 과제: 거북이가 정사각형 상자 벽면에 부딪혔을 때 튕겨나오도록 수정해주세요.
    2-1. 들어간 방향과 정반대로 튕겨나오도록 수정해주세요.
    2-2. 빛이 반사되는 것처럼 거북이가 튕기도록 해주세요.
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
    # mouse_x와 mouse_y에는 각각 마우스로 클릭한 곳의 x와 y 좌표가 들어있습니다.
    print(f'x:{mouse_x}, y:{mouse_y}')

    # ####################### 1번 과제 #######################
    # 정사각형 상자 밖을 클릭했을 때는 아무 일도 일어나지 않도록 수정해주세요.
    
    # 이 아래는 마우스를 클릭한 곳으로 거북이의 머리 방향을 바꾸어주는 코드입니다.
    turtle_x, turtle_y = turtle.pos()
    delta_x, delta_y = mouse_x - turtle_x, mouse_y - turtle_y
    radian = math.atan2(delta_y, delta_x)
    degree = (180 / math.pi) * radian       # x rad = 180/pi * x deg
    turtle.setheading(degree)

screen.onclick(turnDirection)



# 게임 실행
screen.listen()
 
while True:
    turtle.forward(turtle_speed)

    # ####################### 2번 과제 #######################
    # 거북이가 정사각형 상자 벽면에 부딪혔을 때 튕겨나오도록 수정해주세요.
    # 2-1. 부딪힌 벽에 수직으로 튕겨나오도록 수정해주세요.
    #      (1) 거북이가 위쪽 벽에 부딪히면 거북이의 머리를 남쪽으로 바꾸어주세요.
    #      (2) 거북이가 아래쪽 벽에 부딪히면 거북이의 머리를 ?쪽으로 바꾸어주세요. (?에 들어갈 방향은 직접 생각해보세요.)
    #      (3) 거북이가 오른쪽 벽에 부딪히면 거북이의 머리를 ?쪽으로 바꾸어주세요. (?에 들어갈 방향은 직접 생각해보세요.)
    #      (4) 거북이가 왼쪽 벽에 부딪히면 거북이의 머리를 ?쪽으로 바꾸어주세요. (?에 들어갈 방향은 직접 생각해보세요.)
    # 2-2. 빛이 반사되는 것처럼(입사각과 반사각이 같도록) 거북이가 튕기도록 해주세요.
    
    # 여기 아래에 코드를 작성합니다.
    
    time.sleep(0.01)
    
