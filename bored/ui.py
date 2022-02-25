import pygame

from pygame.locals import *

from window import instance as window

class Button:
	def __init__(self, x, y, w, h, font, text, foreground_color, background_color, callback):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.font = font
		self.text = text
		self.foreground_color = foreground_color
		self.background_color = background_color
		self.callback = callback

	def update(self):
		x, y = pygame.mouse.get_pos()
		rect = pygame.Rect(self.x, self.y, self.w, self.h)
		if rect.collidepoint(x, y):
			self.callback(self)

	def render(self):
		width, height = window.surface.get_size()

		rect = pygame.Rect(self.x, self.y, self.w, self.h)

		# rect.centerx = rect.centerx * (width / 640)
		# rect.centery = rect.centery * (height / 480)

		pygame.draw.rect(window.surface, self.background_color, rect, border_radius=10)

		ANTIALIAS = True #  Makes the text look good

		surface = self.font.render(self.text, ANTIALIAS, self.foreground_color)

		# width, height = font.size(self.text)
		width, height = surface.get_size() #  Already have surface might as well use it

		assert self.w >= width and self.h >= height, "Text is bigger than button size !" #  Not sure if asserting is the right thing to do.  We could just let the text overflow.

		#  Position of top left corner of text surface to be centered on button rect

		x = self.x + self.w / 2 - width / 2
		y = self.y + self.h / 2 - height / 2

		window.surface.blit(surface, (x, y))

	def set_text(self, text):
		self.text = text

