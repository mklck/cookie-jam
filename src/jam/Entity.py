class Entity:
    def __init__(self, x_start, y_start, image_path):
        self.x = x_start
        self.y = y_start
        self.image_path = image_path # Ścieżka do obrazka reprezentującego obiekt
        self.graphics_item = None

    def initialize_graphics(self, scene, tile_size):
        """Dodaje graficzną reprezentację obiektu do sceny."""
        pixmap = QPixmap(self.image_path).scaled(tile_size, tile_size)  # Skalujemy obrazek do rozmiaru płytki
        self.graphics_item = QGraphicsPixmapItem(pixmap)
        self.graphics_item.setPos(self.y * tile_size, self.x * tile_size)  # Ustawiamy początkową pozycję
        scene.addItem(self.graphics_item)

    def move(self, new_x, new_y, duration_ms):
        """
        Przesuwa obiekt do nowej pozycji z animacją.
        :param new_x: Docelowa pozycja X.
        :param new_y: Docelowa pozycja Y.
        :param duration_ms: Czas trwania ruchu (w milisekundach).
        """
        if self.graphics_item is None:
            raise RuntimeError("Entity graphics not initialized. Call initialize_graphics first.")

        steps = 50  # Liczba kroków animacji
        dx = (new_x - self.x) / steps
        dy = (new_y - self.y) / steps
        interval = duration_ms / steps

        def update_position():
            nonlocal steps
            if steps > 0:
                self.x += dx
                self.y += dy
                self.graphics_item.setPos(self.y, self.x)
                steps -= 1
            else:
                timer.stop()

        timer = QTimer()
        timer.timeout.connect(update_position)
        timer.start(interval)
