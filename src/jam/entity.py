from .tile import TilePixmap

class Entity(TilePixmap):
	def __init__(self, path : str):
		super().__init__(path=path)
