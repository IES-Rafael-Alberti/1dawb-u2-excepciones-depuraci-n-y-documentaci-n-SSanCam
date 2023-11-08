"""Escribir que solicite una contraseña, y si no coincide con la que se tiene, 
lance la excepción NameError con el mensaje, "Incorrect Password!!" """
def solicitarContrasenia(contrasenia: str) -> str:

    password = "pestillo1234"
        
    if (contrasenia == password):
        return "Contraseña correcta!"
        
    else: 
        raise NameError("Incorrect Password!!")


        
def main():
    
    try:    
        
        contrasenia = str(input("Introduce la contraseña: "))
        resultado = solicitarContrasenia(contrasenia)
        print(resultado)
        
    except NameError as e:
        print(e)
        
if __name__=="__main__":
    main()