import sys, pygame, re, time
import pyganim
from bullet import Bullet
from alien import Alien
from ship import Ship
from settings import Settings
from bomb import Bomb

pi_settings = Settings()
screen = pygame.display.set_mode(
		(pi_settings.screen_width,pi_settings.screen_height))
screen = screen
ship = Ship(pi_settings, screen)

pygame.mixer.pre_init(22050, -16, 2, 1102)
pygame.mixer.init()
pygame.init()

shoot_sound = pygame.mixer.Sound('sounds/shoot.wav')
invader_hit = pygame.mixer.Sound('sounds/invaderkilled.wav')
pygame.mixer.music.load('sounds/spaceinvaders1.mpeg')
pygame.mixer.music.play(-1, 0)
invader_hit.set_volume(.3)
shoot_sound.set_volume(.3)

def check_keydown_events(event, pi_settings, screen, ship, bullets, bombs, stats):
	volume = .5
	'''Respond to keypresses'''
	if event.key == pygame.K_ESCAPE:
		sys.exit()
	#Move the ship to the right
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	#Move the ship to the left
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	if event.key == pygame.K_y and stats.game_active == False:
		stats.ships_left += 4
		pi_settings.bombs_allowed = 1
		stats.score *= 0
		stats.game_active = True
	if event.key == pygame.K_UP:
		bomb(pi_settings, screen, ship, bombs)
	#Fire bullet
	elif event.key == pygame.K_SPACE:
		fire_bullet(pi_settings, screen, ship, bullets)
		
def fire_bullet (pi_settings, screen, ship, bullets):
#Create new bullet and add add it to bullets group
	if len(bullets) < pi_settings.bullets_allowed:
		new_bullet = Bullet(pi_settings, screen, ship)
		bullets.add(new_bullet)
		shoot_sound.play()

def bomb (pi_settings, screen, ship, bombs):
#Create new bullet and add add it to bullets group
	if len(bombs) < pi_settings.bombs_allowed:
		new_bomb = Bomb(pi_settings, screen, ship)
		bombs.add(new_bomb)
		shoot_sound.play()
		pi_settings.bombs_allowed -= 1

def check_keyup_events(event, ship):
	'''Respond to key releases'''
	if event.key == pygame.K_RIGHT:
		ship.image = pygame.image.load('images/ship_test.png')
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.image = pygame.image.load('images/ship_test.png')
		ship.moving_left = False
	if event.key == pygame.K_UP:	
		ship.moving_up = False
	if event.key == pygame.K_DOWN:	
		ship.moving_down = False
				
def check_events(pi_settings, screen, ship, bullets, bombs, stats):
	'''Respone to keyboard and Mouse'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, pi_settings, screen, ship, bullets, bombs, stats)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def game_over(pi_settings, screen, stats):
	white = (255,255,255)

	basicfont = pygame.font.SysFont(0, 70)
	game_over_text = basicfont.render('GAME OVER', True, white)
	reset_text = basicfont.render('Press Y to Replay', True, white)
	game_over_text_rect = game_over_text.get_rect()
	reset_text_rect = reset_text.get_rect()
	screen_rect = screen.get_rect()
	game_over_text_rect.centerx = screen_rect.centerx
	game_over_text_rect.top = screen_rect.top
	reset_text_rect.centerx = screen_rect.centerx
	reset_text_rect.top = game_over_text_rect.bottom
	if stats.game_active == False:
		screen.blit(game_over_text, game_over_text_rect)
		screen.blit(reset_text, reset_text_rect)

def update_screen(pi_settings, screen, ship, aliens, bullets, bombs):
	'''Update images on the screen and flip to the new screen'''
	#Redraw screen on each pass.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	for bomb in bombs.sprites():
		bomb.draw_bomb()
	ship.blitme()
	aliens.draw(screen)
	#Make the most recently drawn frame visable.
	pygame.display.flip()

def get_number_aliens_x(pi_settings, alien_width):
	"""Determine the number of aliens that fit in a row."""
	available_space_x = pi_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (alien_width))
	return number_aliens_x

def get_number_rows(pi_settings, ship_height, alien_height):
	"""Determine the number of rows of aliens that fit on the screen."""
	available_space_y = (pi_settings.screen_height - 
		(3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (alien_height))
	return number_rows

def create_alien(pi_settings, screen, aliens, alien_number, row_number):
	"""Create an alien and place it in the row."""
	alien = Alien(pi_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 1 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 1 * alien.rect.height * row_number
	aliens.add(alien)
	
def create_fleet(pi_settings, screen, ship, aliens):
	"""Create a full fleet of aliens."""
	#Create an alien and find the number of aliens in a row.
	alien = Alien(pi_settings, screen)
	number_aliens_x = get_number_aliens_x(pi_settings, alien.rect.width)
	number_rows = get_number_rows(pi_settings, ship.rect.height,
		alien.rect.height)
		
	# Create the first row of aliens.
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(pi_settings, screen, aliens, alien_number,
				row_number)
	
def update_bullets(pi_settings, screen, aliens, bullets, stats):
	'''Update bullet position and get rid of old bullets'''
	#Update bullet position
	bullets.update()
	
	#Get rid of old bullets
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	
	#Check if any bullets hit an alien
	#If so make bullet dissappear and alien
	
	if pygame.sprite.groupcollide(bullets, aliens, True, True):
		invader_hit.play()
		stats.score += 1
		#Add a bomb every hundred kills
		pattern1 = r"..00$"
		pattern2 = r".00$"
		pattern3 = r".000$"
		if re.match(pattern1, str(stats.score)) or re.match(pattern2, str(stats.score)):
			pi_settings.bombs_allowed += 1
		
		#Add a life every 1,000 points
		if re.match(pattern3, str(stats.score)):
			stats.ships_left += 1

	if len(aliens) == 0:
		#Destroy exisiting bullets and create new fleet
		bullets.empty()
		create_fleet(pi_settings, screen, ship, aliens)
		pi_settings.alien_speed_factor += .3
		if pi_settings.ship_speed_factor <= 4:
			pi_settings.ship_speed_factor += .1

def update_bombs(pi_settings, screen, aliens, bombs, stats):
	'''Update bomb position and get rid of old bombs'''
	#Update bombs position
	bombs.update()
	
	#Get rid of old bombs
	for bomb in bombs.copy():
		if bomb.rect.bottom <= 0:
			bomb.remove(bullet)
	
	#Check if any bombs hit an alien
	#If so make bombs dissappear and alien

	if pygame.sprite.groupcollide(bombs, aliens, True, True):
		invader_hit.play()
		stats.score += 1
		#Add a bomb every hundred kills
		pattern1 = r"..00$"
		pattern2 = r".00$"
		pattern3 = r".000"
		if re.match(pattern1, str(stats.score)) or re.match(pattern2, str(stats.score)):
			pi_settings.bombs_allowed += 1

		#Add a life every 1,000 points
		elif re.match(pattern3, str(stats.score)):
			stats.ships_left += 1

	if len(aliens) == 0:
		#Destroy exisiting bullets and create new fleet
		bombs.empty()
		create_fleet(pi_settings, screen, ship, aliens)
		pi_settings.alien_speed_factor += .3
		if pi_settings.ship_speed_factor <= 4:
			pi_settings.ship_speed_factor += .1

def kill_counter(pi_settings, screen, stats):
	white = (255,255,255)

	basicfont = pygame.font.SysFont(0, 30)
	score_text = basicfont.render('Score:' + str(stats.score), True, white)
	score_text_rect = score_text.get_rect()
	screen_rect = screen.get_rect()
	score_text_rect.centerx = screen_rect.centerx
	score_text_rect.top = screen_rect.top
	screen.blit(score_text, score_text_rect)

def bomb_counter(pi_settings, screen):
	white = (255,255,255)

	basicfont = pygame.font.SysFont(0, 30)
	bomb_text = basicfont.render('Bombs:' + str(pi_settings.bombs_allowed), True, white)
	bomb_text_rect = bomb_text.get_rect()
	screen_rect = screen.get_rect()
	bomb_text_rect.topleft = screen_rect.topleft
	bomb_text_rect.topleft = screen_rect.topleft
	screen.blit(bomb_text, bomb_text_rect)

def life_counter(pi_settings, screen, stats):
	white = (255,255,255)

	basicfont = pygame.font.SysFont(0, 30)
	life_text = basicfont.render('Lives:' + str(stats.ships_left), True, white)
	life_text_rect = life_text.get_rect()
	screen_rect = screen.get_rect()
	life_text_rect.topright = screen_rect.topright
	life_text_rect.topright = screen_rect.topright
	screen.blit(life_text, life_text_rect)
		
def check_fleet_edges(pi_settings, aliens):
	'''Respond to any alien reaching the edge of the screen'''
	for alien in aliens.sprites():
		if alien.check_edges(pi_settings):
			change_fleet_direction(pi_settings, aliens)
			break
			
def change_fleet_direction(pi_settings, aliens):
	'''Drop the fleet and change direction'''
	for alien in aliens.sprites():
		alien.rect.y += pi_settings.fleet_drop_speed
	pi_settings.fleet_direction *= -1

def ship_hit(pi_settings, stats, screen, ship, aliens, bullets):
		if stats.ships_left > 0:
				#Lower ships_left
				stats.ships_left -= 1
		
				#Empty the list of aliens and bullets
				aliens.empty()
				bullets.empty()

				#Creat a new fleet and center ship
				create_fleet(pi_settings, screen, ship, aliens)
				ship.center_ship()

				#Pause
				time.sleep(0.5)

		else:
				stats.game_active = False
def check_aliens_bottom(pi_settings, stats, screen, ship, aliens, bullets):
		"""Check if any aliens have reached the bottom of the screen."""
		screen_rect = screen.get_rect()
		for alien in aliens.sprites():
				if alien.rect.bottom >= screen_rect.bottom:
						# Treat this the same as if the ship got hit.
						ship_hit(pi_settings, stats, screen, ship, aliens, bullets)
						break

def update_aliens(pi_settings, stats, screen, ship, aliens, bullets, bombs):
	'''
	Check if the last alien in the fleet is at an edge
	and then update the positions of all aliens in the fleet
	'''
	check_fleet_edges(pi_settings, aliens)
	aliens.update()

	#Look for alien collision with ship
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(pi_settings, stats, screen, ship, aliens, bullets)

	#Look for aliens hitting bottom
	check_aliens_bottom(pi_settings, stats, screen, ship, aliens, bullets)
		

























