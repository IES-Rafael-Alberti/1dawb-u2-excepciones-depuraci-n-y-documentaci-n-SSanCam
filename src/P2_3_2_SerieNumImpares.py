"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""

def serie_impares(numero: int):
    
    serie = []
    
    if(numero <= 0):
        raise Exception
    
    else:
        for num in range(1,numero+1,2):
            
            serie.append(num)
            
    print("Todos los numeros impares desde el 1 tu numero elegido son:\n")
    
    return print(serie) 
   
    
    
    
def main():
    
    try: 
        
        print("Ingresa un número: ")
        numero = int(input())
        
        if (numero <= 0):
            raise Exception
        else:
            serie_impares(numero)
           
        
    except TypeError:
        print("ERROR\nDebes ingresar numeros enteros positivos.")
    
    except ValueError:
        print("Debes ngresar valores numericos.") 

    except Exception:
        print("ERROR.\n Introduce valores superiores a 0.")
        
if __name__=="__main__":
    main()