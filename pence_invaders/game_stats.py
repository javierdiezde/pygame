from settings import Settings

pi_settings = Settings()

class GameStats():
	"""Track Stats for game"""

	def __init__(self, pi_settigs):
		'''init statistics'''
		self.pi_settings = pi_settings
		self.reset_stats()

		#Start Invasion of PENCE
		self.game_active = True
		self.score = 0

	def reset_stats(self):
		"""init statistics that can change during game"""
		self.ships_left = self.pi_settings.ship_limit
