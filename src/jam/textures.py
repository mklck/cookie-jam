from .model	import Texture, TextureManager

t = [
	Texture('graphics/roman front/roman_front.png', 'south', 'normal'),

	Texture('graphics/roman front/roman_walk1.png', 'south', 'walk', 0),
	Texture('graphics/roman front/roman_walk2.png', 'south', 'walk', 1),

	Texture('graphics/roman back/roman_back.png', 'north', 'normal'),

	Texture('graphics/roman back/roman_back_walk1.png', 'north', 'walk', 0),
	Texture('graphics/roman back/roman_back_walk2.png', 'north', 'walk', 1),

	Texture('graphics/roman left/roman_left1.png', 'west', 'normal'),

	Texture('graphics/roman left/roman_left_walk1.png', 'west', 'walk', 0),
	Texture('graphics/roman left/roman_left_walk2.png', 'west', 'walk', 1),
	Texture('graphics/roman left/roman_left_walk3.png', 'west', 'walk', 2),
	Texture('graphics/roman left/roman_left_walk4.png', 'west', 'walk', 3),

	Texture('graphics/roman right/roman_right1.png', 'east', 'normal'),

	Texture('graphics/roman right/roman_right_walk1.png', 'east', 'walk', 0),
	Texture('graphics/roman right/roman_right_walk2.png', 'east', 'walk', 1),
	Texture('graphics/roman right/roman_right_walk3.png', 'east', 'walk', 2),
	Texture('graphics/roman right/roman_right_walk4.png', 'east', 'walk', 3),
]

textureManager = TextureManager()

for x in t:
	textureManager.addTexture(x)
