'Lab3 Python AI-23
'Author: Daniel Claesson
@startuml
class GeometricFigure {  
-x_pos  
-y_pos  
translation()  
__eq__() '=='
__lt__() '<'
__gt__ () '>'
__le__() '<='
__ge__() '>='
}  
  
class Circle {  
+radius  
+area  
+circumference  
is_inside()  
is_unitcircle()  
__str__()  
__repr__()  
}  
  
class Rectangle {  
+side1  
+side2  
+area  
+circumference  
is_inside()  
is_quadratic()  
__str__()  
__repr__()  
}  
    
GeometricFigure *-- Circle  
GeometricFigure *-- Rectangle  
  
@enduml

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
			return f'__str__ :\\nx = {self.x}\\ny = {self.y}\\nside1 = {self.side1}\\nside2 = {self.side2}\\narea = {self.area}\\n
		elif hasattr(self.is_unitcircle):
			return f'__str__ :\\nx = {self.x}\\ny = {self.y}\\nradius = {self.radius}\\narea = {self.area}\\n
	
	def __repr__(self):
		if hasattr(self.is_quadratic):
			return f'__repr__ :\\nx = {self.x}\\ny = {self.y}\\nside1 = {self.side1}\\nside2 = {self.side2}\\narea = {self.area}\\n
		elif hasattr(self.is_unitcircle):
			return f'__repr__ :\\nx = {self.x}\\ny = {self.y}\\nradius = {self.radius}\\narea = {self.area}\\n
		
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
		return self._area
		
	@area.setter
	def area(self):
		self._area = self.radius**2 * math.pi
		return self._area
	
	@property	
	def circumference(self):
		return self._circumference
		
	@circumference.setter
		self._circumference = math.pi * 2 * self.radius
			
	def is_inside(self, other_x, other_y):
		return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2) < self.radius
	
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
		return self._circumference
		
	@circumference.setter
		self._circumference = side1*2 + side2*2
		
	@property
	def area(self):
		return self._area
	
	@area.setter
		def self._area = side1 * side2
	
	def is_quadratic(self):
		return side1 == side2
		
	def is_inside(self, point):
		return f'to be done'
		