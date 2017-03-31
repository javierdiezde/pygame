import pygame



class Sound():
	
	def __init__(self):
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.mixer.init()
	
		self.invader_hit = pygame.mixer.Sound('noises/invaderkilled.wav')
		self.shoot_sound = pygame.mixer.Sound('noises/shoot.wav')
		self.pygame.mixer.music.load('noises/spaceinvaders1.mpeg')
		self.pygame.mixer.music.play(-1, 0)
		self.invader_hit.set_volume(.3)
		self.shoot_sound.set_volume(.3)

