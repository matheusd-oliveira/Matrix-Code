import pygame
from pygame.locals import *
from sys import exit
from random import randrange, choice


pygame.init()

# Creating colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
COLORS = [GREEN, RED, BLUE]
color_change = 0
FONT_SIZE = 10
# Creating a Screen
width = 1028
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Matrix')

# Creating Letters:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 1, 2, 3, 4, 5, 6]

# Writing a message on screen
font = pygame.font.SysFont('arial', FONT_SIZE, True, True)
'''message = 'hello world'
text = font.render(message, True, GREEN)'''

# Putting a sound in our program:
sound = pygame.mixer.music.load('_Trinity Infinity_160k.mp3')
pygame.mixer.music.play(-1)

# Setting the FPS
clock = pygame.time.Clock()
FPS = 10

# Monitoring the Time
initial_time = 0
current_time = 0
# Change the colour letter about the time:
color_time = 0
# Creating a Class That create the code lines from matrix:
class CodeLine:
    def __init__(self):
        self.color = GREEN
        self.fill = 1
        self.ypos_list = list()    # Store the y values
        self.letters_list = list() # Store the drawn random letters
        self.xpos = randrange(FONT_SIZE, width + FONT_SIZE, FONT_SIZE)
        self.ypos = randrange(0, height + FONT_SIZE, FONT_SIZE)
        self.ypos_list.append(self.ypos)  
    def draw_codeline(self):   # DRAW THE LINES ON THE SCREEN ,IN GREEN
        randomic_letter = choice(letters)
        self.letters_list.append(randomic_letter)
        
        for msg , y in zip(self.letters_list, self.ypos_list):  # At each iteration of the while loop, a letter will be drawn
            message = f'{msg}'
            text = font.render(message, True, self.color )
            screen.blit(text, (self.xpos, y))

    def desloc_codeline(self): # MOVE THE LINES FOR DOWN
        # I want the lines to disappear in a certain length
        if self.ypos > height or len(self.ypos_list) > 20: 
            message = ' '
            text = font.render(message, True, WHITE)
            screen.fill(BLACK, (self.xpos, self.ypos_list[0], text.get_width() + FONT_SIZE, text.get_height() * self.fill))
            if text.get_height() * self.fill > len(self.ypos_list) * text.get_height():
                self.letters_list.clear()
            else:
                self.fill += 1

        else:
            self.ypos += FONT_SIZE # At each iteration while loop, the codeline will be move for down.
            self.ypos_list.append(self.ypos)
            message = f'{self.letters_list[-1]}'
            text = font.render(message, True, WHITE)
            screen.fill(BLACK, (self.xpos, self.ypos_list[-1], text.get_width() + FONT_SIZE, text.get_height()))
            screen.blit(text, (self.xpos, self.ypos_list[-1]))
            

# Creating variables for use in the function 'create_multiples_obj':

obj_list = list()
repeat_list = list()
number_of_obj = 20
generate = True

# Creating multiples objects:
def create_multiples_obj(obj_list, number_of_obj, generate):
    if generate:
        for i in range(number_of_obj):
            obj = CodeLine()
            # if two idential objects are created,one will be deleted
            if obj.xpos in repeat_list or obj.ypos > height:
                repeat_list.remove(obj.xpos)
                obj.letters_list.clear()
                del obj
            else:
                obj_list.append(obj)
                repeat_list.append(obj.xpos)
        for i in obj_list:
            i.color = COLORS[color_change]
            i.draw_codeline()
            i.desloc_codeline()
    else:
        for i in obj_list:
            i.color = COLORS[color_change]
            i.draw_codeline()
            i.desloc_codeline()



# Main loop
while True:
    clock.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    current_time = pygame.time.get_ticks()
    if current_time - color_time > 10000: # 10 seconds
        color_change  = (color_change + 1) % len(COLORS)
        color_time = pygame.time.get_ticks()

    if current_time - initial_time > 200:   # 0.2 seconds, new objects are created.
        gerenate = True
        initial_time = pygame.time.get_ticks()


    create_multiples_obj(obj_list, number_of_obj, generate)
    #screen.blit(text, (width // 2, height // 2))
    pygame.display.flip()
