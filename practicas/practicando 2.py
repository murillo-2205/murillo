#Control de Acceso por Edad: Escribe un programa que reciba la edad de un
#usuario. Si la edad es menor de 18, debe imprimir "Acceso denegado". Si está entre
#18 y 65 años, debe imprimir "Acceso permitido". Si es mayor de 65, debe imprimir
#"Acceso preferencial para adultos mayores".

edad= int(input('ingrese su edad'))
if edad <18:
    print('es menor de edad')
elif edad <=65:
    print('acceso permitido')
else:
    print('acceso para mayores')


