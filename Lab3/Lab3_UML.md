'Lab3 Python AI-23
'Author: Daniel Claesson
@startuml
class GeometricFigure {  
- x   
- y  
+translation(delta_x,delta_y)  
__str__()  
__repr__() 
}  

class Shape2D {
-area  
-circumference  
+is_inside()  
__eq__() '=='  
__lt__() '<'  
__gt__ () '>'  
__le__() '<='  
__ge__() '>='  
}

class Shape3D {
- z  
-volume
-surface_area
+translation(delta_z)  
+is_inside()
__eq__() '=='  
__lt__() '<'  
__gt__ () '>'  
__le__() '<='  
__ge__() '>='  
}
  
class Circle {  
+radius  
is_unitcircle()  
}  
  
class Rectangle {  
+width  
+height  
is_quadratic()  
}  

class Cube {  
+width  
+height  
+depth  
is_cubic()  
 
}

class Sphere {  
+radius  
+circumference  
}

    
GeometricFigure <|-- Shape2D
GeometricFigure <|-- Shape3D
Shape2D <|-- Circle  
Shape2D <|-- Rectangle  
Shape3D <|-- Cube
Shape3D <|-- Sphere
@enduml
