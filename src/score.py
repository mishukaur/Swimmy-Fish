import pygame
pygame.font.init()

class score:
	def __init__(self, font=pygame.font.SysFont("Arial", 30)):
		"""
		initializes score characteristics
		args: self
		return: none
		"""
		self.scorevalue = 0
		self.highscore = 0
		self.font = font
		self.textx = 0
		self.texty = 0

	def scorecounter(self, num):
		"""
		score increases 
		args: (num): int
		return: none
		"""
		self.scorevalue += num
	
	def drawScore(self, screen):
		"""
		this function makes the score visible on the screen
		args: (screen): screen object
		return: none
		"""
		self.score = self.font.render("Score: " + str(self.scorevalue), True, (255,255,255))
		screen.blit(self.score, (self.textx, self.texty))
		
	def saveScore(self):
		"""
		this function saves the high score in a text file 
		args: none
		return: none
		"""
		hsfile=open("assets/highscore.txt", "r")
		self.highscore = hsfile.readline()
		self.highscore = int(self.highscore)
		hsfile.close()
		if self.scorevalue == self.highscore:
			self.highscore = self.scorevalue
		elif self.scorevalue < self.highscore:
			self.highscore = self.highscore
		elif self.scorevalue > self.highscore:
			self.highscore = self.scorevalue
		hsfile=open("assets/highscore.txt", "w")
		hsfile.write(str(self.highscore) + "\n")
		hsfile.close()
