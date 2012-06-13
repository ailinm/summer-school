import pygame, tetris, random, os

from pygame.locals import *
from piece import *

#Initializations
pygame.font.init()
pygame.mixer.init()

my_font50 = pygame.font.SysFont(None,50)
my_font40 = pygame.font.SysFont(None,40)
my_font30 = pygame.font.SysFont(None,30)
my_font25 = pygame.font.SysFont(None,25)
my_font20 = pygame.font.SysFont(None,20)
my_font15 = pygame.font.SysFont(None,15)

class Settings(object):
	"""
	Game Settings class
	"""
	game_area = Rect(5, 5, 150, 300)
	game_info = Rect(160, 5, 150, 300)
	box_display = Rect(185, 65, 100, 70)
	lines = 0
	speed = 300

	def __init__(self):
		"""        
		Initialize with default settings
		"""
		#Size of the main window
		self.resolution = (315, 310)
		# Background color
		self.background = (0, 153, 153)
		# Mouse enabled
		self.mouse_enabled = True
		# Title
		self.title = "Tetris"
       
		self.colors = [(255, 255, 255),		# WHITE
					   (100, 100, 100), 	# GRAY
		     		   (255,   0,   0), 	# RED
		     		   (  0, 255,   0), 	# BLUE
		     		   (  0,   0, 255), 	# GREEN
					   (  0, 153, 153),		# TURQUOISE
		     		   (  0,   0,   0)]		# BLACK
		     		   
		colors = self.colors
		
		self.my_font40 = pygame.font.SysFont(None, 40)
		self.my_font30 = pygame.font.SysFont(None, 30)
		self.my_font20 = pygame.font.SysFont(None, 20)
		
		self.help_text1 = my_font20.render('Rules:', True, colors[6], colors[5])
		self.help_text2 = my_font20.render('Left and Right keys to move.', True, colors[6], colors[5])
		self.help_text3 = my_font20.render('Up key to rotate blocks.', True, colors[6], colors[5])
		self.help_text4 = my_font30.render('START GAME', True, colors[6], colors[5])
		self.help_text5 = my_font30.render('RESET GAME', True, colors[6], colors[5])
		self.help_text6 = my_font40.render('PAUSE FOR BEER', True, colors[6], colors[5])
		self.my_font30.set_bold(True)
		self.game_over = my_font30.render('NO BEER FOR YOU TODAY', True, colors[6], colors[5])

		self.click_sound = pygame.mixer.Sound(os.path.join('sounds', 'click.wav'))
		self.move_sound = pygame.mixer.Sound(os.path.join('sounds', 'move.wav'))
		self.rotate_sound = pygame.mixer.Sound(os.path.join('sounds', 'rotate.wav'))
		self.tetris_sound = pygame.mixer.Sound(os.path.join('sounds', 'tetris.wav'))

		# List of all bricks
		grid = []
		# A dictionary in which we find the number of the bricks on a line
		bricks = {290:0, 275:0, 260:0, 245:0, 230:0, 215:0, 200:0, 185:0, 170:0, 155:0, 
                  140:0, 125:0, 110:0, 95:0, 80:0, 65:0, 50:0, 35:0, 20:0, 5:0}

	def update():
		screen.set_clip(game_info)
		line_text = my_font30.render('Lines Number:' + str(lines), True, colors[6], colors[5])
		screen.blit(line_text, (165, 10))
		screen.set_clip(game_area)
		for g in grid:
			for pos in g.starting_pos:
				screen.blit(g.image, pos)
		pygame.display.update()

	def move_down(key, grid, bricks):
		for g in grid:
			for pos in g.starting_pos:
				if (pos.top < key):
					bricks[pos.top] -= 1
					pos.top += 15
					bricks[pos.top] += 1
		screen.fill(colors[5])
		update()
		pygame.time.wait(30)
		game(grid, bricks)

	def game(grid, bricks):
		sorted_keys = bricks.keys()
		sorted_keys.sort(reverse = True)
		for k in sorted_keys:
			if (bricks[k] == 10):
				lines += 1
				speed -= 10
				for g in grid:
					for pos in g.starting_pos:
						if pos.top == k:
							pygame.draw.rect(screen, colors[6], pos, 0)
							tetris_sound.play()
							pygame.display.update()
							pygame.time.wait(20)
					g.starting_pos = [pos for pos in g.starting_pos if pos != k]
				bricks[k] = 0
				grid = [g for g in grid if len(g.starting_pos) > 0]
				move_down(k, grid, bricks)
