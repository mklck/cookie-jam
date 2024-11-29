
class Tile:

    def __init__(self, colour="white"):
        self.colour = colour

    def __repr__(self):
        """
        Reprezentacja tekstowa płytki.
        """
        return f"Tile(colour='{self.colour}')"