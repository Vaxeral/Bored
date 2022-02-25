import pygame

from pygame.locals import *

from window import instance as window

import math

class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.r = 10
		self.time_accumalated = 1000
		self.color = [255, 60, 2, 255]
		self.n = 0.0

	def update(self, dt):
		self.time_accumalated += dt
		if self.time_accumalated > 1000:
			if self.n > math.pi * 2:
				self.n = 0.0
			self.n += 0.1
			self.r = 10 * math.sin(self.n) + 25




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
		pygame.draw.circle(window.surface, self.color, (self.x, self.y), self.r)