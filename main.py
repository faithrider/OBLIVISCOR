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
ferryman = pygame.image.load(r'Ferryman.png')
mystery_man = pygame.image.load(r'Mystery_Man.png')

# Creates the window the game will run in, as well as give the game's name and font
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
pygame.display.set_caption('OBLIVISCOR')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(pygame.font.match_font("calibri"), 18)
dialogue = pygame.font.Font(pygame.font.match_font("papyrus"), 18)
story = True
have_coin = False
decision = True

# this both serves as a way to let the player quit at anytime, and to test if the program should take in L/R or space.
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
            if event.type == KEYDOWN:
                # If it is 'story', it means that there is no decision to be made, so only space is accepected.
                if story == True:
                        if event.key == K_SPACE:
                            running = False
                elif story == False:
                    if event.key == K_LEFT:
                        screen.fill(BLACK)
                        return True
                    elif event.key == K_RIGHT:
                        screen.fill(BLACK)
                        return False
    screen.fill(BLACK)

# prints whatever the current dialogue is.
def print_dialogue(output_text):
    window = output_text.get_rect()
    window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
    screen.blit(output_text, window)
    pygame.display.flip()
    quit_mechanic()

# prints the two choices, if there are two.
def print_choices(left, right):
    window = left.get_rect()
    window.center = (SCREEN_WIDTH * (1/4), SCREEN_HEIGHT // 6)
    screen.blit(left, window)
    window = right.get_rect()
    window.center = (SCREEN_WIDTH * (3/4), SCREEN_HEIGHT // 6)
    screen.blit(right, window)
    pygame.display.flip()
    return quit_mechanic()


# prints the speaking character's picture.
def print_character(picture):
    screen.blit(picture, ((SCREEN_WIDTH // 2)-128, SCREEN_HEIGHT-256))


# start screen, allows the player to either start the game, or exit.
def starting_screen():
    font = pygame.font.Font(pygame.font.match_font("calibri"), 56)
    title = font.render('OBLIVISCOR', False, WHITE, BLACK)
    title_window = title.get_rect()
    title_window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
    screen.blit(title, title_window)
    print_character(ferryman)

    font = pygame.font.Font(pygame.font.match_font("calibri"), 18)
    continue_button = font.render('press space to start', False, WHITE, BLACK)
    button_window = continue_button.get_rect()
    button_window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT-(SCREEN_HEIGHT // 5))
    screen.blit(continue_button, button_window)

    pygame.display.flip()
    quit_mechanic()

    font = pygame.font.Font(pygame.font.match_font("calibri"), 18)
    controls = font.render('Press space when there is one line of dialogue.', False, WHITE, BLACK)
    control_window = controls.get_rect()
    control_window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * (1/5))
    screen.blit(controls, control_window)

    controls = font.render('Press the left or right arrow button when making a decision.', False, WHITE, BLACK)
    control_window = controls.get_rect()
    control_window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * (2/5))
    screen.blit(controls, control_window)

    controls = font.render('You can quit at any time by pressing esc.', False, WHITE, BLACK)
    control_window = controls.get_rect()
    control_window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * (3/5))
    screen.blit(controls, control_window)

    controls = font.render('(Press space to continue)', False, WHITE, BLACK)
    control_window = controls.get_rect()
    control_window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * (4/5))
    screen.blit(controls, control_window)





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

    output_text = dialogue.render('It\'s sad to see you like this.', False, WHITE, BLACK)
    print_character(mystery_man)
    print_dialogue(output_text)

    output_text = font.render('Like what?...I can\'t remember anything...', False, WHITE, BLACK)
    print_character(mystery_man)
    print_dialogue(output_text)

    output_text = dialogue.render('You really should get to the river.', False, WHITE, BLACK)
    print_character(mystery_man)
    print_dialogue(output_text)


# Run the game.
starting_screen()
before_interaction()

# choices with the mystery man
story = False
print_character(mystery_man)
left_text = font.render('The river?', False, WHITE, BLACK)
right_text = font.render('Do you know who I am? My name?', False, WHITE, BLACK)
decision = print_choices(left_text, right_text)

if decision:
    print_character(mystery_man)
    output_text = dialogue.render('Yes, just keep walking, you\'ll get there.', False, WHITE, BLACK)
    story = True
    print_dialogue(output_text)
    story = False

    left_text = font.render('But what\'s going on??', False, WHITE, BLACK)
    right_text = font.render('Thank you. I\'ll be going, then.', False, WHITE, BLACK)
    print_character(mystery_man)
    decision = print_choices(left_text, right_text)
    story = True

    if decision:
        print_character(mystery_man)
        output_text = dialogue.render('That is not for you to comprehend. Leave.', False, WHITE, BLACK)
        print_dialogue(output_text)
    elif decision == False:
        print_character(mystery_man)
        output_text = dialogue.render('Here. For the end.', False, WHITE, BLACK)
        print_dialogue(output_text)
        print_character(mystery_man)
        output_text = font.render('A coin...', False, WHITE, BLACK)
        print_dialogue(output_text)
        have_coin = True
elif decision == False:
    print_character(mystery_man)
    output_text = dialogue.render('Your name? Unimportant.', False, WHITE, BLACK)
    story = True
    print_dialogue(output_text)
    story = False
    
    left_text = font.render('Please. I need to know!', False, WHITE, BLACK)
    right_text = font.render('Where do I go?', False, WHITE, BLACK)
    print_character(mystery_man)
    decision = print_choices(left_text, right_text)
    story = True

    if decision:
        print_character(mystery_man)
        output_text = dialogue.render('No. The river awaits you.', False, WHITE, BLACK)
        print_dialogue(output_text)
    elif decision == False:
        print_character(mystery_man)
        output_text = dialogue.render('Onward.', False, WHITE, BLACK)
        print_dialogue(output_text)

# speak with ferryman
def ferryman_conversation():
    dialogue = pygame.font.Font(pygame.font.match_font("papyrus"), 12)
    output_text = font.render('I suppose I should find the river.', False, WHITE, BLACK)
    print_dialogue(output_text)

    output_text = font.render('...', False, WHITE, BLACK)
    print_dialogue(output_text)

    output_text = font.render('Here it is.', False, WHITE, BLACK)
    print_dialogue(output_text)

    print_character(ferryman)
    output_text = dialogue.render('THE RIVER.', False, WHITE, BLACK)
    print_dialogue(output_text)

    print_character(ferryman)
    output_text = dialogue.render('YOU HAVE ARRIVED AT THE END OF BEING.', False, WHITE, BLACK)
    print_dialogue(output_text)

    print_character(ferryman)
    output_text = font.render('Where do I go from here?', False, WHITE, BLACK)
    print_dialogue(output_text)

    print_character(ferryman)
    output_text = dialogue.render('PAY FOR PASSAGE AND YOU SHALL BE LET TO TRAVEL ON.', False, WHITE, BLACK)
    print_dialogue(output_text)


# final part of the story--dependent on if player got the coin from the mystery man.
ferryman_conversation()
def good_end():
    dialogue = pygame.font.Font(pygame.font.match_font("papyrus"), 12)
    font = pygame.font.Font(pygame.font.match_font("calibri"), 18)
    print_character(ferryman)
    output_text = font.render('Pay? Can I pay with this coin?', False, WHITE, BLACK)
    print_dialogue(output_text)

    print_character(ferryman)
    output_text = dialogue.render('THAT IS ACCEPTABLE. PREPARE YOURSELF.', False, WHITE, BLACK)
    print_dialogue(output_text)

    print_character(ferryman)
    output_text = font.render('For?', False, WHITE, BLACK)
    print_dialogue(output_text)

    print_character(ferryman)
    output_text = dialogue.render('BEYOND.', False, WHITE, BLACK)
    print_dialogue(output_text)

    font = pygame.font.Font(pygame.font.match_font("calibri"), 18)
    output_text = font.render('Thank you.', False, WHITE, BLACK)
    print_dialogue(output_text)

    font = pygame.font.Font(pygame.font.match_font("calibri"), 56)
    title = font.render('GOOD END', False, WHITE, BLACK)
    title_window = title.get_rect()
    title_window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
    screen.blit(title, title_window)
    print_character(ferryman)

    font = pygame.font.Font(pygame.font.match_font("calibri"), 18)
    continue_button = font.render('demo created by Faith Rider', False, WHITE, BLACK)
    button_window = continue_button.get_rect()
    button_window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT-(SCREEN_HEIGHT // 5))
    screen.blit(continue_button, button_window)

    pygame.display.flip()
    quit_mechanic()


def bad_end():
    font = pygame.font.Font(pygame.font.match_font("calibri"), 18)
    print_character(ferryman)
    output_text = font.render('Pay? How can I pay when I don\'t even know what\'s going on?', False, WHITE, BLACK)
    print_dialogue(output_text)

    dialogue = pygame.font.Font(pygame.font.match_font("papyrus"), 12)
    print_character(ferryman)
    output_text = dialogue.render('IF YOU HAVE NOT ACQUIRED PAYMENT, YOU CANNOT GO ONWARD.', False, WHITE, BLACK)
    print_dialogue(output_text)

    print_character(ferryman)
    output_text = font.render('Where would I even get payment?!?', False, WHITE, BLACK)
    print_dialogue(output_text)

    print_character(ferryman)
    output_text = dialogue.render('YOU HAD YOUR CHANCE. YOU SPOKE OUT OF TURN, SO YOU LOST YOURS.', False, WHITE, BLACK)
    print_dialogue(output_text)

    output_text = font.render('Wait.', False, WHITE, BLACK)
    print_dialogue(output_text)

    print_character(mystery_man)
    output_text = font.render('I spoke...out of turn...?', False, WHITE, BLACK)
    print_dialogue(output_text)

    font = pygame.font.Font(pygame.font.match_font("calibri"), 18)
    output_text = font.render('How could I have known...?', False, WHITE, BLACK)
    print_dialogue(output_text)

    font = pygame.font.Font(pygame.font.match_font("calibri"), 56)
    title = font.render('BAD END', False, WHITE, BLACK)
    title_window = title.get_rect()
    title_window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
    screen.blit(title, title_window)
    print_character(ferryman)

    font = pygame.font.Font(pygame.font.match_font("calibri"), 18)
    continue_button = font.render('demo created by Faith Rider', False, WHITE, BLACK)
    button_window = continue_button.get_rect()
    button_window.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT-(SCREEN_HEIGHT // 5))
    screen.blit(continue_button, button_window)

    pygame.display.flip()
    quit_mechanic()

if have_coin:
    good_end()
else:
    bad_end()
quit()