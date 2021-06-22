import pygame
from pygame import mixer, font
import time
import random

snake_speed = 10

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
yellow = pygame.Color(200, 200, 0)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(200, 0, 200)
snakeColor = random.choice([blue, green, purple, yellow])

pygame.init()
pygame.font.init()
# lets make a function to play sound on eating the fruit and when game over
mixer.init()
def snd(music):
	mixer.music.load(music)
	mixer.music.play()
	
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()
# defining snake default position
snake_position = [100, 50]

# defining first 3 blocks of snake
snake_body = [ [100, 50],
				[90, 50],
				[80, 50]
			]
# fruit posiiton
fruit_position = [random.randrange(1, (window_x//10)) * 10,
				random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# setting default snake direction
direction = 'RIGHT'
change_to = direction
# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):
	
	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, red)
	
	# create a rectangular object for the
	# text surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	game_window.blit(score_surface, score_rect)
# game over function
def game_over():
	
	# creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	# creating a text surface on which text
	# will be drawn
	game_over_surface = my_font.render('Your Score is : ' + str(score), True, black)
	
	# create a rectangular object for the text
	# surface object
	game_over_rect = game_over_surface.get_rect()
	
	# setting position of the text
	game_over_rect.midtop = (window_x/2, window_y/4)
	
	# blit wil draw the text on screen
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the
	# program
	time.sleep(4)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()
	
# Main Function
while True:
	# handling key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			snd('2899.ogg')
			if event.key == pygame.K_w and pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_z and pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_a and pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_s and pygame.K_RIGHT:
				change_to = 'RIGHT'

	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	# Snake body growing mechanism
	# if fruits and snakes collide then scores will be
	# incremented by 10
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 5
		snd('5251.ogg') # You should move the music file to project directory before using here
		fruit_spawn = False
	else:
		snake_body.pop()
	if score > 20:
		snake_speed = 13
		
	if not fruit_spawn:
		fruit_position = [random.randrange(1, (window_x//10)) * 10,
						random.randrange(1, (window_y//10)) * 10]
		
	fruit_spawn = True
	
	game_window.fill(white)
	my_bg = pygame.image.load('/storage/emulated/0/download/images.png') # path of image
	my_bg = pygame.transform.scale(my_bg, (window_x, window_y))
	game_window.blit(my_bg, (0, 0))
	
	for pos in snake_body:
		pygame.draw.rect(game_window,snakeColor, pygame.Rect(
		pos[0], pos[1], 10, 10))
		
	pygame.draw.rect(game_window, red, pygame.Rect(
	fruit_position[0], fruit_position[1], 10, 10))
	
	# Game Over conditions
	if snake_position[0] < 0 or snake_position[0] > window_x-20:
		snd('524.ogg') # You should move the music file to project directory before using here
		game_over()
	if snake_position[1] < 0 or snake_position[1] > window_y-20:
		snd('524.ogg')
		game_over()
	
	# Touching the snake body
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			snd('524.ogg')
			game_over()
	
	# displaying score countinuously
	show_score(1, blue, 'times new roman', 20)
	
	# Refresh game screen
	pygame.display.update()

	# Frame Per Second /Refres Rate
	fps.tick(snake_speed)
	
