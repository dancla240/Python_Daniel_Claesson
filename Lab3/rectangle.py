from geometricfigure2D import GeometricFigure2D

class Rectangle(GeometricFigure2D):
	"""Sub class to class Geometric figures, containing properties,
	attributes and methods unique for the rectangle."""
	def __init__(self, x, y, side1, side2):
		super().__init__(x, y)
		if not all(isinstance(value, self.allowed_types) for value in [side1, side2]):
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
		
