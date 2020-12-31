import pygame
import os
from random import randint
import pyttsx3

pygame.init()

robot_mouth = pyttsx3.init()

# Set screen size
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

running = True
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREY = (220, 200, 200)

# Tube sizes 
TUBE_WIDTH = 50

# Choose velocity for tube movement
TUBE_VELOCITY = 3

# Distance between 2 tubes
TUBE_GAP = 150

# Position of three-first tubes (outside the screen)
tube1_x = 600
tube2_x = 800
tube3_x = 1000

# Random tube heights
tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

# First bird position
BIRD_X = 30
bird_y = 300

# Bird size
BIRD_WIDTH = 35
BIRD_HEIGHT = 35

font = pygame.font.SysFont('sans', 20)
text_1 = font.render('FLAPPY BIRD', True, BLACK)
text_2 = font.render('SNAKE WITH BOX', True, BLACK)
text_3 = font.render('FREEDOM SNAKE', True, BLACK)
text_4 = font.render('ABOUT ME', True, BLACK)
text_5 = font.render('QUIT', True, BLACK)
# text_6 = font.render('Reset', True, BLACK)

text = font.render('x', True, BLACK)

background_image = pygame.image.load("game-background-png-2.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

bird_image = pygame.image.load("chim2.png")

pygame.display.set_caption('My Games')

welcome = "Hello. Welcome to My Games. Please choose a game"
introduction = "This is my project for examination term of Python class"
thank = "Thank you for comming. See you again"
bird = "You choose FLAPPY BIRD"
snake = "You choose SNAKE WITH BOX"
free = "You choose FREEDOM SNAKE"

clock = pygame.time.Clock()

while running:		
	clock.tick(60)
	
	# Beautiful background
	screen.blit(background_image,(0, 0))

	# Draw tubes up
	tube1u_rect = pygame.draw.rect(screen, GREEN, (tube1_x, 0, TUBE_WIDTH, tube1_height))
	tube2u_rect = pygame.draw.rect(screen, GREEN, (tube2_x, 0, TUBE_WIDTH, tube2_height))
	tube3u_rect = pygame.draw.rect(screen, GREEN, (tube3_x, 0, TUBE_WIDTH, tube3_height))
	# screen.blit(tube_image, (tube1_x, 0)) 
	
	# Draw tubes down
	tube1d_rect = pygame.draw.rect(screen, GREEN, (tube1_x, tube1_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube1_height - TUBE_GAP))
	tube2d_rect = pygame.draw.rect(screen, GREEN, (tube2_x, tube2_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube2_height - TUBE_GAP))
	tube3d_rect = pygame.draw.rect(screen, GREEN, (tube3_x, tube3_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube3_height - TUBE_GAP))
	# screen.blit(tube_image, (tube1_x, tube1_height + TUBE_GAP))
	
	# Draw quit
	quit_button = pygame.draw.rect(screen, GREY, (WIDTH - 20, 10, 10, 10))
	screen.blit(text, (WIDTH - 18, 4))

	# Tube movement
	tube1_x -= TUBE_VELOCITY
	tube2_x -= TUBE_VELOCITY
	tube3_x -= TUBE_VELOCITY

	# Draw bird
	bird_rect = pygame.draw.rect(screen, YELLOW, (BIRD_X, bird_y, BIRD_WIDTH, BIRD_HEIGHT))
	screen.blit(bird_image, bird_rect)

	# New tubes
	if tube1_x < -TUBE_WIDTH:
		tube1_x = 550
		tube1_height = randint(100, 400)
		tube1_pass = False
		robot_mouth.say(welcome)
		robot_mouth.runAndWait()
	if tube2_x < -TUBE_WIDTH:
		tube2_x = 550
		tube2_height = randint(100, 400)
		tube2_pass = False
	if tube3_x < -TUBE_WIDTH:
		tube3_x = 550
		tube3_height = randint(100, 400)
		tube3_pass = False

	# Welcome
	WELCOME_txt = font.render("WELCOME TO MY GAMES", True, BLACK)
	author_txt = font.render("Author: Nguyen Viet Anh", True, BLACK)
	screen.blit(WELCOME_txt, (100, 10))
	screen.blit(author_txt, (110, 30))

	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen, WHITE, (110, 100, 180, 50))
	pygame.draw.rect(screen, WHITE, (110, 200, 180, 50))
	pygame.draw.rect(screen, WHITE, (110, 300, 180, 50))
	pygame.draw.rect(screen, WHITE, (110, 400, 180, 50))
	pygame.draw.rect(screen, WHITE, (110, 500, 180, 50))

	screen.blit(text_1, (150, 115))
	screen.blit(text_2, (130, 215))
	screen.blit(text_3, (130, 315))
	screen.blit(text_4, (160, 415))
	screen.blit(text_5, (180, 515))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				pygame.mixer.pause()
				if (100 < mouse_x < 300) and (100 < mouse_y < 150):
					print("You choose FLAPPY BIRD")
					robot_mouth.say(bird)
					robot_mouth.runAndWait()
					failure = os.system("python flappybird.py")
				if (100 < mouse_x < 300) and (200 < mouse_y < 250):
					print("You choose SNAKE WITH BOX")
					robot_mouth.say(snake)
					robot_mouth.runAndWait()
					failure = os.system("python snake.py")
				if (100 < mouse_x < 300) and (300 < mouse_y < 350):
					print("You choose FREEDOM SNAKE")
					robot_mouth.say(free)
					robot_mouth.runAndWait()
					failure = os.system("python snakeunbox.py")
				if (100 < mouse_x < 300) and (400 < mouse_y < 450):
					print("You choose ABOUT ME")
					robot_mouth.say(introduction)
					robot_mouth.runAndWait()
				if (100 < mouse_x < 300) and (500 < mouse_y < 550):
					print("You choose QUIT")
					robot_mouth.say(thank)
					robot_mouth.runAndWait()
					pygame.quit()
				if (WIDTH - 20 < mouse_x < WIDTH - 10) and (10 < mouse_y < 20):
					robot_mouth.say(thank)
					robot_mouth.runAndWait()	
					pygame.quit()
				
	pygame.display.flip()

pygame.quit()