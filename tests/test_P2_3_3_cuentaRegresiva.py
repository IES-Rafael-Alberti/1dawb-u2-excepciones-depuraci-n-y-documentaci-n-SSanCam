import pytest 
from src.P2_3_3_cuentaRegresiva import cuenta_atras

@pytest.mark.parametrize(
    "numero, expected",
    [
        (5, [5, 4, 3, 2, 1, 0])
    ]
)

def P2_3_1_anios_cumplidos(numero, expected):
    assert cuenta_atras(numero) == expected
    
def comprobar_excepciones():
    with pytest.raises(TypeError):
        cuenta_atras("cuentaAtras")
    
    with pytest.raises(Exception):
        cuenta_atras