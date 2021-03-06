import pygame

from pygame.locals import *

from window import instance as window

import math

pygame.font.init()

global_font = pygame.sysfont.SysFont(None, 18)

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
		self.wiggle_count = 0
		self.dizzy = False
		self.dizzy_counter = 0
		self.hurt_counter = 0
		self.hurt = False
		self.happy = False
		self.happy_counter = 0
		self.is_offscreen = False
		self.offscreen_counter = 0
		self.go_to_center = False
		self.angry = False
		self.angry_counter = 0

	def update(self, dt):
		self.time_accumalated += dt

		width, height = window.surface.get_size()

		if self.x + self.r > width \
		or self.x - self.r < 0 \
		or self.y + self.r > height \
		or self.y - self.r < 0:
			self.is_offscreen = True
		else:
			self.is_offscreen = False

		if self.is_offscreen:
			self.go_to_center = True

		if self.go_to_center: self.offscreen_counter += dt
		else: self.offscreen_counter = 0
		if self.offscreen_counter > 4000:
			self.offscreen_counter = 0
			self.go_to_center = False
			self.angry = True

		if self.go_to_center:
			width, height = window.surface.get_size()
			hw, hh = width / 2, height / 2
			force = [0, 0]
			dx = hw - self.x
			dy = hh - self.y
			magnitude = .1
			direction = math.atan2(dy, dx)
			force[0] = magnitude * math.cos(direction)
			force[1] = magnitude * math.sin(direction)
			self.velocity[0] += force[0]
			self.velocity[1] += force[1]

		if self.n > math.pi * 2:
			self.n = 0.0
		self.n += 0.1
		self.r = self.r_change * math.sin(self.n) + self.r_base

		self.hurt_counter += dt
		if self.hurt_counter > 3000:
			self.hurt_counter = 0
			self.hurt = False


		if self.angry: self.angry_counter += dt
		else: self.angry_counter = 0
		if self.angry_counter > 3000:
			self.angry_counter = 0
			self.angry = False

		self.happy_counter += dt
		if self.happy_counter > 3000:
			self.happy_counter = 0
			self.happy = False

		self.dizzy_counter += dt
		if self.dizzy_counter > 3000:
			self.dizzy = False
			self.dizzy_counter = 0
			self.wiggle_count = 0

		keys = pygame.key.get_pressed()

		if keys[K_w]:
			self.y -= .5 * dt
		if keys[K_a]:
			self.x -= .5 * dt
		if keys[K_s]:
			self.y += .5 * dt
		if keys[K_d]:
			self.x += .5 * dt
		dir_previous = 0
		mag_previous = 0
		buttons = pygame.mouse.get_pressed()
		if buttons[0]:
			x, y = pygame.mouse.get_pos()
			force = [0, 0]
			dx = self.x - x
			dy = self.y - y
			magnitude = dx * dx + dy * dy
			magnitude = self.r_base * self.r_base / max(magnitude, self.r_base)
			if magnitude > self.r_base * .2:
				self.hurt = True
			direction = math.atan2(dy, dx)
			force[0] = magnitude * math.cos(direction)
			force[1] = magnitude * math.sin(direction)
			self.velocity[0] += force[0]
			self.velocity[1] += force[1]
			mag_upper = 200 * 200
			mag_lower = 25 * 25
			dir_lower = math.pi / 8
			magnitude = dx * dx + dy * dy
			if abs(magnitude - mag_previous) < 35 * 35:
				self.happy = True
			if self.time_accumalated > 10:
				self.time_accumalated = 0
				if magnitude < mag_upper and magnitude > mag_lower:
					if abs(direction - dir_previous) < dir_lower:
						self.wiggle_count += 1
			dir_previous = direction
			mag_previous = magnitude
		else:
			self.time_accumalated = 0

		self.x += self.velocity[0]
		self.y += self.velocity[1]

		self.velocity[0] /= 1.1
		self.velocity[1] /= 1.1
		if math.isclose(self.velocity[0], 0):
			self.velocity[0] = 0
		if math.isclose(self.velocity[1], 0):
			self.velocity[1] = 0

		if self.wiggle_count > 8:
			self.dizzy = True
			self.wiggle_count = 0

	def render(self):
		pygame.draw.circle(window.surface, self.color, (self.x, self.y), self.r)
		if self.hurt:
			surface = global_font.render("Hey That Hurt!", True, (0, 0, 0, 255))
			window.surface.blit(surface, (self.x, self.y))	
		# elif self.dizzy:
		# 	surface = global_font.render("That Makes Me Dizzy. :(", True, (0, 0, 0, 255))
		# 	window.surface.blit(surface, (self.x, self.y))
		elif self.happy:
			surface = global_font.render("Wee! :D", True, (0, 0, 0, 255))
			window.surface.blit(surface, (self.x, self.y))
		elif self.angry:
			surface = global_font.render("Fuck you!", True, (0, 0, 0, 255))
			window.surface.blit(surface, (self.x, self.y))