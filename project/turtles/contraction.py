import pygame
import sys
import time
import random
from color import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)

FONT_LARGE_SIZE = 100
FONT_SMALL_SIZE = 30
font_large = pygame.font.SysFont("malgungothic", FONT_LARGE_SIZE)
font_small = pygame.font.SysFont("malgungothic", FONT_SMALL_SIZE)



class Rectangle:

    def __init__(self, pos=(0, 0), size=(100, 50)):
        self.pos = pos
        self.size = size
        self.text = None
    
    def set_text(self, text):
        self.text = text
    
    def draw(self, font_color=BLACK, bg_color=WHITE):
        x, y = self.pos
        w, h = self.size
        pyrect = pygame.Rect(x-w//2, y-h//2, w, h)
        pygame.draw.rect(screen, bg_color, pyrect)
        pygame.draw.rect(screen, font_color, pyrect, 2)
        text = font_small.render(self.text, True, font_color)
        screen.blit(text, (x-FONT_SMALL_SIZE, y-FONT_SMALL_SIZE//3*2))

    def is_hovering(self, pos):
        event_x, event_y = pos
        x, y = self.pos
        w, h = self.size
        return ((x-w//2 <= event_x <= x+w//2) and (y-h//2 <= event_y <= y+h//2))

    def get_text(self):
        return self.text



def make_question():
    sample_colors = random.sample(color_list, 4)
    samples = list(map(lambda c:c[1], sample_colors))
    question_colors = random.sample(sample_colors, 2)
    answer, dummy_text = question_colors
    return answer, dummy_text[1], samples



buttons = []
button_box_center = (400, 700)
start = -3
half = 60
for i in range(4):
    bc_x, bc_y = button_box_center
    button = Rectangle(pos=(bc_x + (start+2*i)*half, bc_y))
    buttons.append(button)


TIME_LIMIT = 3000

class Game_Setter:
    def __init__(self):
        self.time_limit = None
        self.answer_text = None
        self.texts = None
        self.score = 0
        self.end = False

    def update_score(self):
        self.score += 1

    def set_new_game(self, answer_text, texts):
        self.answer_text = answer_text
        self.texts = texts
        for i in range(4):
            buttons[i].set_text(texts[i])
        time_limit = max(1000, TIME_LIMIT - self.score * 50)
        self.time_limit = pygame.time.get_ticks() + time_limit
        print(time_limit)

    def is_answer(self, text):
        return self.answer_text == text

    def is_time_over(self):
        current_time = pygame.time.get_ticks()
        return current_time > self.time_limit

    def get_score(self):
        return self.score
    
     
    




def write_text(text, color):
    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    text = font_large.render(text, True, color)
    screen.blit(text, (x-FONT_LARGE_SIZE, y-FONT_LARGE_SIZE))


def write_score(text):
    x, y = SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.1
    text = font_small.render(str(text), True, BLACK)
    screen.blit(text, (x, y))


screen.fill(WHITE)
manager = Game_Setter()
answer, dummy_text, texts = make_question()
answer_color, answer_text = answer
manager.set_new_game(answer_text, texts)
write_text(dummy_text, answer_color)


running = True
new_game = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                for b in buttons:
                    if b.is_hovering(pos):
                        if manager.is_answer(b.get_text()):
                            manager.update_score()
                            new_game = True
                        else:
                            running = False
                        break
                    else:
                        pass
    
    pos = pygame.mouse.get_pos()
    for b in buttons:
        if b.is_hovering(pos):
            b.draw(WHITE, BLACK)
        else:
            b.draw()

    if new_game:
        screen.fill(WHITE)
        answer, dummy_text, texts = make_question()
        answer_color, answer_text = answer
        manager.set_new_game(answer_text, texts)
        write_text(dummy_text, answer_color)
        write_score(manager.get_score())
        new_game = False
    
    if manager.is_time_over():
        running = False
        
    pygame.display.update()


screen.fill(WHITE)
write_text(f'점수:{manager.get_score()}', BLACK)
pygame.display.update()

ticks = pygame.time.get_ticks()
while pygame.time.get_ticks() - ticks < 3000:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()
sys.exit()
