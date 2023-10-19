from geometricfigure import GeometricFigure

class Shape2D(GeometricFigure):
    def __init__(self, x, y):
        super().__init__(x, y)

    @property
    def area(self):
        return 0 #each subclass will contain its unique calculation of area
	
    @property
    def circumference(self):
        return 0 #each subclass will contain its unique calculation of circumference
    
    def is_inside(self):
        return 0 #each subclass will contain its unique calculation of is_inside

    def __eq__(self, other):
        return self.area == other.area
		#return self._get_compare_value() == other._get_compare_value()
			
    def __lt__(self, other):
       return self.area < other.area
		
    def __gt__(self, other):
        return self.area > other.area
		
    def __le__(self, other):
        return self.area <= other.area
		
    def __ge__(self, other):
        return self.area >= other.area