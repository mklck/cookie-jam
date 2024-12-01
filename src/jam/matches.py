from PyQt6.QtWidgets import (
	QGraphicsLineItem, QMainWindow, QGraphicsView, QGraphicsScene, QPushButton, QVBoxLayout, QWidget
)
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPen, QColor


class MatchstickGame(QMainWindow):
	"""
	przykładowe wywołanie zapałek:
	app = QApplication(sys.argv)
	window = MatchstickGame("5+7=2",1)
	window.show()
	app.exec()

	przykładowe argumenty:
	("6+3=9",1)
	("5+7=2",1)
	("4-9=7",1)
	("0-9=5",1)
	("4X9=46",2)

	"""
	def __init__(self, equation, quantity):
		super().__init__()
		self.setWindowTitle("Matchstick Equation")
		self.setGeometry(100, 100, 800, 400)
		self.setStyleSheet("background-color: #1E1E1E;")
		# Inicjalizacja widoku i sceny
		self.scene = QGraphicsScene()
		self.view = QGraphicsView(self.scene, self)
		self.setCentralWidget(self.view)

		self.matches = {}  # Przechowywanie zapałek
		self.selected_match = None  # Aktualnie wybrana zapałka
		self.counter=1
		self.safequantity=quantity
		self.quantity=quantity
		# Przyciski
		self.reset_button = QPushButton("Resetuj")
		self.reset_button.clicked.connect(lambda: (self.reset_matches(), self.create_equation(equation)))

		layout = QVBoxLayout()
		layout.addWidget(self.view)
		layout.addWidget(self.reset_button)

		container = QWidget()
		container.setLayout(layout)
		self.setCentralWidget(container)

		self.create_equation(equation)

		# Ustawiamy zdarzenia kliknięcia myszką
		self.view.setMouseTracking(True)
		self.view.viewport().installEventFilter(self)
	def reset_matches(self):
		"""
		Resetuje wszystkie zapałki do początkowego ustawienia.
		"""
		self.scene.clear()  # Czyścimy scenę
		self.quantity=self.safequantity
		self.matches.clear()  # Usuwamy zapamiętane zapałki
		self.selected_match = None  # Resetujemy wybraną zapałkę


	def create_equation(self, equation):
		"""
		Tworzenie równania z zapałek.
		"""
		x_offset = 50
		y_offset = 150
		for char in equation:
			if char.isdigit():
				self.create_digit(int(char), x_offset, y_offset)
				x_offset += 150  # Przesunięcie po cyfrze
			elif char in {'+', '-', 'X', '/'}:
				self.create_operator(char, x_offset, y_offset)
				x_offset += 100  # Przesunięcie po operatorze
			elif char == '=':
				self.create_operator('=', x_offset, y_offset)
				x_offset += 100  # Przesunięcie po znaku równości

	def create_digit(self, number, x_offset, y_offset):
		"""
		Tworzenie cyfr za pomocą segmentów zapałek.
		"""
		segments = {
			'a': [(x_offset + 10, y_offset), (x_offset + 60, y_offset)],
			'b': [(x_offset + 60, y_offset), (x_offset + 60, y_offset + 50)],
			'c': [(x_offset + 60, y_offset + 50), (x_offset + 60, y_offset + 100)],
			'd': [(x_offset + 10, y_offset + 100), (x_offset + 60, y_offset + 100)],
			'e': [(x_offset, y_offset + 50), (x_offset, y_offset + 100)],
			'f': [(x_offset, y_offset), (x_offset, y_offset + 50)],
			'g': [(x_offset + 10, y_offset + 50), (x_offset + 60, y_offset + 50)],
		}
		self.counter=self.counter+1
		active_segments = self.get_active_segments(number)

		for segment, coords in segments.items():
			line = QGraphicsLineItem(*coords[0], *coords[1])
			owner = f"digit_{self.counter}"  # Unikalny identyfikator cyfry
			segment_key = (segment, owner)

			if segment in active_segments:
				line.setPen(QPen(QColor(203, 167, 92), 5))  # Kolor zapałki
			else:
				line.setPen(QPen(Qt.GlobalColor.black, 5))  # Kolor nieaktywnej linii

			self.matches[segment_key] = line
			self.scene.addItem(line)

	def get_active_segments(self, number):
		"""
		Returns the segments that are active for a given digit.
		"""
		segment_map = {
			0: ['a', 'b', 'c', 'd', 'e', 'f'],
			1: ['b', 'c'],
			2: ['a', 'b', 'd', 'e', 'g'],
			3: ['a', 'b', 'c', 'd', 'g'],
			4: ['b', 'c', 'f', 'g'],
			5: ['a', 'c', 'd', 'f', 'g'],
			6: ['a', 'c', 'd', 'e', 'f', 'g'],
			7: ['a', 'b', 'c'],
			8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
			9: ['a', 'b', 'c', 'd', 'f', 'g'],
		}
		return segment_map.get(number, [])

	def create_operator(self, operator, x_offset, y_offset):
		"""
		Tworzenie operatorów matematycznych.
		"""
		if operator == '+':
			segments = {
				'h': [(x_offset + 10, y_offset + 25), (x_offset + 50, y_offset + 25)],
				'v': [(x_offset + 30, y_offset), (x_offset + 30, y_offset + 50)],
			}
		elif operator == '-':
			segments = {
				'h': [(x_offset + 10, y_offset + 25), (x_offset + 50, y_offset + 25)],
				'v': [(x_offset + 30, y_offset), (x_offset + 30, y_offset + 50)],
			}
		elif operator == 'X':
			segments = {
				'd1': [(x_offset, y_offset), (x_offset + 50, y_offset + 50)],
				'd2': [(x_offset, y_offset + 50), (x_offset + 50, y_offset)],
			}
		elif operator == '/':
			segments = {
				'd': [(x_offset, y_offset + 50), (x_offset + 50, y_offset)],
			}
		elif operator == '=':
			segments = {
				'h1': [(x_offset, y_offset + 15), (x_offset + 50, y_offset + 15)],
				'h2': [(x_offset, y_offset + 35), (x_offset + 50, y_offset + 35)],
			}

		for segment, coords in segments.items():
			line = QGraphicsLineItem(*coords[0], *coords[1])
			owner = f"operator_{operator}"  # Unikalny identyfikator operatora
			segment_key = (segment, owner)

			line.setPen(QPen(QColor(203, 167, 92), 5))  # Kolor zapałki
			if operator=='-' and segment=='v':
				line.setPen(QPen(QColor(0, 0, 0), 5))
			self.matches[segment_key] = line
			self.scene.addItem(line)

	def eventFilter(self, source, event):
		"""
		Obsługuje kliknięcia na zapałki i puste miejsca.
		"""
		if event.type() == event.Type.MouseButtonPress:
			pos = self.view.mapToScene(event.pos())  # Mapa współrzędnych z widoku na scenę
			items = self.scene.items(pos)  # Pobieramy elementy w miejscu kliknięcia

			if items:
				clicked_item = items[0]
				# Kliknięcie na zapałkę
				if clicked_item.pen().color().name()=="#cba75c":
					if (not self.selected_match):
						# Wybieramy zapałkę
						self.selected_match = clicked_item
						clicked_item.setPen(QPen(Qt.GlobalColor.red, 5))  # Zaznaczamy zapałkę na czerwono
				elif clicked_item.pen().color().name()=="#ff0000":
					#print("odkliknięto zapałkę")
					self.selected_match = None
					clicked_item.setPen(QPen(QColor(203, 167, 92), 5))
					#print(self.check_logic(self.check_eqaution()))
				elif clicked_item.pen().color().name()=="#000000" and self.selected_match:
					clicked_item.setPen(QPen(QColor(203, 167, 92), 5))
					self.selected_match.setPen(QPen(Qt.GlobalColor.black, 5))
					self.selected_match = None  # Resetujemy wybraną zapałkę
					self.quantity=self.quantity-1
					if self.quantity==0:
						if self.check_logic(self.check_eqaution()):
							self.win()
						else:
							print("Równanie źle ułożone!")
							self.reset_button.click()


			return True
		return super().eventFilter(source, event)
####################
	def get_all_segment_colors(self):
		"""
		Pobiera kolory wszystkich segmentów.
		Zwraca słownik, gdzie kluczami są segmenty (np. 'a', 'b', 'c', ...)
		a wartościami są kolory (np. QColor).
		"""
		segment_colors = {}

		# Przechodzimy przez wszystkie elementy na scenie
		for match, item in self.matches.items():
			# Sprawdzamy kolor pióra (pen) danego elementu
			color = item.pen().color()

			# Przypisujemy kolor do segmentu na podstawie jego nazwy
			segment_name = match  # Segment (np. 'a', 'b', 'c', ...) jest już kluczem
			segment_colors[segment_name] = color
		#for (segment_name, owner), color in segment_colors.items():
			#print(f"Segment {segment_name} ({owner}): {color.name()}")
		return segment_colors
######################
	def check_eqaution(self):
		"""
		no sprawdza równanie a co ma robić innego
		"""
		digits_segment_map = {
			0: ['a', 'b', 'c', 'd', 'e', 'f'],
			1: ['b', 'c'],
			2: ['a', 'b', 'd', 'e', 'g'],
			3: ['a', 'b', 'c', 'd', 'g'],
			4: ['b', 'c', 'f', 'g'],
			5: ['a', 'c', 'd', 'f', 'g'],
			6: ['a', 'c', 'd', 'e', 'f', 'g'],
			7: ['a', 'b', 'c'],
			8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
			9: ['a', 'b', 'c', 'd', 'f', 'g'],
		}

		operators_segment_map = {
			'+': ['h', 'v'],
			'*': ['d1','d2'],
			'=': ['h1', 'h2'],
			'/': ['d'],
			'-': ['h'],
		}

		segment_colors = self.get_all_segment_colors()
		segments = []
		owners = []
		colours = []

		equation = []
		current_segments = []

		current_owner = None

		for (segment_name, owner), colour in segment_colors.items():
			if colour.name() == "#cba75c":  # tylko aktywne segmenty
				segments.append(segment_name)
				owners.append(owner)
				colours.append(colour.name())

		for i in range(len(segments)):
			segment = segments[i]
			owner = owners[i]

			if owner != current_owner:  # zmiana właściciela
				if current_owner is not None:
					temp = []
					# jeśli to cyfra, dopasuj segmenty
					if current_owner.startswith("digit"):
						for k, v in digits_segment_map.items():
							if set(current_segments) == set(v):
								equation.append(k)
								break
					# jeśli to operator, dopasuj segmenty
					elif current_owner.startswith("operator"):
						for k, v in operators_segment_map.items():
							if set(current_segments) == set(v):
								equation.append(k)
								break

				# zresetuj segmenty i ustaw nowego właściciela
				current_segments = []
				current_owner = owner

			# dodaj segment do aktualnej cyfry/operatora
			current_segments.append(segment)

		# przetwórz ostatnią cyfrę/operator
		if current_owner.startswith("digit"):
			for k, v in digits_segment_map.items():
				if set(current_segments) == set(v):
					equation.append(k)
					break
		elif current_owner.startswith("operator"):
			for k, v in operators_segment_map.items():
				if set(current_segments) == set(v):
					equation.append(k)
					break
		print(equation)
		return equation

	def check_logic(self,equation):
		k=0
		for i in range(len(equation)):
			if(equation[i]=='='):
				k=i;
		left  = equation[:k]
		right = equation[(k+1):]
		rightValue=0
		for i in range(len(right)):
			rightValue+=right[i]*10**(len(right)-1-i)
		operator=0
		number1=0
		number2=0
		pos=0
		for i in range(len(left)):
			if(left[i] in ['+','-','*','/']):
				pos=i
		for i in range(len(left)):
			if(left[i]=='+'):
				operator='+'
			elif(left[i]=='-'):
				operator = '-'
			elif (left[i] == '*'):
				operator = '*'
			elif (left[i] == '/'):
				operator = '/'
			else:
				if i<pos:
					number1 += left[i] * 10 ** (pos-i-1)
				else:
					number2 += left[i] * 10 ** (len(left)-i-1)
		if operator=='+':
			leftValue=number1+number2
		elif operator=='-':
			leftValue=number1-number2
		elif operator=='*':
			leftValue=number1*number2
		elif operator=='/':
			leftValue=number1/number2
		if leftValue==rightValue:
			return True
		else:
			return False
	def win(self):
		print("Gratulacje, rozwiązałeś równanie!")
		self.close()
		return True
