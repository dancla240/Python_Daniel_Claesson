'Lab3 Python AI-23
'Author: Daniel Claesson
@startuml
class GeometricFigure {  
-x_pos  
-y_pos  
-z_pos
-area  
-circumference  
+translation(delta_x,delta_y,delta_z)  
+is_inside()  
__eq__() '=='  
__lt__() '<'  
__gt__ () '>'  
__le__() '<='  
__ge__() '>='  
__str__()  
__repr__()  
}  
  
class Circle {  
+radius  
is_unitcircle()  
}  
  
class Rectangle {  
+side1  
+side2  
is_quadratic()  
}  

class Cube {  
+side1  
+side2  
+side3  
is_cubic()
volume()    
}

class Sphere {  
+radius  
volume()  
}

    
GeometricFigure <|-- Circle  
GeometricFigure <|-- Rectangle  
GeometricFigure <|-- Cube
GeometricFigure <|-- Sphere
  
@enduml
