from .map	import MapPainter
from .model	import Point
from .Entity	import Entity

def main():
	size = Point(70, 70)
	m = MapPainter(size)
	for p in size.iterate():
		if(p.x%2==0 and p.y%2==0):
			m.setTileColour(p, "#b123b7");
	m.draw()
	#Roman = Entity(15, 15)
