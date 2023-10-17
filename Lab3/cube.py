from geometricfigure import GeometricFigure

class Cube(GeometricFigure):
    """Sub class to class Geometric figures, containing properties,attributes and 
	methods unique for the circle. The sides can also be of different length."""
    def __init__(self, x, y, z, side1, side2, side3):
        super().__init__(x, y)
        if not all(isinstance(value, self.allowed_types) for value in [z, side1, side2, side3]):
            raise TypeError('Allowed input on radius is integer or float.')
        
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError('Side1, side2 and side3 must all be positive values.')	
        
        self.z = z
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def z(self):
        return self._z
        
    @z.setter
    def z(self, z):
        self._z = z
    
    @property
    def area(self):
        return (self.side1 * self.side2)*2 + (self.side1 * self.side3)*2 + (self.side2 * self.side3)*2
    
    @property
    def volume(self):
        return self.side1 * self.side2 * self.side3
    
    @property
    def circumference(self):
        return min[(self.side1*2+self.side2*2),(self.side1*2+self.side3*2),(self.side2*2+self.side3*2)] #circumference defined as the smallest possible circumference

    def is_inside(self, other_x, other_y, other_z):
        return ((self.x - self.side1/2 <= other_x <= self.x + self.side1/2) and
                (self.y - self.side2/2 <= other_y <= self.y + self.side2/2) and
                (self.z - self.side3/2 <= other_z <= self.z + self.side3/2))
    
    def is_cubic(self):
        return self.side1 == self.side2 == self.side3

    def __str__(self):
        return f'x = {self.x}\ny = {self.y}\nz = {self.z}\narea = {self.area}\nvolume = {self.volume}'
        
    def __repr__(self):
        return f'x = {self.x}\ny = {self.y}\nz = {self.z}\narea = {self.area}\nvolume = {self.volume}'


        
            
