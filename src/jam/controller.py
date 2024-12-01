from .map	import Map
from .animator	import Animator, Movements

class Controller:
	def __init__(self):
		self.animator = Animator()
		self.clearPaper()

	def clearPaper(self):
		self.steppedPaper = None

	def setMap(self, m):
		self.map = m

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
		return not self.map.isPointDead(newPos)

	def step(self):
		print(f'pos = {self.map.mainHero.pos}', end='\r')
		self.animator.step()
		for p in self.map.paper:
			if p.pos == self.map.mainHero.pos:
				self.steppedPaper = p
				self.map.paper.remove(p)
				break
