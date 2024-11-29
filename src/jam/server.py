from .map import Map

def server():
	limbo=Map(100,100)
	limbo.set_tile_colour(10, 15, "#FFFF00");
	limbo.draw()