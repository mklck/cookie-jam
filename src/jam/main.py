from .mapPainter	import MapPainter
from .model		import Point
from .entity		import Entity
from .textures		import textureManager
from .tile		import Tile, pixmapDB, TilePixmap
from .mapConstructor	import MapConstructor

def main():
	mc = MapConstructor()
	mc.feedJSON("scenes/main.json5")

	size = mc.readMapSize()
	tileSize = mc.readTileSize()

	m = MapPainter(size, tileSize)

	m.setMap(mc.getMap())

	m.show()
