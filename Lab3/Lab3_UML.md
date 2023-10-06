'Lab3 Python AI-23
'Author: Daniel Claesson
@startuml
class GeometricFigure {  
+x_pos  
+y_pos  
+z_pos  
move()  
__str__()  
__repr__()  
}  
  
class Circle {  
+radius  
+area  
+circumference  
+is_unitcircle  
is_in_figure()  
check_unitcircle()  
}  
  
class Rectangle {  
+width  
+height  
+area  
+circumference  
+quadratic  
is_in_figure()  
check_quadratic()  
}  
  
class Sphere {  
+volume  
}  
  
class Cube {  
+volume  
}  
  
GeometricFigure *-- Circle  
GeometricFigure *-- Rectangle  
GeometricFigure *-- Sphere  
GeometricFigure *-- Cube  
  
@enduml