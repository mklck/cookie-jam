def main():
	print("Hello World!")
	## moje zmiany:
	from map_old import Map
	from Entity import Entity
	n=70
	m=70
	testmap=Map(n,m)
	for i in range (n):
		for j in range (m):
			if(i%2==0 and j%2==0):
				testmap.set_tile_colour(i,j,"#b123b7");
	Roman = Entity(15, 15,)