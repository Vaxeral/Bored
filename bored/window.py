import pygame

from pygame.locals import *

class Window:
	def __init__(self):

		 #  The returned object has screen resolution width and height attributes ie current_w and current_h
		info = pygame.display.Info()

		#  "or" together flags ie SCALED, RESIZABLE, and others with | operator.  SCALED fixes stuff with fullscreen but does other stuff idk about
		pygame.display.set_mode((info.current_w, info.current_h), RESIZABLE) #  SCALED cuases issues when trying to resize.
		pygame.display.set_caption("Bored")

		#  The icon is relative to the projects root directory.  Which means for it to load the image the game must be ran from the root of the project.

		#  for example . . .
		#  cd Bored
		#  python bored/main.py 
		icon = pygame.image.load("./resources/icon.png")
		pygame.display.set_icon(icon)
		self.surface = pygame.display.get_surface()

		#  The fourth number here is how opaque the color is.   Opaque is the oposite from transparent.
		#  the fourth value is known as alpha.  A value of 255 is max alpha just like with r, g, b
		self.fill = (255, 255, 255, 255) 

		self.fullscreen = False

#  This makes it so that we can call pygame.display module functions
pygame.display.init()


#  We call pygame.display module functions inside the Window __init__ method
instance = Window()
