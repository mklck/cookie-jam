from .mapPainter	import MapPainter
from .model		import Point
from .entity		import Entity
from .textures		import textureManager
from .tile		import Tile, pixmapDB, TilePixmap

def main():
	size = Point(20, 12)
	m = MapPainter(size)

	tsize = Tile.getTileSize()

	bg = TilePixmap()
	bg.setPixmap('graphics/background.png')
	bg.setDesiredSize(size * tsize)

	m.setBackground(bg)
	
	Roman = Entity(textureManager)
	Roman.setPos(Point(3,4))
	Roman.setDesiredSize(Point(tsize, tsize))
	m.setMainHero(Roman)
	
	m.show()
