import pygame
import random

pygame.init()
# colos
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 0, 100)



screen_width = 900
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update() # updating the window

# Game specific variable
# exit_game = False
# game_over = False
# snake_x = 45
# snake_y = 55
# init_velocity = 5
# velocity_x = 0
# velocity_y = 0
# snake_size = 10
# fps = 60
# food_x = random.randint(20, screen_width//2)
# food_y = random.randint(20, screen_height//2)
# score = 0



clock = pygame.time.Clock() # clock for the game kitne time pe window update karni hai
font = pygame.font.SysFont(None, 55)  # 1 argu is fro default text font, 2 for size of the font
def text_screen(text, color, x, y):
	screen_text = font.render(text, True, color)  # 1 for text, 2 conver heigh to low resolution, 3 color of text
	screen.blit(screen_text , [x, y]) # for updating the screen


def plot_snake(screen, color, snk_list, snake_size):
	for x, y in snk_list:
		pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])


def welcome():
	exit_game = False
	while not exit_game:
		screen.fill((0, 255, 0))
		text_screen("Welcome To Snakes", black, 260, 250)
		text_screen("Press Space Bar To Play", black, 232, 290)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					gameLoop()

		pygame.display.update()
		clock.tick(60)


# snk_list = []
# snk_length = 1

def gameLoop():
	exit_game = False
	game_over = False
	snake_x = 45
	snake_y = 55
	init_velocity = 5
	velocity_x = 0
	velocity_y = 0
	snake_size = 10
	fps = 60
	snk_list = []
	snk_length = 1
	food_x = random.randint(20, screen_width//2)
	food_y = random.randint(20, screen_height//2)
	score = 0
	# game loop
	while not exit_game:
		if game_over:
			screen.fill(white)
			text_screen("Game Over! Press Enter to Continue", red, 100, 250)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True
					
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						welcome()
		else:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						velocity_x = init_velocity
						velocity_y = 0

					if event.key == pygame.K_LEFT:
						velocity_x = -init_velocity
						velocity_y = 0

					if event.key == pygame.K_UP:
						velocity_y = -init_velocity
						velocity_x = 0

					if event.key == pygame.K_DOWN:
						velocity_y = init_velocity
						velocity_x = 0

			snake_x += velocity_x
			snake_y += velocity_y

			if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
				score += 1
				food_x = random.randint(20, screen_width//2)
				food_y = random.randint(20, screen_height//2)
				snk_length += 4

			screen.fill(white)
			text_screen("Score: " + str(score * 10), yellow, 5, 5)
			pygame.draw.rect(screen, red, [food_x, food_y, snake_size, snake_size])

			head = []
			head.append(snake_x)
			head.append(snake_y)
			snk_list.append(head)

			if len(snk_list) > snk_length:
				del snk_list[0]

			if head in snk_list[:-1]:
				game_over = True

			if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
				game_over = True


			# pygame.draw.rect(screen, black, [snake_x, snake_y, snake_size, snake_size])	
			plot_snake(screen, black, snk_list, snake_size)
		pygame.display.update()
		clock.tick(fps) # 1 second main kitne frame chahiye

	pygame.quit()
	quit()

# gameLoop()
welcome()