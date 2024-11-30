from .map	import Map
from .animator	import Animator, Movements

class Controller:
	def __init__(self, m : Map):
		self.map = m
		self.animator = Animator()
		
	def keyEvent(self, key):
		movements = {
			'w': 'north',
			's': 'south',
			'a': 'west',
			'd': 'east',
		}
		if key not in movements:
			return
		direction = movements[key]
		if not self.canMove(direction):
			return
		self.animator.animate(self.map.mainHero, direction)
	def canMove(self, direction):
		newPos = Movements[direction] + self.map.mainHero.pos
		return self.map.isPointInMap(newPos)
	def step(self):
		self.animator.step()
