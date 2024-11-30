from .mapPainter	import MapPainter
from .model		import Point
from .entity		import Entity

def main():
	size = Point(20, 20)
	m = MapPainter(size)
	
	Roman = Entity(path="graphics/64x64_RomanV2.png")
	Roman.setPos(Point(3,4))
	m.setMainHero(Roman)
	
	m.show()
