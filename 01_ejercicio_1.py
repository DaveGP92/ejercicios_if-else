# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5 mil pesos y si es mayor de 18 años, 10 mil pesos.

edad = int(input("¿Qué edad tienes?: \n"))

if edad < 4:
    print(f"El cliente tiene {edad} años. Puede entrar gratis.")

elif edad >= 4 and edad <=18:
    print(f"El cliente tiene {edad} años, debe pagar 5 mil pesos.")

else:
    print(f"El cliente tiene {edad}, debe pagar 10 mil pesos.")