class GeometricFigure2D:
	"""Parent class for creating geometric figures.
	Contains attributes and methods common between
	different geometrical figures."""
	allowed_types = (int, float)

	def __init__(self, x, y):
		if not all(isinstance(value, self.allowed_types) for value in [x, y]):
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
		if not all(isinstance(value, self.allowed_types) for value in [delta_x, delta_y]):
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