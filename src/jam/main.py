from .game		import Game
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

	path = "graphics/RomanIJola_overlay_compressed.mp4"
	
	g = Game(size, tileSize)

	g.setMap(mc.getMap())

	g.show()
