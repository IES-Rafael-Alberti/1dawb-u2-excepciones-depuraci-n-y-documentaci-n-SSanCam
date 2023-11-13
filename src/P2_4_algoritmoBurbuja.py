def ordenacionAlgoritmoBurbuja(listaNumeros: list) -> list:
    
    cont = len(listaNumeros)
    
    #Con la primera iteracion recorreremos todos los numeros de la cadena 
    for i in range(cont + 1):
        #En la segunda iteracion, comparamos el numero donde nos encontremos con el siguiente a la derecha.
        for j in range(0, cont - i - 1):
            if listaNumeros[j] > listaNumeros[j + 1]:
            #Segun la condicion dada, si se cumple, se intercambian la posicion de los numeros que estamos comparando 
                j_temporal = listaNumeros[j]
                j1_temporal = listaNumeros[j + 1]
                
                listaNumeros[j] = j1_temporal
                listaNumeros[j + 1] = j_temporal

    return listaNumeros
    
    
#####################################################################
def main():
    
    try:
        lista_numeros = []
        print("Ingresa todos los numeros enteros positivos que quieres incluir en la lista.\nIngresa 0 para finalizar:  ")
        indice = 1
        numero = int(input(f"{indice}.- "))
        while (numero > 0):
            indice += 1
            numero = int(input(f"{indice}.- "))
            if (numero == 0):    
                resultado = print(ordenacionAlgoritmoBurbuja(lista_numeros))
                return (resultado)
            lista_numeros.append(numero)
            
    except Exception:
        return "ERROR - 404"
    
    
if __name__=="__main__":
    main()