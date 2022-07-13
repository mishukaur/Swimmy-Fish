import pygame
import random

class sharktwo(pygame.sprite.Sprite):
	def __init__(self, name, x, y):
		"""
		initializes shark characteristics
		args: (name): string, name of shark; (x): int, x value transforming image; (y): int, y value of transforming image
		return: none
		"""
		pygame.sprite.Sprite.__init__(self)
		self.imagefile = "assets/swimmyfish upshark4.png"
		self.image = pygame.image.load(self.imagefile).convert_alpha()
		self.image = pygame.transform.scale(self.image, (163,242))
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.name = name 
		self.speed = 1
		
	def update(self):
		"""
		updates & kills sharks as generate
		args: none
		return: none
		"""
		self.rect.x -= self.speed
		if self.rect.topright[0] < 0:
			self.kill()
