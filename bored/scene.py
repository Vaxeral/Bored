import pygame 

from pygame.locals import *

from window import instance as window

from ui import Button

from player import Player

global_clock = pygame.time.Clock()

pygame.font.init()

global_font = pygame.sysfont.SysFont(None, 18)

#  TODO: Support preloading scenes
#  TODO: Handle screen resizing such that UI and game respond to it
#  TODO: Load Menu layout from xml files
#  NOTE: May not need layering effect for terraria clone.  Simple scene switching may be enough.
#  TODO: Fat Pointer Class for Chunks.  
#        Only store chunk data ie 2d dimensional list and only access the chunk data through the Chunk object.

class SceneManager:
	def __init__(self):
		self.scenes = []
		self.scene_current = None
		self.scene_switched = False

	def scene_push(self, scene):
		names = [scene.name for scene in self.scenes]
		assert scene.name not in names, "Scene with name, {scene.name}, already exists."

		self.scenes.append(scene)
		self.scene_current = self.scenes[-1]
		self.scene_switched = True

	def scene_pop(self):
		last = self.scenes.pop()

		if len(self.scenes):
			self.scene_current = self.scenes[-1]
			self.scene_switched = True
		else:
			self.scene_current = None
		return last

	def scene_remove(self, name):
		for scene in self.scenes:
			if scene.name == name:
				scene.to_remove = True
				break

	def scene_find_by_name(self, name):
		for scene in self.scenes:
			if scene.name == name:
				return scene

	def update(self):
		if len(self.scenes) == 0:
			return
		self.scenes.sort(key=lambda scene: scene.to_remove)
		while True:
			last = self.scenes[-1]
			if last.to_remove:
				if last.name == self.scene_current.name:
					self.scene_current = None #  If the current scene is removed the user should set a new scene.
				self.pop()
			else:
				break
		if self.scene_switched:
			if not self.scene_current.was_loaded:
				self.scene_current.load()
			self.scene_switched = False
			self.scene_current.start()

	def scene_switch(self, name):
		assert len(self.scenes) > 1, "No scenes to switch to!"
		index = None
		print(name)
		for i, scene in enumerate(self.scenes):
			if scene.name == name:
				index = i
				break
		assert index is not None, f"Scene {name} was not found!"
		temp = self.scenes[-1]
		self.scenes[-1] = self.scenes[index]
		self.scenes[index] = temp
		self.scene_current = self.scenes[-1]
		self.scene_switched = True

	def scene_current_run(self, func_name, *args):
		if self.scene_current and hasattr(self.scene_current, func_name): getattr(self.scene_current, func_name)(*args)

	def scene_all_run(self, func_name, *args):
		for scene in self.scenes:
			if hasattr(scene, func_name): getattr(scene, func_name)(*args)


scene_manager = SceneManager()

class Scene:
	def __init__(self, name, *, preload=False):
		self.name = name
		self.to_remove = False
		self.was_loaded = False
		self.preload = preload

	def load(self):
		self.was_loaded = True

	def start(self):
		pass

	def handle_event(self, event):
		pass

	def update(self, dt):
		pass

	def render(sefl):
		pass

class MenuScene(Scene):
	#  Could pass in settings here for menu layout, user settings, ...  Maybe parse an xml file for menu layout?
	def __init__(self, name):
		super().__init__(name, preload=True)
		if self.preload:
			self.load()

	def start(self):
		pass

	def load(self):
		super().load()

		self.birds = pygame.image.load("./resources/birds.jpg") #  Do these paths work on windows?
		self.bird = pygame.image.load("./resources/bird.jpg")

		self.background = self.bird

		width, height = window.surface.get_size()
		BUTTON_WIDTH = 250
		BUTTON_HEIGHT = 20
		BUTTON_X = width / 2 - BUTTON_WIDTH / 2
		BUTTON_Y = height / 2 - BUTTON_HEIGHT / 2
		self.button_play = Button( \
			BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, \
			global_font, "Play", (0, 0, 0, 255), (255, 255, 255, 255), \
			lambda button: (scene_manager.scene_pop(), scene_manager.scene_push(GameScene("Game"))))

		self.button_quit = Button( \
			BUTTON_X, BUTTON_Y + BUTTON_HEIGHT * 2, BUTTON_WIDTH, BUTTON_HEIGHT, \
			global_font, "Quit", (0, 0, 0, 255), (255, 255, 255, 255), \
			lambda button: scene_manager.scene_pop())

	def handle_event(self, event):
		if event.type == KEYDOWN:
			pass
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				self.button_play.update()
				self.button_quit.update()

	def update(self, dt):
		keys = pygame.key.get_pressed()

	def render(self):
		width, height = window.surface.get_size()
		surface = pygame.transform.scale(self.background, (width, height))
		window.surface.blit(surface, (0, 0))

		self.button_quit.render()
		self.button_play.render()


class GameScene(Scene):
	def __init__(self, name):
		super().__init__(name, preload=True)
		if self.preload:
			self.load()

	def load(self):
		super().load()
		self.player = Player(320, 240)

	def start(self):
		pass

	def handle_event(self, event):
		pass

	def update(self, dt):
		self.player.update(dt)

	def render(self):
		self.player.render()

