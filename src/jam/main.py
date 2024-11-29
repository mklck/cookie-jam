from .mapPainter	import MapPainter
from .model		import Point
from .entity	import Entity

def main():
	size = Point(20, 20)
	m = MapPainter(size)
	for p in m.tileIterate():
		if(p.x%2==p.y%2):
			m.setTileColour(p, "#b123b7");

	Roman = Entity(path="graphics/64x64_RomanV2.png")
	Roman.setPos(Point(3,4))

	m.addEntity(Roman)
	m.draw()
