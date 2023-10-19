from shape2D import Shape2D

class Rectangle(Shape2D):
	"""Sub class to class Geometric figures, containing properties,
	attributes and methods unique for the rectangle.
	"""
	def __init__(self, x, y, width, height):
		super().__init__(x, y)
		if not all(isinstance(value, self.allowed_types) for value in [width, height]):
			raise TypeError('Allowed input on width and height is integer or float.')
		
		if width <= 0 or height <= 0:
			raise ValueError('width and height must be a positive value.')	
		
		self.width = width
		self.height = height
		
	@property
	def circumference(self):
		return self.width*2 + self.height*2
		
	@property
	def area(self):
		return self.width * self.height
	
	def is_quadratic(self):
		return self.width == self.height
		
	def is_inside(self, other_x, other_y):
		return other_x < (self._x + self.width/2) and other_x > (self._x - self.width/2) and other_y < (self._y + self.height/2) and other_y > (self._y - self.height/2)

	def __str__(self):
		return f'x = {self._x}, y = {self._y}, width = {self.width}, height = {self.height}, area = {self.area}, circumference = {self.circumference}, is quadratic = {self.is_quadratic()}'
		
	def __repr__(self):
			return f'{self.__class__.__name__}(address={id(self)})'
		
