from dataclasses	import dataclass
from itertools		import product
from typing		import Literal, Union

Direction = Literal['north', 'south', 'east', 'west']
HeroState = Literal['normal', 'walk', 'fight']

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
	def __mul__(self, other):
		if type(other) is int:
			return Point(self.x * other, self.y * other)

@dataclass
class Pointf:
	x : float
	y : float
	def __add__(self, other):
		return Pointf(
			self.x + other.x,
			self.y, + other.y
		)
	def __mul__(self, other):
		return Pointf (
			self.x * other.x,
			self.y * other.y
		)


@dataclass
class Texture:
	path		: str
	direction	: Direction
	state		: HeroState
	stage		: Union[int, None] = None

class TextureManager:
	def __init__(self):
		self.textures = []

	def find(self, direction : Direction, state : HeroState):
		for t in self.textures:
			if t.direction != direction or t.state != state:
				continue
			yield t

	def addTexture(self, t : Texture):
		self.textures.append(t)

@dataclass
class Deadplace:
	start	: Point
	end	: Point

	def __contains__(self, p : Point):
		cond0 = self.start.x <= p.x <= self.end.x
		cond1 = self.start.y <= p.y <= self.end.y
		return cond0 and cond1
