from Classes.Ciclista import Ciclista

# OBJETO
ciclista = Ciclista()

# Lista
ciclistas = []
tiempos = []

opcion = 1

# Utilizo el SETTER
# ciclista.nombre = ''
# ciclista.edad = 0
# ciclista.pais = ''
# ciclista.equipo = ''
# ciclista.tiempo = 0

# Acceder al atributo
# ciclistas.append(print('Digite el nombre: ') + input(ciclista.nombre))
# ciclistas.append(print('Digite la edad: ') + input(ciclista.edad))
# ciclistas.append(print('Digite el pais: ') + input(ciclista.pais))
# ciclistas.append(print('Digite el equipo: ') + input(ciclista.equipo))
# ciclistas.append(print('Digite el tiempo: ') + input(ciclista.tiempo))


# print(ciclistas)



# MENU
# print('MENÚ DEL PROGRAMA')
# print('1. Agregar ciclista')
# print('2. Mostrar ciclistas')
# print('3. Mostrar ciclista con mejor tiempo')
# print('4. Salir')

# while (opcion != 4):
#     opcion = int(input('Digita una opción: '))
#     if(opcion == 1):
#         agregar = {}
#         ## Llenando el diccionario
#         agregar[ciclista.nombre] = input('Nombre: ')
#         agregar[ciclista.edad] = int(input('Edad: '))
#         agregar[ciclista.pais] = input('Pais: ')
#         agregar[ciclista.equipo] = input('Equipo: ')
#         agregar[ciclista.tiempo] = int(input('Tiempo: '))
        
#         # Llenando la lista
#         ciclistas.append(agregar)

#     elif(opcion == 2):
#         print(ciclistas)

    
#     elif(opcion == 4):
#         print('Saliendo del programa...')
#     else:
#         print('Digita una opción valida')

# else:
#     print('---------------------------------')
#     print('Saliste del programa.')

# MENU
print('MENÚ DEL PROGRAMA')
print('1. Agregar ciclista')
print('2. Mostrar ciclistas')
print('3. Mostrar ciclista con mejor tiempo')
print('4. Salir')

while (opcion != 4):
    opcion = int(input('Digita una opción: '))
    if(opcion == 1):

        ciclista.nombre = ''
        ciclista.edad = 0
        ciclista.pais = ''
        ciclista.equipo = ''
        ciclista.tiempo = 0
        
        ciclistas.append({"nombre":ciclista.nombre,"edad":ciclista.edad,"pais":ciclista.pais,"equipo":ciclista.equipo,"tiempo":ciclista.tiempo})
        tiempos.append(ciclista.tiempo)
        # Llenando la lista
        

    elif(opcion == 2):
        print(ciclistas)

    elif(opcion == 3):
        mejorTiempo = min(tiempos)
        print('El ciclista con mejor tiempo fue:')
        print(next(x for x in ciclistas if x['tiempo'] == mejorTiempo))
        

    elif(opcion == 4):
        print('Saliendo del programa...')
    else:
        print('Digita una opción valida')

else:
    print('---------------------------------')
    print('Saliste del programa.')