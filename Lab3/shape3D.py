from geometricfigure import GeometricFigure

class Shape3D(GeometricFigure):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        self._z = z

    @property
    def surface_area(self):
        return 0
    
    def translation(self,delta_x, delta_y, delta_z):
        if not all(isinstance(value, self.allowed_types) for value in [delta_x, delta_y]):
            raise TypeError('Allowed translation inputs are integers or floats.')

        self._x += delta_x
        self._y += delta_y
        self._z += delta_z

    def __eq__(self, other):
        return self.volume == other.volume

    def __lt__(self, other):
       return self.volume < other.volume
		
    def __gt__(self, other):
        return self.volume > other.volume
		
    def __le__(self, other):
        return self.volume <= other.volume
		
    def __ge__(self, other):
        return self.volume >= other.volume