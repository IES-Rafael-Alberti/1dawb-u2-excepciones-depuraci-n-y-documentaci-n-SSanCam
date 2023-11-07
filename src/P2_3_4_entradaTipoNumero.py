"""Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada."""
def tipo_entrada(numero: int) -> str:

        if (type(numero) != int):
            raise ValueError
        
        else: 
            msj = ("Entrada correcta.")
    
        return msj
    
    

def main():
    
    try :  
        numero = int(input("Introduce un numero: "))
        resultado = tipo_entrada(numero)
        
        return print(resultado)
        
    except ValueError:
        print("La entrada no es correcta.")
    
if __name__=="__main__":
    main()