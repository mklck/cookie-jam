from .mapPainter	import MapPainter
from .model		import Point
from .Entity	import Entity

def main():
	size = Point(20, 20)
	m = MapPainter(size)
	for p in size.iterate():
		if(p.x%2==p.y%2):
			m.setTileColour(p, "#b123b7");
	Roman = Entity("graphics/64x64_RomanV2.png")
	m.addEntity(Roman)
	Roman.setPos(Point(3,4))
	m.draw()
