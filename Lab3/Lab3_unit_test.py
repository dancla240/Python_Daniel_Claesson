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
    


# def test_rectangle():
#     rectangle1 = fkn.Rectangle(1,1,1,1)
#     assert rectangle1.area == 1
#     assert rectangle1.circumference == 4
#     assert rectangle1.x == 1
#     assert rectangle1.y == 1
#     assert rectangle1.is_quadratic() == True
#     rectangle2 = fkn.Rectangle(1,1,1,1)
#     assert rectangle2 == rectangle1
#     assert rectangle2 >= rectangle1
#     rectangle3 = fkn.Rectangle(2,2,1,2)
#     assert rectangle3 != rectangle1
#     assert rectangle3.is_quadratic() == False
#     rectangle3.translation(1,1)
#     assert rectangle3.x == 3
#     assert rectangle3.y == 3
#     assert rectangle3 > rectangle1
#     assert rectangle1 < rectangle3


# def test_circle():
#     circle1 = fkn.Circle(0,0,1)
#     assert circle1.area == 1*1*math.pi
#     assert circle1.is_inside(0,0) == True
#     assert circle1.is_inside(1,1) == False
#     assert circle1.is_inside(1,0) == False
#     assert circle1.is_inside(0.5,0.5) == True
#     assert circle1.is_inside(0.9999,0) == True
#     assert circle1.is_unitcircle() == True
#     circle2 = fkn.Circle(0,0,1)
#     assert circle1 == circle2
#     circle1.translation(2,2)
#     assert circle1.is_inside(0,0) == False
#     assert circle1.is_inside(2,2) == True
#     assert circle1.is_unitcircle() == False
#     assert circle1 == circle2
#     assert circle1 >= circle2

# def test_circle_rectangle():
#     circle1 = fkn.Circle(0,0,1)
#     rectangle1 = fkn.Rectangle(1,1,1,1)
#     assert circle1.area > rectangle1.area

