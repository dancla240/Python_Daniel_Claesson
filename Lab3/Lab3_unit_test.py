import Lab3_functions as fkn
import math

def test_circle():
    circle1 = fkn.Circle(0,0,1)
    assert circle1.area == 1*1*math.pi
    assert circle1.is_inside(0,0) == True
    assert circle1.is_inside(1,1) == False
    assert circle1.is_inside(1,0) == False
    assert circle1.is_inside(0.5,0.5) == True
    assert circle1.is_inside(0.9999,0) == True

def test_rectangle():
    rectangle1 = fkn.Rectangle(1,1,1,1)
    assert rectangle1.area == 1
    assert rectangle1.x == 1
    assert rectangle1.y == 1
    assert rectangle1.circumference == 4
    assert rectangle1.is_quadratic == True