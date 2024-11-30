from .tile	import TilePixmap
from .model	import TextureManager, HeroState, Direction

from math		import floor
from dataclasses	import dataclass

@dataclass(init=False)
class Entity(TilePixmap):
	direction	: Direction
	state		: HeroState
	def __init__(self, textures : TextureManager):
		super().__init__()
		self.state = 'normal'
		self.direction = 'south'
		self.textureManager = textures
		self.updateTexture()
	def setDirection(self, direction : Direction):
		self.direction = direction

	def setState(self, state : HeroState):
		self.state = state

	def updateTexture(self, stage : float = 0):
		t = self.textureManager.find(state=self.state, direction=self.direction)
		tlist = list(t)
		idx = floor((len(tlist) - 1) * stage)
		self.setPixmap(tlist[idx].path)
