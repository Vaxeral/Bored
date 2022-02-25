import pygame 

from pygame.locals import *

from window import instance as window

global_clock = pygame.time.Clock()

class SceneManager:
	def __init__(self):
		self.scenes = []
		self.scene_current = None

	def scene_push(self, scene):
		self.scenes.append(scene)
		self.scene_current = self.scenes[-1]
		names = [scene.name for scene in self.scenes]
		assert self.scene.name not in names, "Scene with name, {scene.name}, already exists."

	def scene_pop(self):
		last = self.scenes.pop()
		self.scene_current = self.scenes[-1]
		return last

	def scene_remove(self, name):
		for scene in self.scenes:
			if scenes.name == name:
				scene.to_remove = True
				break

	def update():
		self.scenes.sort(key=lambda scene: scene.to_remove)
		while True:
			if self.scenes[-1].to_remove:
				self.pop()
			else:
				break

	def scene_switch(self, name):
		index = None
		for i, scene in enumerate(self.scenes):
			if scene.name == name:
				index = i
				break
		temp = self.scenes[-1]
		self.scenes[-1] = self.scenes[index]
		self.scenes[index] = temp

scene_manager = SceneManager()

class Scene:
	def __init__(self, name):
		self.name = name
		self.to_remove = False
		self.passthrough = 0

	def handle_event(self, event):
		pass

	def update(self, dt):
		pass

	def render(sefl):
		pass

	def switch_scene(self, name):
		pass
