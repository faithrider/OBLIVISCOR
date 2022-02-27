# Import the pygame module
import pygame
from pygame.locals import *
pygame.init()

# Define constants for the screen width and height, and colors. And, load the character images
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
WINDOW_WIDTH = 100
WINDOW_HEIGHT = 100
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
skeleton = pygame.image.load(r'Skeleton.png')
mystery_man = pygame.image.load(r'Mystery_Man.png')

# Creates the window the game will run in, as well as give the game's name and font
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
pygame.display.set_caption('OBLIVISCOR')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(pygame.font.match_font("calibri"), 18)
dialogue = pygame.font.Font(pygame.font.match_font("papyrus"), 18)
story = True
decision = 0

def quit_mechanic():
    # for loop through the event queue, checks if player wants to quit.
    running = True
    while running:
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    quit()
            elif event.type == QUIT:
                running = False
                quit()
            if story:
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        running = False
            elif story == False:
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        screen.fill(BLACK)
                        return 0
                    elif event.key == K_LEFT:
                        screen.fill(BLACK)
                        return 1
    screen.fill(BLACK)

# prints whatever the current dialogue is.
def print_dialogue(output_text):
    window = output_text.get_rect()
    window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
    screen.blit(output_text, window)
    pygame.display.flip()
    quit_mechanic()

def print_choices(left_text, right_text):
    window = left_text.get_rect()
    window.center = (SCREEN_WIDTH * (1/4), SCREEN_HEIGHT // 6)
    screen.blit(left_text, window)
    window = right_text.get_rect()
    window.center = (SCREEN_WIDTH * (3/4), SCREEN_HEIGHT // 6)
    screen.blit(right_text, window)
    pygame.display.flip()
    quit_mechanic()


# prints the speaking character
def print_character(picture):
    screen.blit(picture, ((SCREEN_WIDTH // 2)-128, SCREEN_HEIGHT-256))

# start screen, allows the player to either start the game, or exit.
def starting_screen():
    font = pygame.font.Font(pygame.font.match_font("calibri"), 56)
    title = font.render('OBLIVISCOR', False, WHITE, BLACK)
    title_window = title.get_rect()
    title_window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
    screen.blit(title, title_window)
    print_character(skeleton)

    font = pygame.font.Font(pygame.font.match_font("calibri"), 18)
    continue_button = font.render('press space to start', False, WHITE, BLACK)
    button_window = continue_button.get_rect()
    button_window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT-(SCREEN_HEIGHT // 5))
    screen.blit(continue_button, button_window)

    pygame.display.flip()
    quit_mechanic()

# The story the player will click through before any gameplay
def before_interaction():
    output_text = font.render('Where am I...?', False, WHITE, BLACK)
    print_dialogue(output_text)

    output_text = font.render('...what is this place?', False, WHITE, BLACK)
    print_dialogue(output_text)

    output_text = font.render('Wait, I think I see someone.', False, WHITE, BLACK)
    print_dialogue(output_text)

    output_text = font.render('Hello...?', False, WHITE, BLACK)
    print_dialogue(output_text)

def first_talk_with_mystery_man():
    output_text = dialogue.render('It\'s sad to see you like this.', False, WHITE, BLACK)
    print_character(mystery_man)
    print_dialogue(output_text)

    output_text = font.render('Like what?...I can\'t remember anything...', False, WHITE, BLACK)
    print_dialogue(output_text)
    print_character(mystery_man)

    output_text = dialogue.render('You really should get to the river.', False, WHITE, BLACK)
    print_character(mystery_man)
    print_dialogue(output_text)

    story = False
    print_character(mystery_man)
    left_text = font.render('The river?', False, WHITE, BLACK)
    right_text = font.render('Do you know who I am? My name?', False, WHITE, BLACK)
    decision = print_choices(left_text, right_text)
    if decision:
        print_character(mystery_man)
        output_text = dialogue.render('Yes, just keep walking, you\'ll get there.', False, WHITE, BLACK)
        print_dialogue(output_text)
    else:
        print_character(mystery_man)
        output_text = dialogue.render('Your name? Unimportant.', False, WHITE, BLACK)
        print_dialogue(output_text)

    story = True


# Run the game.
starting_screen()
before_interaction()
first_talk_with_mystery_man()
quit()