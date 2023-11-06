import pytest 
from src.P2_3_1_anios_cumplidos import anios_cumplido

"""
@pytest.mark.parametrize(
    "edad, expected",
    [ 
        (5, [1, 2, 3, 4, 5])
    ]
)
"""
def test_P2_3_1_anios_cumplidos (edad, expected):
    assert anios_cumplido(edad) == expected 
    

def test_comprobar_numero():
    with pytest.raises(TypeError):
        anios_cumplido("edad")
        
    with pytest.raises(Exception):
        anios_cumplido(-5)