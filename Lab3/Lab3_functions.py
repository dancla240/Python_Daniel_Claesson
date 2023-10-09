import math

class GeometricFigure:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def translation(self,delta_x, delta_y):
		self.x = self.x + delta_x
		self.y = self.y + delta_y
	
	def __str__(self):
		if hasattr(self.is_quadratic):
			return f'__str__ :\\nx = {self.x}\\ny = {self.y}\\nside1 = {self.side1}\\nside2 = {self.side2}\\narea = {self.area}'
		elif hasattr(self.is_unitcircle):
			return f'_str_ :\\nx = {self.x}\\ny = {self.y}\\nradius = {self.radius}\\narea = {self.area}'
	
	def __repr__(self):
		if hasattr(self.is_quadratic):
			return f'__repr__ :\\nx = {self.x}\\ny = {self.y}\\nside1 = {self.side1}\\nside2 = {self.side2}\\narea = {self.area}'
		elif hasattr(self.is_unitcircle):
			return f'__repr__ :\\nx = {self.x}\\ny = {self.y}\\nradius = {self.radius}\\narea = {self.area}'
		
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
		self.x = x
		self.y = y
		self.radius = radius
	
	@property
	def area(self):
		return self.radius**2 * math.pi
		
	# @area.setter
	# def area(self):
	# 	self._area = self.radius**2 * math.pi
	# 	return self._area
	
	@property	
	def circumference(self):
		return math.pi * 2 * self.radius
		
	# @circumference.setter
	# def circumference(self, self.radius):
	# 	self._circumference = math.pi * 2 * self.radius
			
	def is_inside(self, other_x, other_y):
		return math.sqrt((self.x - other_x)**2 + (self.y - other_y)**2) < self.radius
	
	def is_unitcircle(self):
		return self.radius == 1 and self.x == 0 and self.y == 0
		
class Rectangle(GeometricFigure):
	def __init__(self, x, y, side1, side2):
		self.x = x
		self.y = y
		self.side1 = side1
		self.side2 = side2
		
	@property
	def circumference(self):
		return self.side1*2 + self.side2*2
		
	# @circumference.setter
	# 	self._circumference = 
		
	@property
	def area(self):
		return self.side1 * self.side2
	
	# @area.setter
	# 	def self._area = side1 * side2
	
	def is_quadratic(self):
		return self.side1 == self.side2
		
	def is_inside(self, point):
		return f'to be done'
		