from .mapPainter	import MapPainter
from .model		import Point
from .entity		import Entity
from .textures		import textureManager

def main():
	size = Point(20, 20)
	m = MapPainter(size)
	
	Roman = Entity(textureManager)
	Roman.setPos(Point(3,4))
	m.setMainHero(Roman)
	
	m.show()
