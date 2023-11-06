"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

def anios_cumplido(edad: int) -> str:
        
    cumplido = []
    if (edad <= 0):
        raise Exception
                
    for anio in range(1,edad+1):
        cumplido.append(anio)
    
    return cumplido
    
    #else: si no captura ninguna excepcion, ejecuta el else
        #serie = obtenerSerie(edad)
    
    #finally: es algo que se ejecurata siempre
  

########################


def main():

    try:
        
        print("¿Qué edad tienes?: ")
        edad = int(input())
        
        if (edad <= 0): 
            raise Exception
        
        if (edad > 0):
            print("Desde que naciste, has cumplido estos años: ")
            print(anios_cumplido(edad))
            
    except TypeError: #va a ejecutar el error que he elevadoa antes en if edad < 0
        print ("**ERROR**\nDebes introducir números enteros positivos.")
        
    except Exception:
        print("ERROR\nDebes introducir valores numéricos enteros positivos.")  
      
        
if __name__=="__main__":
    main()