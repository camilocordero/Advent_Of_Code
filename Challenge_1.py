seguir = True
datos = None
resultado = 0
while (seguir == True):
        def ajustar_lista ():
            global seguir
            global resultado
            datos = input("Input Data:")
            if datos == "final":
                seguir = False
            else:
                caracteres = [caracter for caracter in datos if caracter.isdigit()]
                print(caracteres)
                primer_numero = next((x for x in caracteres if x.isdigit()), None)
                caracteres_al_reves = list(reversed(caracteres))
                ultimo_numero = next((x for x in caracteres_al_reves if x.isdigit()), None)
                resultado = resultado + int(f"{primer_numero}{ultimo_numero}")
                print (resultado)
            return None
        ajustar_lista()
    


print ("Thanks for using :)")



# Crear una lista con caracteres individuales del string
