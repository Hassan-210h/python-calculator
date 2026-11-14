import math

from main import add, subtract, multiply, divide, power, modulo, square_root


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(2.5, 2.5) == 5.0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
    # القسمة على صفر يجب أن ترجع رسالة خطأ
    assert divide(10, 0) == "خطأ: لا يمكن القسمة على صفر!"


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(9, 0.5) == 3.0


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(10, 0) == "خطأ: لا يمكن القسمة على صفر!"


def test_square_root():
    assert square_root(9) == 3.0
    assert math.isclose(square_root(2), math.sqrt(2))
    # الجذر لعدد سالب يجب أن يرجع رسالة خطأ
    assert square_root(-1) == "خطأ: لا يمكن أخذ الجذر التربيعي لعدد سالب!"
