import pygame
import random
import sys
from src import fish
from src import shark
from src import sharktwo
from src import score
from src import button

BLACK = (0, 0, 0)
GREEN = (34, 177, 76)
LIGHTGREEN = (0, 255, 0)
RED = (200, 0, 0)
LIGHTRED = (255, 0, 0)
WHITE = (255, 255, 255)


class controller:

	def __init__(self, width=740, height=580):
		"""
		initializes start settings of game
		args: (width=740): int, width of screen; (height=580): int, height of screen
		return: none
		"""
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.sound = pygame.mixer.Sound("assets/assets_Water_Drop_1.wav")
		self.state = "START"

	def mainLoop(self):
		"""
		Sets state of game
		args: none
		return: none
		"""
		while True:
			if(self.state == "START"):
				self.gameStart()
			elif(self.state == "GAME"):
				self.gameLoop()
			elif(self.state == "OVER"):
				self.gameOver()

	def gameStart(self):
		"""
		Start screen; click button to begin
		args: none
		return: self.state (state of game when button clicked) 
		"""
		#sets up screen
		self.background = pygame.image.load("assets/oceanbackground.png").convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.screen.blit(self.background, (0,0))
		#gametitle
		font = pygame.font.SysFont(None, 24)
		txt = font.render('SWIMMY FISH', True, WHITE)
		self.screen.blit(txt, (330, 250))
		#displays button	
		button1 = button.button(self.screen, 340, 280, 100, 60, GREEN, LIGHTGREEN, action = "PLAY")
		pygame.display.flip()
		game_over = False
		while not game_over:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			cur = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			play = button1.hoverbutton(cur, click)
			if play:
				self.state = "GAME"
				return self.state
			pygame.display.flip()



	def gameOver(self):
		"""
		game over message box with end score appears; click button to quit or play again
		args: none
		returns: self.state (state of game when button clicked)
		"""
		#sets up screen
		self.score.saveScore()
		self.background = pygame.image.load("assets/oceanbackground.png").convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.screen.blit(self.background, (0,0))
		#messages
		font = pygame.font.SysFont(None, 24)
		txt = font.render('YOU LOSE', True, WHITE)
		txt2 = font.render("Score: " + str(self.score.scorevalue), True, WHITE)
		txt3 = font.render("High Score: " + str(self.score.highscore), True, WHITE)
		self.screen.blit(txt, (340, 140))
		self.screen.blit(txt2, (350, 170))
		self.screen.blit(txt3, (320, 200))
		#displays button	
		button1 = button.button(self.screen, 340, 250, 100, 60, GREEN, LIGHTGREEN, action = "PLAY AGAIN")
		button2 = button.button(self.screen, 340, 340, 100, 60, RED, LIGHTRED, action = "QUIT")
		pygame.display.flip()
		game_over = False
		while not game_over:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			cur = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			play = button1.hoverbutton(cur, click)
			if play:
				self.state = "GAME"
				return self.state
			exit = button2.hoverbutton(cur, click)
			if exit:
				self.state = "START"
				return self.state
			pygame.display.flip()
		

	def gameLoop(self):	
		"""
		Game screen: when click, fish moves up; sharks generate; player loses game if collides w sharks or goes off screen; player's points go up and sound plays as go through sharks
		args: none
		return: self.state (state of game so when click "play again", game starts new)
		"""
		#sets up screen
		self.background = pygame.image.load("assets/swimmyfish background.png").convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.sharkgroup = pygame.sprite.Group()
		self.sharktwogroup = pygame.sprite.Group()
		self.player = fish.fish("nemo", 0, 300)
		self.score = score.score()
		while self.state == "GAME":

			#generates new sharks; looks like fish is moving forward
			NEWSHARK = pygame.USEREVENT
			pygame.time.set_timer(NEWSHARK, 1800) 
			offset = 300
			x = self.width + 100
			while True: 
				for event in pygame.event.get(): 
					if event.type == NEWSHARK:
						y = random.randint(-100,0)
						self.sharkgroup.add(shark.shark("down", x, y + offset))
						self.sharktwogroup.add(sharktwo.sharktwo("up", x, y))

					#makes fish move up on click 
					if event.type == pygame.MOUSEBUTTONDOWN:
						self.player.moveUp()
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()

				#makes sure sharks dont overlap each other
				oldshark = None
				for i in self.sharkgroup:
					if oldshark and pygame.sprite.collide_rect(i, oldshark):
						i.kill()
					else: 
						oldshark = i
				oldshark = None
				for i in self.sharktwogroup:
					if oldshark and pygame.sprite.collide_rect(i, oldshark):
						i.kill()
					else: 
						oldshark = i
	
				#check if fish goes off screen
				if self.player.rect.y > self.height:
					self.state = "OVER"
					return

				#check for collisions
				if pygame.sprite.spritecollide(self.player, self.sharkgroup, False, collided=pygame.sprite.collide_mask):
					self.state = "OVER"
					return

				if pygame.sprite.spritecollide(self.player, self.sharktwogroup, False, collided=pygame.sprite.collide_mask):
					self.state = "OVER"
					return

				#play sound & score goes up
				play_sound = False
				for i in self.sharkgroup:
					if i.rect.centerx < self.player.rect.x:
						play_sound = True
						break
				if play_sound:
					self.score.scorecounter(1)
					self.sound.play()

				#updates screen
				self.sharkgroup.update()
				self.sharktwogroup.update()
				self.player.update()
				self.screen.blit(self.background, (0,0))
				self.sharkgroup.draw(self.screen)
				self.sharktwogroup.draw(self.screen)
				self.screen.blit(self.player.image, self.player.rect.topleft)
				self.score.drawScore(self.screen)
				pygame.display.flip()
