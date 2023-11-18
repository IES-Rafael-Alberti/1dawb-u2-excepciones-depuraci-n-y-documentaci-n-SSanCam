"""Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada."""
def tipo_entrada(numero: int) -> str:

        if (type(numero) != int):
            raise ValueError("La entrada no es correcta.")
        
        else: 
            msj = ("Entrada correcta.")
    
        return msj
    
    

def main():
    
    try : 
         
        numero = int(input("Introduce un numero: "))
        resultado = tipo_entrada(numero)
        
        return print(resultado)
        
    except ValueError as e:
        print(e)
    
if __name__=="__main__":
    main()