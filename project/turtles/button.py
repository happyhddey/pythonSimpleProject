import pygame
import sys
from constant import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)

font = pygame.font.SysFont("arial", 30, True, True)

class Rectangle:

    def __init__(self, pos=(0, 0), size=(50, 50), color=BLACK, text="", value=""):
        self.pos = pos
        self.size = size
        self.color = color
        self.text = text
        self.value = value
    
    def draw(self, pos=None):
        pyrect = None
        w, h = self.size
        if pos != None:
            x, y = pos
        else:
            x, y = self.pos
        pyrect = pygame.Rect(x-w//2, y-h//2, w, h)
        pygame.draw.rect(screen, self.color, pyrect, 2)
        text = font.render(self.text, True, self.color)
        screen.blit(text, (x-10, y-15))

    def is_clicked(self, pos):
        event_x, event_y = pos
        x, y = self.pos
        w, h = self.size
        return ((x-w//2 <= event_x <= x+w//2) and (y-h//2 <= event_y <= y+h//2))

    def get_value(self):
        return self.value


def draw_circle(pos, size=50):
    # default position
    x, y = size//2, size//2
    # draw circle
    x, y = pos
    r = size // 2
    pygame.draw.circle(screen, BLACK, [x, y], r)

def draw_triangle(pos, size=50):
    # default position
    x, y = size//2, size//2
    # draw triangle
    x, y = pos
    half_width = size // 2
    one_third_height = size // 2 * 0.58
    pygame.draw.polygon(screen, BLACK, [[x-half_width, y+one_third_height], [x+half_width, y+one_third_height], [x, y-one_third_height*2]])






polygon_type = "C"

screen.fill(WHITE)

center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250)
button_infos = [((0, -80), "U"), ((0, 80), "D"), ((-100, 0), "L"), ((100, 0), "R")]
buttons = []
for b in button_infos:
    pos, val = b
    x, y = pos
    c_x, c_y = center
    button = Rectangle(pos=(c_x+x, c_y+y), text=val, value=val)
    buttons.append(button)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                # draw_circle(pos)
                for b in buttons:
                    if b.is_clicked(pos):
                        print(b.get_value())
                        break
            if event.button == 3:
                new_button = Rectangle()
                new_button.draw(pos)
    
    for b in buttons:
        b.draw()
    pygame.display.update()
    

        
