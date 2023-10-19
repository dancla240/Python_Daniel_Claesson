from circle import Circle
from rectangle import Rectangle
from cube import Cube
from sphere import Sphere
import math
import pytest

#test of 2d shapes
def test_instantiate_circle_with_invalid_radius_input():
    with pytest.raises(ValueError):
        circle = Circle(1,1,0)
    with pytest.raises(TypeError):
        circle = Circle(1,1,'one')
    with pytest.raises(ValueError):
        circle = Circle(1,1,-1)

def test_instantiate_circle_with_invalid_coordinate_input():
    with pytest.raises(TypeError):
        circle = Circle('one',1,1)
    with pytest.raises(TypeError):
        circle = Circle(1,'one',1)

def test_instantiate_rectangle_with_invalid_side_input():
    with pytest.raises(ValueError):
        rectangle = Rectangle(1,1,0,0)
    with pytest.raises(ValueError):
        rectangle = Rectangle(1,1,-1,1)
    with pytest.raises(ValueError):
        rectangle = Rectangle(1,1,1,-1)
    with pytest.raises(TypeError):
        rectangle = Rectangle(1,1,'one',1)
    with pytest.raises(TypeError):
        rectangle = Rectangle(1,1,1,'one')

def test_translation_with_invalid_coordinates():
    circle = Circle(0,0,1)
    with pytest.raises(TypeError):
        circle.translation(-1,'one')
    with pytest.raises(TypeError):
        circle.translation('one',-1)

def test_translation():
    circle = Circle(0,0,1)
    circle.translation(-1,-1)
    assert circle.x == -1
    assert circle.y == -1
    circle.translation(5,5)
    assert circle.x == 4
    assert circle.y == 4

def test_circles_equal():
    circle1 = Circle(0,0,2)
    circle2 = Circle(1,1,2)
    circle3 = Circle(0,0,2)
    circle4 = Circle(1,1,3)
    assert circle1 == circle2
    assert circle2 == circle3
    assert circle1 == circle3
    assert circle1 != circle4
    assert circle2 != circle4
    assert circle3 != circle4

def test_rectangles_equal():
    rectangle1 = Rectangle(0,0,1,1)
    rectangle2 = Rectangle(1,1,1,1)
    rectangle3 = Rectangle(0,0,2,3)
    assert rectangle1 == rectangle2
    assert rectangle1 != rectangle3
    assert rectangle2 != rectangle3

def test_circles_rectangles_equal():
    circle = Circle(0,0,1)
    rectangle = Rectangle(0,0,2,3)
    assert circle != rectangle

def test_circles_larger_than():
    circle1 = Circle(0,0,2)
    circle2 = Circle(1,1,2)
    circle3 = Circle(0,0,2)
    circle4 = Circle(1,1,3)
    assert not circle1 > circle2
    assert not circle2 > circle3
    assert not circle1 > circle3
    assert not circle1 > circle4
    assert not circle2 > circle4
    assert not circle3 > circle4
    assert circle4 > circle3
    assert circle4 > circle2
    assert circle4 > circle1

def test_rectangles_larger_than():
    rectangle1 = Rectangle(0,0,1,1)
    rectangle2 = Rectangle(1,1,1,1)
    rectangle3 = Rectangle(0,0,2,3)
    assert not rectangle1 > rectangle2
    assert not rectangle1 > rectangle3
    assert not rectangle2 > rectangle1
    assert not rectangle2 > rectangle3
    assert rectangle3 > rectangle2
    assert rectangle3 > rectangle1

def test_circles_rectangles_larger_than():
    circle = Circle(0,0,1)
    rectangle = Rectangle(0,0,2,3)
    assert not circle > rectangle
    assert rectangle > circle

def test_circles_equal_or_smaller_than():
    circle1 = Circle(0,0,2)
    circle2 = Circle(1,1,2)
    circle3 = Circle(0,0,2)
    circle4 = Circle(1,1,3)
    assert circle1 <= circle2
    assert circle2 <= circle3
    assert circle1 <= circle3
    assert circle1 <= circle4
    assert circle2 <= circle4
    assert circle3 <= circle4
    assert not circle4 <= circle3
    assert not circle4 <= circle2
    assert not circle4 <= circle1

def test_rectangles_equal_or_smaller_than():
    rectangle1 = Rectangle(0,0,1,1)
    rectangle2 = Rectangle(1,1,1,1)
    rectangle3 = Rectangle(0,0,2,3)
    assert rectangle1 <= rectangle2
    assert rectangle1 <= rectangle3
    assert rectangle2 <= rectangle1
    assert rectangle2 <= rectangle3
    assert not rectangle3 <= rectangle2
    assert not rectangle3 <= rectangle1

def test_circles_rectangles_equal_or_smaller_than():
    circle = Circle(0,0,1)
    rectangle = Rectangle(0,0,2,3)
    assert circle <= rectangle
    assert not rectangle <= circle

def test_circles_equal_or_larger_than():
    circle1 = Circle(0,0,2)
    circle2 = Circle(1,1,2)
    circle3 = Circle(0,0,2)
    circle4 = Circle(1,1,3)
    assert circle1 >= circle2
    assert circle2 >= circle3
    assert circle1 >= circle3
    assert not circle1 >= circle4
    assert not circle2 >= circle4
    assert not circle3 >= circle4
    assert circle4 >= circle3
    assert circle4 >= circle2
    assert circle4 >= circle1

def test_rectangles_equal_or_larger_than():
    rectangle1 = Rectangle(0,0,1,1)
    rectangle2 = Rectangle(1,1,1,1)
    rectangle3 = Rectangle(0,0,2,3)
    assert rectangle1 >= rectangle2
    assert not rectangle1 >= rectangle3
    assert rectangle2 >= rectangle1
    assert not rectangle2 >= rectangle3
    assert rectangle3 >= rectangle2
    assert rectangle3 >= rectangle1

def test_circles_rectangles_equal_or_larger_than():
    circle = Circle(0,0,1)
    rectangle = Rectangle(0,0,2,3)
    assert not circle >= rectangle
    assert rectangle >= circle

def test_circle_unitcircle():
    circle = Circle(0,0,1)
    assert circle.is_unitcircle() == True
    circle = Circle(1,1,1)
    assert circle.is_unitcircle() == False

def test_circle_area():
    circle = Circle(0,0,1)
    assert circle.area == 1**2 * math.pi

def test_circle_circumference():
    circle = Circle(0,0,1)
    assert circle.circumference == 2 * 1 * math.pi

def test_circle_is_inside():
    circle = Circle(0,0,1)
    assert circle.is_inside(0,0) == True
    assert circle.is_inside(1,1) == False
    assert circle.is_inside(1,0) == False
    assert circle.is_inside(0.5,0.5) == True
    assert circle.is_inside(0.9999,0) == True
    
def test_rectangle_is_quadratic():
    rectangle = Rectangle(1,1,1,1)
    assert rectangle.is_quadratic() == True

def test_rectangle_area():
    rectangle = Rectangle(1,1,1,1)
    assert rectangle.area == 1

def test_rectangle_circumference():
    rectangle = Rectangle(1,1,1,1)
    assert rectangle.circumference == 4

def test_rectangele_is_inside():
    rectangle = Rectangle(0,0,1,1)
    assert rectangle.is_inside(0,0) == True
    assert rectangle.is_inside(0.4999,0.4999) == True
    assert rectangle.is_inside(0.5,0.5) == False

def test_rectangle_str():
    rectangle = Rectangle(0,1,1,1)
    assert str(rectangle) == 'x = 0, y = 1, width = 1, height = 1, area = 1, circumference = 4, is quadratic = True'

def test_circle_str():
    circle = Circle(0,0,1)
    assert str(circle) == 'x = 0, y = 0, radius = 1, area = 3.141592653589793, circumference = 6.283185307179586, is unitcircle = True'

# test of 3d shapes
def test_instantiate_sphere_with_invalid_radius_input():
    with pytest.raises(TypeError):
        sphere = Sphere(0,0,0,'one')
    with pytest.raises(ValueError):
        sphere = Sphere(0,0,0,-1)
    with pytest.raises(ValueError):
        sphere = Sphere(0,0,0,0)

def test_instantiate_sphere_with_invalid_coordinate_input():
    with pytest.raises(TypeError):
        sphere = Sphere('zero',0,0,1)
    with pytest.raises(TypeError):
        sphere = Sphere(0,'zero',0, 1)

def test_instantiate_cube_with_invalid_coordinate_input():
    with pytest.raises(TypeError):
        cube = Cube('zero',0,0,1,1,1)
    with pytest.raises(TypeError):
        cube = Cube([0],0,0,1,1,1)

def test_instantiate_cube_with_invalid_side_input(): #28
    with pytest.raises(ValueError):
        cube = Cube(0,0,0,0,1,1)
    with pytest.raises(ValueError):
        cube = Cube(0,0,0,1,0,1)
    with pytest.raises(ValueError):
        cube = Cube(0,0,0,1,1,0)
    with pytest.raises(ValueError):
        cube = Cube(0,0,0,0,0,0)   
    with pytest.raises(ValueError):
        cube = Cube(0,0,0,-1,1,1)
    with pytest.raises(ValueError):
        cube = Cube(0,0,0,1,-1,1)
    with pytest.raises(ValueError):
        cube = Cube(0,0,0,1,1,-1)
    with pytest.raises(TypeError):
        cube = Cube(0,0,0,'one',1,1)
    with pytest.raises(TypeError):
        cube = Cube(0,0,0,1,'one',1)
    with pytest.raises(TypeError):
        cube = Cube(0,0,0,1,1,'one')

def test_sphere_translation_with_invalid_coordinates():
    sphere = Sphere(0,0,0,1)
    with pytest.raises(TypeError):
        sphere.translation('one',1,1)
    with pytest.raises(TypeError):
        sphere.translation(1,'one',1)
    with pytest.raises(TypeError):
        sphere.translation(1,1,[1])

def test_cube_translation_with_invalid_coordinates():
    cube = Cube(0,0,0,1,1,1)
    with pytest.raises(TypeError):
        cube.translation('one',1,1)
    with pytest.raises(TypeError):
        cube.translation(1,'one',1)
    with pytest.raises(TypeError):
        cube.translation(1,1,'one')

def test_sphere_translation():
    sphere = Sphere(0,0,0,1)
    sphere.translation(-1,-1,-1)
    assert sphere.x == -1
    assert sphere.y == -1
    assert sphere.z == -1
    sphere.translation(5,5,5)
    assert sphere.x == 4
    assert sphere.y == 4
    assert sphere.z == 4
    
def test_cube_translation():
    cube = Cube(0,0,0,1,1,1)
    cube.translation(-1,-1,-1)
    assert cube.x == -1
    assert cube.y == -1
    assert cube.z == -1
    cube.translation(5,5,5)
    assert cube.x == 4
    assert cube.y == 4
    assert cube.z == 4

def test_sphere_equal():
    sphere1 = Sphere(0,0,0,1)
    sphere2 = Sphere(1,1,2,1)
    sphere3 = Sphere(2,2,2,2)
    assert sphere1 == sphere2
    assert sphere2 == sphere1
    assert not sphere1 == sphere3
    assert not sphere2 == sphere3

def test_cubes_equal(): #34
    cube1 = Cube(0,0,0,1,1,1)
    cube2 = Cube(1,1,1,1,1,1)
    cube3 = Cube(1,1,1,2,2,2)
    assert cube1 == cube2
    assert not cube1 == cube3
    assert not cube2 == cube3

def test_spheres_larger_than():
    sphere1 = Sphere(0,0,0,1)
    sphere2 = Sphere(1,1,2,1)
    sphere3 = Sphere(2,2,2,2)
    assert not sphere1 > sphere2
    assert not sphere1 > sphere3
    assert sphere3 > sphere1
    assert sphere3 > sphere2

def test_cubes_larger_than():
    cube1 = Cube(0,0,0,1,1,1)
    cube2 = Cube(1,1,1,1,1,1)
    cube3 = Cube(1,1,1,2,2,2)
    assert not cube1 > cube2
    assert not cube1 > cube3
    assert cube3 > cube1
    assert cube3 > cube2

def test_spheres_smaller_than(): #37
    sphere1 = Sphere(0,0,0,1)
    sphere2 = Sphere(1,1,2,1)
    sphere3 = Sphere(2,2,2,2)
    assert not sphere1 < sphere2
    assert sphere1 < sphere3
    assert sphere2 < sphere3
    assert not sphere3 < sphere1
    assert not sphere3 < sphere2

def test_cubes_smaller_than():
    cube1 = Cube(0,0,0,1,1,1)
    cube2 = Cube(1,1,1,1,1,1)
    cube3 = Cube(1,1,1,2,2,2)
    assert not cube1 < cube2
    assert cube1 < cube3
    assert cube2 < cube3
    assert not cube3 < cube1
    assert not cube3 < cube2
    assert cube2 < cube3

def test_spheres_smaller_than_or_equal():
    sphere1 = Sphere(0,0,0,1)
    sphere2 = Sphere(1,1,2,1)
    sphere3 = Sphere(2,2,2,2)
    assert sphere1 <= sphere2
    assert sphere1 <= sphere3
    assert sphere2 <= sphere3
    assert not sphere3 <= sphere1
    assert not sphere3 <= sphere2

def test_cubes_smaller_than_or_equal(): #40
    cube1 = Cube(0,0,0,1,1,1)
    cube2 = Cube(1,1,1,1,1,1)
    cube3 = Cube(1,1,1,2,2,2)
    assert cube1 <= cube2
    assert cube1 <= cube3
    assert cube2 <= cube3
    assert not cube3 <= cube1
    assert not cube3 <= cube2

def test_spheres_larger_than_or_equal():
    sphere1 = Sphere(0,0,0,1)
    sphere2 = Sphere(1,1,2,1)
    sphere3 = Sphere(2,2,2,2)
    assert sphere1 >= sphere2
    assert not sphere1 >= sphere3
    assert not sphere2 >= sphere3
    assert sphere3 >= sphere1
    assert sphere3 >= sphere2   

def test_cubes_larger_than_or_equal(): #42
    cube1 = Cube(0,0,0,1,1,1)
    cube2 = Cube(1,1,1,1,1,1)
    cube3 = Cube(1,1,1,2,2,2)
    assert cube1 >= cube2
    assert not cube1 >= cube3
    assert not cube2 >= cube3
    assert cube3 >= cube1
    assert cube3 >= cube2

def test_sphere_is_inside():
    sphere = Sphere(0,0,0,1)
    assert sphere.is_inside(0,0,0)
    assert not sphere.is_inside(-1,0,0)
    assert sphere.is_inside(-0.999,0,0)

def test_cube_is_inside():
    cube = Cube(0,0,0,1,1,1)
    assert cube.is_inside(0,0,0)
    assert cube.is_inside(-0.499,0,0)
    assert cube.is_inside(-0.499,-0.499,-0.499)
    assert cube.is_inside(-0.5,0,0)
    assert not cube.is_inside(-0.51,0,0)

def test_cube_is_cubic():
    cube1 = Cube(0,0,0,1,1,1)
    assert cube1.is_cubic() == True
    cube2 = Cube(0,0,0,1,1,2)
    assert not cube2.is_cubic() == True

def test_sphere_circumference():
    sphere = Sphere(0,0,0,1)
    assert sphere.circumference() == 2 * math.pi * sphere.radius
    assert not sphere.circumference() == 10

def test_sphere_surface_area():
    sphere = Sphere(0,0,0,1)
    assert sphere.surface_area == 4 * math.pi * sphere.radius**3

def test_cube_surface_area():
    cube = Cube(0,0,0,1,1,1)
    assert cube.surface_area == 6
    assert not cube.surface_area == 8

def test_cube_str():
    cube = Cube(1,1,1,1,1,1)
    assert str(cube) == 'x = 1, y = 1, z = 1, surface area = 6, volume = 1'

def test_sphere_str():
    sphere = Sphere(1,1,2,1)
    assert str(sphere) == 'x = 1, y = 1, z = 2, radius = 1, circumference = 6.283185307179586, surface area = 12.566370614359172'