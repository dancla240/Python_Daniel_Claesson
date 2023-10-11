import math

class GeometricFigure:
	"""Parent class for creating geometric figures.
	Contains attributes and methods common between
	different geometrical figures."""
	allowed_types = (int, float)

	def __init__(self, x, y):
		if not all(isinstance(value, Circle.allowed_types) for value in [x, y]):
			raise TypeError('Allowed coordinate inputs are integers or floats.')
		
		self.x = x
		self.y = y

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, x):
		self._x = x

	@property
	def y(self):
		return self._y
	
	@y.setter
	def y(self, y):
		self._y = y
		
	def translation(self,delta_x, delta_y):
		if not all(isinstance(value, Circle.allowed_types) for value in [delta_x, delta_y]):
			raise TypeError('Allowed translation inputs are integers or floats.')
		
		self._x = self._x + delta_x
		self._y = self._y + delta_y
	
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
	"""Sub class to class Geometric figures, containing properties,
	attributes and methods unique for the circle."""

	def __init__(self, x, y, radius):
		super().__init__(x, y)
		if not all(isinstance(value, Circle.allowed_types) for value in [radius]):
			raise TypeError('Allowed input on radius is integer or float.')
		
		if radius <= 0:
			raise ValueError('Radius must be a positive value.')		

		self.radius = radius
	
	@property
	def area(self):
		return self.radius**2 * math.pi
	
	@property	
	def circumference(self):
		return math.pi * 2 * self.radius
					
	def is_inside(self, other_x, other_y):
		return math.sqrt((self._x - other_x)**2 + (self._y - other_y)**2) < self.radius
	
	def is_unitcircle(self):
		return self.radius == 1 and self._x == 0 and self._y == 0
	
	def __str__(self):
		return f'_str_ :\nx = {self._x}\ny = {self._y}\nradius = {self.radius}\narea = {self.area}\ncircumference = {self.circumference}\nis unitcircle = {self.is_unitcircle()}'
	
	def __repr__(self):
		return f'_repr_ :\nx = {self._x}\ny = {self._y}\nradius = {self.radius}\narea = {self.area}\ncircumference = {self.circumference}\nis unitcircle = {self.is_unitcircle()}'
		
class Rectangle(GeometricFigure):
	"""Sub class to class Geometric figures, containing properties,
	attributes and methods unique for the rectangle."""
	def __init__(self, x, y, side1, side2):
		super().__init__(x, y)
		if not all(isinstance(value, Circle.allowed_types) for value in [side1, side2]):
			raise TypeError('Allowed input on side1 and side2 is integer or float.')
		
		if side1 <= 0 or side2 <= 0:
			raise ValueError('Side1 and side2 must be a positive value.')	
		
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
		
	def is_inside(self, other_x, other_y):
		return other_x < (self._x + self.side1/2) and other_x > (self._x - self.side1/2) and other_y < (self._y + self.side2/2) and other_y > (self._y - self.side2/2)

	def __str__(self):
		return f'__str__ :\nx = {self._x}\ny = {self._y}\nside1 = {self.side1}\nside2 = {self.side2}\narea = {self.area}\ncircumference = {self.circumference}\nis quadratic = {self.is_quadratic()}'
		
	def __repr__(self):
		return f'__repr__ :\nx = {self._x}\ny = {self._y}\nside1 = {self.side1}\nside2 = {self.side2}\narea = {self.area}\ncircumference = {self.circumference}\nis quadratic = {self.is_quadratic()}'
		