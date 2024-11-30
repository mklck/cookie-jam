from .tile	import *
from .model	import *
from .entity	import Entity

Movements = {
	'west':		Point(-1, 0),
	'east':		Point(1, 0),
	'north':	Point(0, -1),
	'south':	Point(0, 1),
}


class MovementAnimation:
	def __init__(self, target : TilePixmap, duration = int):
		self.target = target
		self.duration = duration
		self.dir = None

	def animate(self, dir : str):
		self.dir = dir
		self.time = 0
	def getOffset(self):
		t = self.time / self.duration
		return Pointf(t, t) * Movements[self.dir]
	def step(self, delta = 1) -> bool:
		self.time += delta
		if self.time > self.duration:
			self.target.moveByOffset(Movements[self.dir])
			self.target.setSpriteOffset()
			self.dir = None
			return True
		self.target.setSpriteOffset(self.getOffset())
		return False
	def isAnimating(self, t : TilePixmap):
		return self.target == t

class Animator:
	moveDuration = 8 # In ticks
	def __init__(self):
		self.animations = []
	def isYetAnimated(self, obj):
		for a in self.animations:
			if a.isAnimating(obj):
				return True
		return False
	def animate(self, obj, direction = None):
		if self.isYetAnimated(obj):
			return
		if type(obj) is Entity:
			a = MovementAnimation(
				target=obj,
				duration=self.moveDuration
			) 
			a.animate(direction)
			self.animations.append(a)
	def step(self):
		for a in self.animations:
			if a.step():
				self.animations.remove(a)
