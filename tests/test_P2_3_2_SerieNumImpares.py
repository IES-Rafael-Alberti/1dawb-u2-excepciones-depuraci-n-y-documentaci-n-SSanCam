import pytest 
from src.P2_3_2_SerieNumImpares import serie_impares
from src.P2_3_1_anios_cumplidos import anios_cumplido

@pytest.mark.parametrize(
    "numero, expected",
    [
        (11, [1, 3, 5, 7, 9, 11])
    ]
)
def test_P2_3_2_SerieNumImpares(numero, expected):
    assert serie_impares(numero) == expected
 
def comprobar_positivo():
    with pytest.raises(Exception):
        serie_impares(0)
        
def comprobar_tipo_dato():
    with pytest.raises(TypeError):
        serie_impares("asd")
        
def comprobar_entero():
    with pytest.raises(ValueError):
        serie_impares(3.0)