import Lab3_functions as fkn
import math
import pytest

def test_circle_with_invalid_radius_input():
    with pytest.raises(TypeError):
        circle = fkn.Circle(1,1,'one')
    with pytest.raises(ValueError):
        circle = fkn.Circle(1,1,-1)

def test_circle_with_invalid_coordinate_input():
    with pytest.raises(TypeError):
        circle = fkn.Circle('one',1,1)
    with pytest.raises(TypeError):
        circle = fkn.Circle(1,'one',1)

def test_rectangle_with_invalid_side_input():
    with pytest.raises(ValueError):
        rectangle = fkn.Rectangle(1,1,-1,1)
    with pytest.raises(ValueError):
        rectangle = fkn.Rectangle(1,1,1,-1)
    with pytest.raises(TypeError):
        rectangle = fkn.Rectangle(1,1,'one',1)
    with pytest.raises(TypeError):
        rectangle = fkn.Rectangle(1,1,1,'one')

def test_translation_with_invalid_coordinates():
    circle = fkn.Circle(0,0,1)
    with pytest.raises(TypeError):
        circle.translation(-1,'one')
    with pytest.raises(TypeError):
        circle.translation('one',-1)

def test_translation():
    circle = fkn.Circle(0,0,1)
    circle.translation(-1,-1)
    assert circle.x == -1
    assert circle.y == -1
    circle.translation(5,5)
    assert circle.x == 4
    assert circle.y == 4

def test_circles_equal():
    circle1 = fkn.Circle(0,0,2)
    circle2 = fkn.Circle(1,1,2)
    circle3 = fkn.Circle(0,0,2)
    circle4 = fkn.Circle(1,1,3)
    assert circle1 == circle2
    assert circle2 == circle3
    assert circle1 == circle3
    assert circle1 != circle4
    assert circle2 != circle4
    assert circle3 != circle4

def test_rectangles_equal():
    rectangle1 = fkn.Rectangle(0,0,1,1)
    rectangle2 = fkn.Rectangle(1,1,1,1)
    rectangle3 = fkn.Rectangle(0,0,2,3)
    assert rectangle1 == rectangle2
    assert rectangle1 != rectangle3
    assert rectangle2 != rectangle3

def test_circles_rectangles_equal():
    circle = fkn.Circle(0,0,1)
    rectangle = fkn.Rectangle(0,0,2,3)
    assert circle != rectangle

def test_circles_larger_than():
    circle1 = fkn.Circle(0,0,2)
    circle2 = fkn.Circle(1,1,2)
    circle3 = fkn.Circle(0,0,2)
    circle4 = fkn.Circle(1,1,3)
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
    rectangle1 = fkn.Rectangle(0,0,1,1)
    rectangle2 = fkn.Rectangle(1,1,1,1)
    rectangle3 = fkn.Rectangle(0,0,2,3)
    assert not rectangle1 > rectangle2
    assert not rectangle1 > rectangle3
    assert not rectangle2 > rectangle1
    assert not rectangle2 > rectangle3
    assert rectangle3 > rectangle2
    assert rectangle3 > rectangle1

def test_circles_rectangles_larger_than():
    circle = fkn.Circle(0,0,1)
    rectangle = fkn.Rectangle(0,0,2,3)
    assert not circle > rectangle
    assert rectangle > circle

def test_circles_equal_or_smaller_than():
    circle1 = fkn.Circle(0,0,2)
    circle2 = fkn.Circle(1,1,2)
    circle3 = fkn.Circle(0,0,2)
    circle4 = fkn.Circle(1,1,3)
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
    rectangle1 = fkn.Rectangle(0,0,1,1)
    rectangle2 = fkn.Rectangle(1,1,1,1)
    rectangle3 = fkn.Rectangle(0,0,2,3)
    assert rectangle1 <= rectangle2
    assert rectangle1 <= rectangle3
    assert rectangle2 <= rectangle1
    assert rectangle2 <= rectangle3
    assert not rectangle3 <= rectangle2
    assert not rectangle3 <= rectangle1

def test_circles_rectangles_equal_or_smaller_than():
    circle = fkn.Circle(0,0,1)
    rectangle = fkn.Rectangle(0,0,2,3)
    assert circle <= rectangle
    assert not rectangle <= circle

def test_circles_equal_or_larger_than():
    circle1 = fkn.Circle(0,0,2)
    circle2 = fkn.Circle(1,1,2)
    circle3 = fkn.Circle(0,0,2)
    circle4 = fkn.Circle(1,1,3)
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
    rectangle1 = fkn.Rectangle(0,0,1,1)
    rectangle2 = fkn.Rectangle(1,1,1,1)
    rectangle3 = fkn.Rectangle(0,0,2,3)
    assert rectangle1 >= rectangle2
    assert not rectangle1 >= rectangle3
    assert rectangle2 >= rectangle1
    assert not rectangle2 >= rectangle3
    assert rectangle3 >= rectangle2
    assert rectangle3 >= rectangle1

def test_circles_rectangles_equal_or_larger_than():
    circle = fkn.Circle(0,0,1)
    rectangle = fkn.Rectangle(0,0,2,3)
    assert not circle >= rectangle
    assert rectangle >= circle

def test_circle_unitcircle():
    circle = fkn.Circle(0,0,1)
    assert circle.is_unitcircle() == True
    circle = fkn.Circle(1,1,1)
    assert circle.is_unitcircle() == False

def test_circle_area():
    circle = fkn.Circle(0,0,1)
    assert circle.area == 1**2 * math.pi

def test_circle_circumference():
    circle = fkn.Circle(0,0,1)
    assert circle.circumference == 2 * 1 * math.pi

def test_circle_is_inside():
    circle = fkn.Circle(0,0,1)
    assert circle.is_inside(0,0) == True
    assert circle.is_inside(1,1) == False
    assert circle.is_inside(1,0) == False
    assert circle.is_inside(0.5,0.5) == True
    assert circle.is_inside(0.9999,0) == True
    
def test_rectangle_is_quadratic():
    rectangle = fkn.Rectangle(1,1,1,1)
    assert rectangle.is_quadratic() == True

def test_rectangle_area():
    rectangle = fkn.Rectangle(1,1,1,1)
    assert rectangle.area == 1

def test_rectangle_circumference():
    rectangle = fkn.Rectangle(1,1,1,1)
    assert rectangle.circumference == 4

def test_rectangele_is_inside():
    rectangle = fkn.Rectangle(0,0,1,1)
    assert rectangle.is_inside(0,0) == True
    assert rectangle.is_inside(0.4999,0.4999) == True
    assert rectangle.is_inside(0.5,0.5) == False