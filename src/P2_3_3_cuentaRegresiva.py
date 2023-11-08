"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. 
Deberá solicitar el número hasta introducir uno correcto."""
def cuenta_atras(numero: int) -> list:
    from P2_3_1_anios_cumplidos import cada_anio
    
    serie = cada_anio(numero)
    
    serie = list(range(numero, -1, -1))
    return serie



def main():
    
    try: 
        
        print("Introduce un numero entero positivo: ")
        numero = int(input())
        
        while (numero <= 0):
            numero = int(input("ERROR\nDebes introducir un numero entero positivo: "))
        
        print("Cuenta atras: ")
        return print(cuenta_atras(numero))
    
    except TypeError:
        print("Error. Debes introducir un numero entero positivo.")
        
    except Exception:
        print("404 Error indeterminado.")
    
    
    
if __name__=="__main__":
    main()