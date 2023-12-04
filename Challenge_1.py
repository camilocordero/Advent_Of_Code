# Inicialización de variables
seguir = True  # Variable de control del bucle
datos = None  # Variable para almacenar los datos ingresados por el usuario
resultado = 0  # Variable para almacenar el resultado acumulado

# Bucle principal
while seguir:  # Mientras 'seguir' sea True
    def ajustar_lista():
        # Indica que se utilizarán las variables globales 'seguir' y 'resultado'
        global seguir
        global resultado

        # Captura de datos ingresados por el usuario
        datos = input("Input Data:")
        
        # Verificación de si se ingresa 'final' para detener el bucle
        if datos == "final":
            seguir = False
        else:
            # Procesamiento de los datos ingresados para obtener números
            caracteres = [caracter for caracter in datos if caracter.isdigit()]
            print(caracteres)
            
            # Obtención del primer número y último número de la lista 'caracteres'
            primer_numero = next((x for x in caracteres if x.isdigit()), None)
            caracteres_al_reves = list(reversed(caracteres))
            ultimo_numero = next((x for x in caracteres_al_reves if x.isdigit()), None)
            
            # Cálculo del resultado acumulado sumando los números obtenidos
            resultado = resultado + int(f"{primer_numero}{ultimo_numero}")
            print(resultado)
        
        return None

    # Llamada a la función 'ajustar_lista()' en cada iteración del bucle
    ajustar_lista()

print("Thanks for using :)")
