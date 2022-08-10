#Banner F1

print(" _______                             __         ____   ")
print("|    ___|.-----.----.--------.--.--.|  |.---.-.|_   |  ")
print("|    ___||  _  |   _|        |  |  ||  ||  _  | _|  |_ ")
print("|___|    |_____|__| |__|__|__|_____||__||___._||______|\n")

nombre = input("¿Cual es tu nombre?")
print("\n")
print(nombre + " bienvenido, aquí sabremos cuanto te gusta la F1")
print("Es un test de 3 simples preguntas :)\n")
a = ("Es un test de 3 simples preguntas :")
print("-"*len(a))
print("\n")

#Primera pregunta

print("¿Quíen fué campeon del mundo en el 2021?\n")
print("1 -> Max Verstappen")
print("2 -> Lewis Hamilton")
print("3 -> Lando Norris\n")

r1 = int(input("Inserta la respuesta correcta: "))
print("\n")

if ( 1 < r1 > 3):
    print("Esa respuesta no existe.")

if r1 == 1:
    print("Tu respuesta es correcta.\n")
    b = ("Tu respuesta es correcta.") 
    print("-"*len(b),"\n")
    
    #Segunda pregunta

    print("¿Qué equipo tiene la parada más rapida de pits?\n")
    print("1 -> Mercedes")
    print("2 -> Red Bull")
    print("3 -> Willams\n")
    r2 = int(input("Inserta la respuesta correcta: "))
    print("\n")
    
    if ( 1 < r2 > 3):
        print("Esa respuesta no existe.")

    if r2 == 2:
        print("Tu respuesta es correcta.\n")
        print("-"*len(b),"\n")

        #Tercera pregunta

        print("¿Qué piloto F1 tiene 7 campeonatos mundiales?\n") 
        print("1 -> Daniel Ricciardo")
        print("2 -> Nicholas Latifi")
        print("3 -> Lewis Hamilton\n") 
        r3 =int(input("Inserta la respuesta correcta: "))
        print("\n")
       
        if ( 1 < r3 > 3):
            print("Esa respuesta no existe.")

        if r3 == 3:
            print("Tu respuesta es correcta.\n")
            print("-"*len(b),"\n")

            #Puntuacion

            print("Tienes un 10!")

            #Agradecimientos

            print("Eres un verdadero fan de Formula 1 :)\n")
            c =("Eres un verdadero fan de Formula 1 :)") 
            print("-"*len(c),"\n")
            print("*****Creado por Luis Eduardo*****")
            print("\n")

            #Mensaje de error
            #Respuestas incorrectas
            
        else:
            print("Tu respuetsa es incorrecta :(")
            print("Tines 66 de puntuación")

    else:
        print("Tu respuetsa es incorrecta :(")
        print("Tines 33 de puntuación")
else:
    print("Tu respuetsa es incorrecta :(")
    print("Tines 0 de puntuación")

#Creado por luis Eduardo Ocegueda Cortés
#Cuestionario basico de formula 1       
