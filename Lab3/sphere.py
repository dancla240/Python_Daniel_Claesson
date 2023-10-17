from geometricfigure import GeometricFigure
import math

class Sphere(GeometricFigure):
    """doc string"""
    def __init__(self, x, y, z, radius):
        super().__init__(x, y)
        if not all(isinstance(value, self.allowed_types) for value in [z, radius]):
            raise TypeError('Allowed input on radius is integer or float.')
        
        if radius <= 0:
            raise ValueError('Radius must be a positive value.')
  
        self.z = z
        self.radius = radius

    @property
    def z(self):
        return self._z
    
    @z.setter
    def z(self, z):
        self._z = z
    
    @property
    def area(self):
        return math.pi * 4 * self.radius**2
    
    @property
    def volume(self):
        return 4/3*math.pi * self.radius**3

    def is_inside(self, other_x, other_y, other_z):
        return math.sqrt((self.x - other_x)**2 + (self.y - other_y)**2 + (self.z - other_z)**2) < self.radius

    def circumference(self):
        return 2 * self.radius * math.pi
    
    def __str__(self):
        return f'_str_ :\nx = {self._x}\ny = {self._y}\nz = self._z\nradius = {self.radius}\ncircumference = {self.circumference}'
	
    def __repr__(self):
        return f'_str_ :\nx = {self._x}\ny = {self._y}\nz = self._z\nradius = {self.radius}\ncircumference = {self.circumference}'