import pytest 
from src.P2_3_5_ingresarContrasenia import solicitarContrasenia

@pytest.mark.parametrize(
    "contrasenia, expected",
    [
        ("pestillo1234", "Contraseña correcta!"),
        ("nolarecuerdo", "Incorrect Password!!")
    ]
)

def test_P2_3_5_ingresarContrasenia(contrasenia, expected):
    try:
        
        assert solicitarContrasenia(contrasenia) == expected 
    except NameError as e:
        assert str(e) == "Incorrect Password!!"
        
def comprobar_contrasenia():
    
    with pytest.raises(NameError) as e:
        solicitarContrasenia("semarvidao")
        assert str(e.value) == "Incorrect Password!!"
