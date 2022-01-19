from src.main.tests.functions import dividir
from src.main.tests.functions import convertir_mayusculas
from src.main.tests.functions import longitud_palabra
from src.main.tests.functions import minimo_numero
from src.main.tests.functions import suma_numeros
from src.main.tests.functions import convertir_decimal
from src.main.tests.functions import saludo
from src.main.tests.functions import potencia_numero
from src.main.tests.functions import convertir_hexadecimal
from src.main.tests.functions import lista


def test_dividir():
    assert(9/3) == 3


def test_convertir_mayusculas():
    assert('foo'.upper(), 'FOO')


def test_longitud_palabra():
    assert len('hola') == 4


def test_minimo_numero():
    assert min(2, 4, 1) == 1


def test_suma_numeros():
    assert sum([2, 4, 5, 10]) == 21


def test_convertir_decimal():
    assert float(2) == 2.00


def test_saludo():
    assert("Hola Olalla") == "Hola Olalla"


def test_potencia_numero():
    assert pow(2, 4) == 16


def test_convertir_hexadecimal():
    assert hex(10) == "0xa"


def test_lista():
    assert(1, 3, 5, 7) == (1, 3, 5, 7)
