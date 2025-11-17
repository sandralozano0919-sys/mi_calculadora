import calculator

def test_suma():
    assert calculator.sumar(2, 3) == 5

def test_resta():
    assert calculator.restar(5, 2) == 3

def test_multiplicacion():
    assert calculator.multiplicar(3, 4) == 12

def test_division():
    assert calculator.dividir(10, 2) == 5

def test_division_por_cero():
    try:
        calculator.dividir(5, 0)
        assert False  # Si llega aquí, hay error
    except ZeroDivisionError:
        assert True
