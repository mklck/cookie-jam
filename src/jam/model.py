from dataclasses	import dataclass
from itertools		import product

@dataclass
class Point:
	x : int
	y : int
	def iterate(self):
		for x, y in product(range(self.x), range(self.y)):
			yield Point(x, y)
	def __add__(self, other):
		return Point(
			self.x + other.x,
			self.y + other.y
		)
