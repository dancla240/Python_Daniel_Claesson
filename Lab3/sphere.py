from shape3D import Shape3D
import math

class Sphere(Shape3D):
    """Sub class to class Geometric figures, containing properties,
	attributes and methods unique for the sphere.
    """
    def __init__(self, x, y, z, radius):
        super().__init__(x, y, z)
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
    def surface_area(self):
        return math.pi * 4 * self.radius**2
    
    @property
    def volume(self):
        return 4/3*math.pi * self.radius**3

    def is_inside(self, other_x, other_y, other_z):
        return math.sqrt((self.x - other_x)**2 + (self.y - other_y)**2 + (self.z - other_z)**2) < self.radius

    def circumference(self):
        return 2 * self.radius * math.pi
    
    def __str__(self):
        return f'x = {self._x}, y = {self._y}, z = {self._z}, radius = {self.radius}, circumference = {self.circumference()}, surface area = {self.surface_area}'
	
    def __repr__(self):
        	return f'{self.__class__.__name__}(address={id(self)})'