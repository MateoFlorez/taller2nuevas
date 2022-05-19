from Classes.Ciclista import Ciclista

# OBJETO
ciclista = Ciclista()

# Lista
ciclistas = []
tiempos = []

opcion = 1

# MENU
print('MENÚ DEL PROGRAMA')
print('1. Agregar ciclista')
print('2. Mostrar ciclistas')
print('3. Mostrar ciclista con mejor tiempo')
print('4. Salir')

while (opcion != 4):
    opcion = int(input('Digita una opción: '))
    if(opcion == 1):

        ciclista.nombre = input('Digita el nombre: ')
        ciclista.edad = int(input(f'Digita la edad: '))
        ciclista.pais = input('Digita el pais: ')
        ciclista.equipo = input('Digita el equipo: ')
        ciclista.tiempo = int(input('Digita el tiempo: '))
        
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