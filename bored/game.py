#  Imports pygame.  Notice how you have to prefix certain things with pygame?  
#  Well thats becuase you have imported the module pygame with this statement.
import pygame 

#  Imports eveything from pygame.locals module into the file.  
#  This means for everything imported from pygame.locals can be directly use without the modules prefix. 
#  Using this type of import statement we can write ie QUIT instead of pygame.QUIT
#  This is known as a star import 
from pygame.locals import *

#  This imports the object instance from window module and renames it to window
#  This is our global window object used to blit images to the screen
from window import instance as window
from scene import Scene, global_clock

class Game:
	def __init__(self):
		self.is_running = False

	#  This is a empty method for now.  We will update our game objects here, such as the Player, Camera and other things.
	def update(self, dt):
		pass

	def render(self):
		window.surface.fill(window.fill)
		
		#  Render all UI and game objects

		pygame.display.update()

	def handle_event(self, event):
		if event.type == QUIT:
			self.is_running = False
		elif event.type == KEYDOWN:
			if event.key == K_a:
				pygame.display.toggle_fullscreen()

	def run(self):
		self.is_running = True

		#  main loop
		while self.is_running:
			for event in pygame.event.get():
				self.handle_event(event)

			#  This returns the time the last frame took to execute.  Passing 60 will delay the main loop to keep a constant frame rate of 60.
			dt = global_clock.tick(60) 

			#  We pass in dt or delta time to update all our objects positions scaled by the delta time.  
			#  This ensures that objects move at the same rate no matter how fast the main loop ran or in other words how fast your computer is.
			self.update(dt)
			self.render()
