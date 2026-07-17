#Días de la Semana: Crea un script que reciba un número del 1 al 7 en una variable.
#Utiliza match case para asignar e imprimir el día de la semana correspondiente (1
#para Lunes, 7 para Domingo). Incluye un caso por defecto (case _) para números
#fuera de rango.

numero= int(input('ingrese un numero del 1 al 7'))

match numero:
    case 1:
        print('lunes')
    case 2:
        print('martes')
    case 3:
        print('miercoles')
    case 4:
        print('jueves')
    case 5:
        print('viernes')
    case 6:
        print('sabado')
    case 7:
        print('domingo')
    case _:
        print('numero fuera de rango')


