import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''Class to handle bullets from player ship'''
	
	def __init__(self, pi_settings, screen, ship):
		'''Creat a bullet the ship's position'''
		super().__init__()
		self.screen = screen
		
		#Create a bullet at 0,0 and moves it to the correct position
		self.rect = pygame.Rect(0, 0, pi_settings.bullet_width,
			pi_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
			
		#Stores bullet's position as a decimal
		self.y = float(self.rect.y)
	
		self.color = pi_settings.bullet_color
		self.speed_factor = pi_settings.bullet_speed_factor
	
	def update(self):
		'''Move bullet the bullet up the screen'''
		#Update the decimal position of the bullet
		self.y -= self.speed_factor
		#Update the rect position
		self.rect.y = self.y
	
	def draw_bullet(self):
		'''Draw bullet to the screen'''
		pygame.draw.rect(self.screen, self.color, self.rect)
