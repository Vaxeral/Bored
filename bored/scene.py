import pygame 

from pygame.locals import *

from window import instance as window

from ui import Button

global_clock = pygame.time.Clock()

pygame.font.init()

global_font = pygame.sysfont.SysFont(None, 12)

#  TODO: Support preloading scenes

class SceneManager:
	def __init__(self):
		self.scenes = []
		self.scene_current = None
		self.scene_switched = False

	def scene_push(self, scene):
		names = [scene.name for scene in self.scenes]
		assert scene.name not in names, "Scene with name, {scene.name}, already exists."

		scene.manager = self
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
					self.scene_current = None
				self.pop()
			else:
				break
		if self.scene_switched and not self.scene_current.was_init:
			self.scene_current.init()
			self.scene_switched = False

	def scene_switch(self, name):
		assert len(self.scenes), "No scenes to switch to!"
		index = None
		for i, scene in enumerate(self.scenes):
			if scene.name == name:
				index = i
				break
		assert index is not None, "Scene {name} was not found!"
		temp = self.scenes[-1]
		self.scenes[-1] = self.scenes[index]
		self.scenes[index] = temp
		self.scene_current = self.scenes[-1]
		self.scene_switched = True

	def scene_current_run(self, func_name, *agrs):
		if self.scene_current and hasattr(self.scene_current, func_name): getattr(self.scene_current, func_name)(*agrs)

scene_manager = SceneManager()

class Scene:
	def __init__(self, name):
		self.manager = None
		self.name = name
		self.to_remove = False
		self.was_init = False

	def init(self):
		self.was_init = True

	def handle_event(self, event):
		pass

	def update(self, dt):
		pass

	def render(sefl):
		pass

	def scene_switch(self, name):
		self.manager.scene_switch(name)

class Menu(Scene):
	def __init__(self, name, message):
		super().__init__(name)
		self.message = message
		width, height = window.surface.get_size()
		BUTTON_WIDTH = 80
		BUTTON_HEIGHT = 20
		BUTTON_X = width / 2 - BUTTON_WIDTH / 2
		BUTTON_Y = height / 2 - BUTTON_HEIGHT / 2
		self.button = Button(BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, global_font, "Hello Click Me", (0, 0, 0, 255), (255, 255, 255, 255), lambda button: button.set_text(message))

	def init(self):
		super().init()
		window.fill = (0, 0, 0, 255)
		print(self.message)

	def handle_event(self, event):
		if event.type == KEYDOWN:
			if event.key == K_m:
				self.scene_switch("MainMenu")
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				self.button.update()

	def update(self, dt):
		pass

	def render(self):
		self.button.render()
		width, height = window.surface.get_size()
		pygame.draw.rect(window.surface, (255, 255, 255, 255), pygame.Rect(0, 0, width, 10))
