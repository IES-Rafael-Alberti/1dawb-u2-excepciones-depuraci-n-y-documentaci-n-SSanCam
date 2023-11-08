import pytest 
from src.P2_3_1_anios_cumplidos import cada_anio


@pytest.mark.parametrize(
    "edad, expected",
    [ 
        (5,[1, 2, 3, 4, 5])
    ]
)

def test_P2_3_1_anios_cumplidos (edad, expected):
    assert cada_anio(edad) == expected 
    

def test_comprobar_numero():
    with pytest.raises(TypeError):
        cada_anio("edad")
        
    with pytest.raises(Exception) as e:
        cada_anio(-5)
        assert str(e.value) == "ERROR\nDebes introducir valores numéricos enteros positivos."