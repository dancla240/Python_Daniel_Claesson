import math

"""docstrings"""
"""man ska göra tester på te xom man skriver in en sträng som """

class GeometricFigure:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def translation(self,delta_x, delta_y):
		self.x = self.x + delta_x
		self.y = self.y + delta_y
	
	def __eq__(self, other):
		return self.area == other.area
			
	def __lt__(self, other):
		return self.area < other.area
		
	def __gt__(self, other):
		return self.area > other.area
		
	def __le__(self, other):
		return self.area <= other.area
		
	def __ge__(self, other):
		return self.area >= other.area
	
class Circle(GeometricFigure):
	def __init__(self, x, y, radius):
		super().__init__(x, y)
		self.radius = radius
	
	@property
	def area(self):
		return self.radius**2 * math.pi
	
	@property	
	def circumference(self):
		return math.pi * 2 * self.radius
					
	def is_inside(self, other_x, other_y):
		return math.sqrt((self.x - other_x)**2 + (self.y - other_y)**2) < self.radius
	
	def is_unitcircle(self):
		return self.radius == 1 and self.x == 0 and self.y == 0
	
	def __str__(self):
		return f'_str_ :\nx = {self.x}\ny = {self.y}\nradius = {self.radius}\narea = {self.area}\ncircumference = {self.circumference}\nis unitcircle = {self.is_unitcircle()}'
	
	def __repr__(self):
		return f'_repr_ :\nx = {self.x}\ny = {self.y}\nradius = {self.radius}\narea = {self.area}\ncircumference = {self.circumference}\nis unitcircle = {self.is_unitcircle()}'
		
class Rectangle(GeometricFigure):
	def __init__(self, x, y, side1, side2):
		super().__init__(x, y)
		self.side1 = side1
		self.side2 = side2
		
	@property
	def circumference(self):
		return self.side1*2 + self.side2*2
		
	@property
	def area(self):
		return self.side1 * self.side2
	
	def is_quadratic(self):
		return self.side1 == self.side2
		
	def is_inside(self, point):
		return f'to be done'

	def __str__(self):
		return f'__str__ :\nx = {self.x}\ny = {self.y}\nside1 = {self.side1}\nside2 = {self.side2}\narea = {self.area}\ncircumference = {self.circumference}\nis quadratic = {self.is_quadratic()}'
		#return f'__str__ :\nx = {self.x}\ny = {self.y}\nside1 = {self.side1}\nside2 = {self.side2}\narea = {self.area}'
	def __repr__(self):
		return f'__repr__ :\nx = {self.x}\ny = {self.y}\nside1 = {self.side1}\nside2 = {self.side2}\narea = {self.area}\ncircumference = {self.circumference}\nis quadratic = {self.is_quadratic()}'
		