import random
import pygame
from pygame.sprite import Sprite

crooked_images = ['images/trump.png', 'images/pence.png',
                  'images/adolf.png', 'images/bernie.png',
                  'images/bill.png', 'images/denis.png',
                  'images/george.png', 'images/jim.png',
                  'images/keith.png', 'images/louis.png',
                  'images/manuel.png', 'images/marco.png',
                  'images/steve.png', 'images/hillary.png'
                ]

class Alien(Sprite):
	'''A class to represent a single alien in the fleet'''
	
	def __init__(self, pi_settings, screen):
		'''initialize the alien and set its starting position'''
		super().__init__()
		self.screen = screen
		self.pi_settings = pi_settings
	
		#Load the alien image and set its rect attribute
		self.image = pygame.image.load(random.choice(crooked_images[:]))
		self.rect = self.image.get_rect()
	
		#Start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
	
		#Store the alien's exact position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
	def blitme(self):
		'''draw the alien at it's current location'''
		self.screen.blit(self.image, self.rect)

	def check_edges(self, pi_settings):
		'''Return True if alien is at edge of the screen'''
		screen_rect = self.screen.get_rect()
		if self.rect.right >= pi_settings.screen_width:
			return True
		elif self.x <= 0:
			return True
		
	def update(self):
		'''Move the alien right or left'''
		self.x += (self.pi_settings.alien_speed_factor * 
						self.pi_settings.fleet_direction)
		self.rect.x = self.x
		
