import sys
import pygame
import random

# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress: 
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

class TextBox():
    def __init__(self, x, y, width, height, textText='Text Box', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = '#add8e6'
        self.textSurface = pygame.Surface((self.width, self.height))
        self.textRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.textSurf = font.render(textText, True, (20, 20, 20))
        objects.append(self)
    def process(self):
        self.textSurface.fill(self.color)
        self.textSurface.blit(self.textSurf, [
            self.textRect.width/2 - self.textSurf.get_rect().width/2,
            self.textRect.height/2 - self.textSurf.get_rect().height/2
        ])
        screen.blit(self.textSurface, self.textRect)

game_record = [0,0,0]
b_width = 400
b_height = 100
b_init_h = 140

def cpu(user_input):
    cpu = random.randint(1,3)
    choices = ['Rock', 'Paper', 'Scissors']
    cpu_choice = choices[cpu - 1]
    result = 0
    diff = user_input - cpu
    if diff == 0:
        result = 0
        game_record[0]+=1
    elif (diff % 3) == 1: 
        result = 1
        game_record[1]+=1
    else:
        result = 2
        game_record[2]+=1

    game_results = ['Tie Game!','You Win!','CPU Wins!']
    text = 'CPU chose ' + cpu_choice + '. ' + game_results[result]
    TextBox((width - 700)/2, 460, 700, b_height, text)
    wl_record = 'W: ' + str(game_record[1]) + ' T: ' + str(game_record[0]) + ' L: ' + str(game_record[2])
    TextBox((width - 700)/2, 570, 700, b_height, wl_record)
def rockFunc():
    res = cpu(1)

def paperFunc():
    res = cpu(2)

def scissorsFunc():
    res = cpu(3)

Button((width - b_width)/2, b_init_h, b_width, b_height, 'Rock', rockFunc)
Button((width - b_width)/2, b_init_h + b_height + 10, b_width, b_height, 'Paper', paperFunc)
Button((width - b_width)/2, b_init_h + 2 * b_height + 20, b_width, b_height, 'Scissors', scissorsFunc  )
TextBox((width - 700)/2, 30, 700, b_height, 'Choose Rock Paper or Scissors!')
while True:
    screen.fill((173, 216, 230))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for object in objects:
        object.process()
    pygame.display.flip()
    fpsClock.tick(fps)