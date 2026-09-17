import itertools

def generar_tabla_verdad():
    print("--- Tabla de Verdad ---")
    try:
        
        num_prop = int(input("¿Cuántas proposiciones quieres?: "))
        

        #Nombre varianbles
        variables = [chr(112 + i) for i in range(num_prop)]
        
        
        encabezado = " | ".join(variables)
        print("\n" + encabezado)
        print("-" * len(encabezado))

        #Combinaciones pocibles
        combinaciones = list(itertools.product(['V', 'F'], repeat=num_prop))

        for fila in combinaciones:
            print(" | ".join(fila))
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")

if __name__ == "__main__":
    generar_tabla_verdad()