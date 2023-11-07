import pytest 
from src.P2_3_4_entradaTipoNumero import tipo_entrada

@pytest.mark.parametrize(
    "numero, expected",
    [
        (5, "Entrada correcta."),
    ]
)

def test_P2_3_4_entradaTipoNumero(numero, expected):
    assert tipo_entrada(numero) == expected
    
    
def test_tipo_dato():
      
    with pytest.raises(ValueError):
        tipo_entrada("asd")
        
    """with pytest.raises(TypeError):
        tipo_entrada(4.4)"""