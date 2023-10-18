import math
from geometricfigure import GeometricFigure

class Circle(GeometricFigure):
	"""Sub class to class Geometric figures, containing properties,
	attributes and methods unique for the circle.
	"""
	def __init__(self, x, y, radius):
		super().__init__(x, y)
		if not all(isinstance(value, self.allowed_types) for value in [radius]):
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
		return f'_str_ : x = {self._x}, y = {self._y}, radius = {self.radius}, area = {self.area}, circumference = {self.circumference}, is unitcircle = {self.is_unitcircle()}'
	
	def __repr__(self):
		return f'{self.__class__.__name__}(address={id(self)})'
		