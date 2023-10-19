from shape3D import Shape3D

class Cube(Shape3D):
    """Sub class to class Geometric figures, containing properties,attributes and 
	methods unique for the cube. The sides can also be of different length.
    """
    def __init__(self, x, y, z, width, height, depth):
        super().__init__(x, y, z)
        if not all(isinstance(value, self.allowed_types) for value in [z, width, height, depth]):
            raise TypeError('Allowed input on radius is integer or float.')
        
        if width <= 0 or height <= 0 or depth <= 0:
            raise ValueError('width, height and depth must all be positive values.')	
        
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth

    @property
    def z(self):
        return self._z
        
    @z.setter
    def z(self, z):
        self._z = z
    
    @property
    def surface_area(self):
        return (self.width * self.height)*2 + (self.width * self.depth)*2 + (self.height * self.depth)*2
    
    @property
    def volume(self):
        return self.width * self.height * self.depth

    def is_inside(self, other_x, other_y, other_z):
        return ((self.x - self.width/2 <= other_x <= self.x + self.width/2) and
                (self.y - self.height/2 <= other_y <= self.y + self.height/2) and
                (self.z - self.depth/2 <= other_z <= self.z + self.depth/2))

    def is_cubic(self):
        return self.width == self.height == self.depth

    def __str__(self):
        return f'x = {self._x}, y = {self._y}, z = {self._z}, surface area = {self.surface_area}, volume = {self.volume}'

    def __repr__(self):
       	return f'{self.__class__.__name__}(address={id(self)})'