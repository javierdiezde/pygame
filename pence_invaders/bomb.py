import pygame
from pygame.sprite import Sprite

class Bomb(Sprite):
	'''Class to handle bullets from player ship'''
	
	def __init__(self, pi_settings, screen, ship):
		'''Creat a bullet the ship's position'''
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()

		#Create a bullet at 0,0 and moves it to the correct position
		self.rect = pygame.Rect(0, 0, pi_settings.bomb_width,
			pi_settings.bomb_height)
		self.rect.centerx = self.screen_rect.centerx
		self.rect.top = ship.rect.top
			
		#Stores bullet's position as a decimal
		self.y = float(self.rect.y)
			
		self.color = pi_settings.bomb_color
		self.speed_factor = pi_settings.bomb_speed_factor
	
	def update(self):
		'''Move bullet the bullet up the screen'''
		#Update the decimal position of the bullet
		self.y -= self.speed_factor
		#Update the rect position
		self.rect.y = self.y
	
	def draw_bomb(self):
		'''Draw bullet to the screen'''
		pygame.draw.rect(self.screen, self.color, self.rect)
		