import pygame 

from pygame.locals import *

from window import instance as window

global_clock = pygame.time.Clock()

class SceneManager:
	def __init__(self):
		self.scenes = []
		self.scene_current = None

	def scene_push(self, scene):
		names = [scene.name for scene in self.scenes]
		assert scene.name not in names, "Scene with name, {scene.name}, already exists."

		scene.manager = self
		self.scenes.append(scene)
		self.scene_current = self.scenes[-1]
		self.scene_current.init()

	def scene_pop(self):
		last = self.scenes.pop()

		if len(self.scenes):
			self.scene_current = self.scenes[-1]
			self.scene_current.init()
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

	def scene_switch(self, name):
		assert len(self.scenes), "No scenes to switch to!"
		index = None
		for i, scene in enumerate(self.scenes):
			if scene.name == name:
				index = i
				break
		assert index, "Scene {name} was not found!"
		temp = self.scenes[-1]
		self.scenes[-1] = self.scenes[index]
		self.scenes[index] = temp
		self.scene_current = self.scenes[-1]
		self.scene_current.init()

	def scene_current_run(self, func_name, *agrs):
		if self.scene_current and hasattr(self.scene_current, func_name): getattr(self.scene_current, func_name)(*agrs)

scene_manager = SceneManager()

class Scene:
	def __init__(self, name):
		self.manager = None
		self.name = name
		self.to_remove = False

	def init(self):
		pass

	def handle_event(self, event):
		pass

	def update(self, dt):
		pass

	def render(sefl):
		pass

	def scene_switch(self, name):
		self.manager.scene_switch(name)

class Menu(Scene):
	def init(self):
		window.fill = (0, 0, 0, 255)

	def handle_event(self, event):
		if event.type == KEYDOWN:
			if event.key == K_m:
				scene_manager.scene_pop()
			elif event.key == K_p:
				print("Hello from main scene!")

	def update(self, dt):
		pass

	def render(self):
		width, height = window.surface.get_size()
		pygame.draw.rect(window.surface, (0, 0, 0, 255), pygame.Rect(0, 0, width, 10))