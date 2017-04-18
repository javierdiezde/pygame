import pygame

class Ship():
	
	def __init__(self, pi_settings, screen):
		'''Sets Ship position on the screen'''
		self.screen = screen
		self.pi_settings = pi_settings

		#Load the ship image and get it's rect
		self.image = pygame.image.load('images/ship_test.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#Movement Flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)
		
	def update(self):
		'''Updates the ships position based on its tag'''
		
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.pi_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.pi_settings.ship_speed_factor
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.bottom -= self.pi_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.bottom += self.pi_settings.ship_speed_factor
			
		#Update rect object from self.center
		self.rect.centerx = self.center
		self.rect.bottom = self.bottom
		
	def blitme(self):
		'''Draw the ship at its current location'''
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
			"""Center Ship"""
			self.centerx = self.screen_rect.centerx
			self.bottom = self.screen_rect.bottom
