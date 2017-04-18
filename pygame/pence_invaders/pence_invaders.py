import pygame, sys, random, re
from pygame.locals import *
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

colors = {'RED': (255, 0, 0),
	'ORANGE': (255, 165, 0),
	'YELLOW': (255, 255, 0),
	'GREEN': (0, 255, 0),
	'BLUE': (0, 0, 255),
	'INDIGO': (128, 0, 128),
	}

pygame.mixer.pre_init(22100, -16, 2, 64)
pygame.mixer.init()
pygame.init()

def run_game():
	
	pi_settings = Settings()
	bg = pygame.image.load(str(pi_settings.screen_width) + 'x' + str(pi_settings.screen_height) + '.jpg')
	screen = pygame.display.set_mode(
		(pi_settings.screen_width,pi_settings.screen_height), pygame.FULLSCREEN, 32)
	pygame.display.set_caption("Pence Invaders")
	pygame.display.set_icon(pygame.image.load('images//pence.png'))

	#Creat an instance to store game statistics
	stats = GameStats(pi_settings)
	
	# Make a ship, a group of bullets, and a group of aliens
	ship = Ship(pi_settings, screen)
	bullets = Group()
	aliens = Group()
	bombs = Group()
	
	#Creat the fleet of aliens
	gf.create_fleet(pi_settings, screen, ship, aliens)
	
	
	#Main Game Loop
	while True:
		
		#Watch for keyboard and mouse events.
		screen.blit(bg, [0,0])
		gf.check_events(pi_settings, screen, ship, bullets, bombs, stats)

		if stats.game_active:
			ship.update()
			gf.update_bullets(pi_settings, screen, aliens, bullets, stats)
			gf.update_bombs(pi_settings, screen, aliens, bombs, stats)
			gf.update_aliens(pi_settings, stats, screen, ship, aliens, bullets, bombs)
			gf.kill_counter(pi_settings, screen, stats)
			gf.bomb_counter(pi_settings, screen)
			gf.life_counter(pi_settings, screen, stats)
		pi_settings.bullet_color = random.choice(list(colors.values()))
		pi_settings.bomb_color = random.choice(list(colors.values()))
		gf.game_over(pi_settings, screen, stats)
		gf.update_screen(pi_settings, screen, ship, aliens, bullets, bombs)

run_game()
