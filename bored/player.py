import pygame

from pygame.locals import *

from window import instance as window

class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.w = 20
		self.h = 20

	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[K_w]:
			self.y -= .5 * dt
		if keys[K_a]:
			self.x -= .5 * dt
		if keys[K_s]:
			self.y += .5 * dt
		if keys[K_d]:
			self.x += .5 * dt

	def render(self):
		pygame.draw.rect(window.surface, (255, 0, 0, 255), pygame.Rect(self.x, self.y, self.w, self.h))