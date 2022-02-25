import pygame

from pygame.locals import *

from window import instance as window

import math

class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.r = 10
		self.r_base = 25
		self.r_change = 10
		self.time_accumalated = 1000
		self.color = [255, 60, 2, 255]
		self.n = 0.0
		self.velocity = [0, 0]

	def update(self, dt):
		self.time_accumalated += dt
		if self.n > math.pi * 2:
			self.n = 0.0
		self.n += 0.1
		self.r = self.r_change * math.sin(self.n) + self.r_base

		keys = pygame.key.get_pressed()

		if keys[K_w]:
			self.y -= .5 * dt
		if keys[K_a]:
			self.x -= .5 * dt
		if keys[K_s]:
			self.y += .5 * dt
		if keys[K_d]:
			self.x += .5 * dt

		buttons = pygame.mouse.get_pressed()
		if buttons[0]:
			x, y = pygame.mouse.get_pos()
			force = [0, 0]
			dx = self.x - x
			dy = self.y - y
			magnitude = dx * dx + dy * dy
			magnitude = self.r_base * self.r_base / max(magnitude, self.r_base)
			direction = math.atan2(dy, dx)
			force[0] = magnitude * math.cos(direction)
			force[1] = magnitude * math.sin(direction)
			self.velocity[0] += force[0]
			self.velocity[1] += force[1]

		self.x += self.velocity[0]
		self.y += self.velocity[1]

		self.velocity[0] /= 1.1
		self.velocity[1] /= 1.1
		if math.isclose(self.velocity[0], 0):
			self.velocity[0] = 0
		if math.isclose(self.velocity[1], 0):
			self.velocity[1] = 0

	def render(self):
		pygame.draw.circle(window.surface, self.color, (self.x, self.y), self.r)

