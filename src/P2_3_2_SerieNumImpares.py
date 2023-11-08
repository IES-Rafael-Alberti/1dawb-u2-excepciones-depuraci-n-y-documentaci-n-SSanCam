"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""

def serie_impares(numero: int) -> list:
    from src.P2_3_1_anios_cumplidos import cada_anio
    
    serie = cada_anio(numero)

    serieNumImpares = (serie[::2])
    
    return serieNumImpares
 

def main():
    try: 
        
        print("Ingresa un número: ")
        numero = int(input())
        
        if (numero <= 0):
            raise Exception
        
        else:
            resultado = (serie_impares(numero))
            print("La serie de numeros impares desde 1 hasta tu numero es:")
            print(resultado)

        
    except TypeError:
        print("ERROR\nDebes ingresar numeros enteros positivos.")
    
    except ValueError:
        print("Debes ngresar valores numericos.") 

    except Exception:
        print("ERROR.\n Introduce valores superiores a 0.")
        
if __name__=="__main__":
    main()