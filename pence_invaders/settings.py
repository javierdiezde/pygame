import random
 
class Settings():
	'''A class containing all game settings'''
	
	def __init__(self):
		'''Initialize game settings'''
		#screen settings
		self.screen_width = 1366
		self.screen_height = 768
		#Ship settings
		self.ship_speed_factor = 6
		self.ship_limit = 3
		
		#Bullet settings
		self.bullet_speed_factor = 8
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullets_allowed = 4

		#Bomb settings
		self.bomb_speed_factor = 6
		self.bomb_width = self.screen_width
		self.bomb_height = 15
		self.bombs_allowed = 1
		
		#Alien settings
		self.alien_speed_factor = 4
		self.fleet_drop_speed = 10
		#Fleet direction of 1 equalls right; -1 equalls left
		self.fleet_direction = 1
