class GeometricFigure:
	"""Parent class for creating geometric figures.
	Contains attributes and methods common between
	different geometrical figures."""
	allowed_types = (int, float)

	def __init__(self, x, y, z=0):
		if not all(isinstance(value, self.allowed_types) for value in [x, y]):
			raise TypeError('Allowed coordinate inputs are integers or floats.')
		
		self.x = x
		self.y = y
		self.z = z

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

	@property
	def z(self):
		return self._z
	
	@z.setter
	def z(self, z):
		self._z = z

	@property
	def area(self):
		return 0 #each subclass will contain its unique calculation of area
	
	@property
	def circumference(self):
		return 0 #each subclass will contain its unique calculation of circumference
		
	def translation(self,delta_x, delta_y, delta_z = 0):
		if not all(isinstance(value, self.allowed_types) for value in [delta_x, delta_y]):
			raise TypeError('Allowed translation inputs are integers or floats.')
		
		self._x = self._x + delta_x
		self._y = self._y + delta_y
		self._z = self._z + delta_z

	def is_inside(self):
		return 0 #each subclass will contain its unique calculation of is_inside
	
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