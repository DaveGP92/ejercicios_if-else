# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

#Pedimos al cliente que elija el tipo de pizza
eleccion_pizza = input("¿Qué tipo de pizza desea ordenar?\n¿vegetariana o no vegetariana?\nEscriba le letra 'v' para elegir pizza vegetariana o 'nv' para una pizza no vegetariana\n").lower()

#Pedimos al cliente que elija el ingrediente añadido
if eleccion_pizza == 'v':
    eleccion_ingrediente = input(("Elije si quieres la hamburguesa con pimiento (p) o tofu (t)\n")).lower()
    
    #Si elige "p" se agrega pimiento
    if eleccion_ingrediente == "p":
        p = "pimiento"
        print(f"Elegiste una pizza vegetariana con {p}")
        print(f"Tu hamburguesa contiene los siguientes elementos: Mozarella, tomate y el ingrediente añadido: {p}")
        
    #Si elige "t" se agrega tofu
    elif eleccion_ingrediente == "t":
        t = "tofu"
        print(f"Elegiste una pizza vegetariana con {t}")
        print(f"Tu hamburguesa contiene los siguientes elementos: Mozarella, tomate y el ingrediente añadido: {t}")
    
    #Si elige una opción diferente, se termina el programa
    else:
        print("Entrada no válida")

elif eleccion_pizza == 'nv':
    eleccion_ingrediente = input(("Elije si quieres la hamburguesa con peperoni (pe), jamón (j) o salmón (s)\n")).lower()
    
    if eleccion_ingrediente == "pe":
        pe = "peperoni"
        print(f"Elegiste una pizza No vegetariana con {pe} como ingrediente agregado.")
        print(f"Tu hamburguesa contiene los siguientes elementos: Mozarella, tomate y el ingrediente añadido: {pe}")
    
    elif eleccion_ingrediente == "j":
        j = "jamón"
        print(f"Elegiste una pizza No vegetariana con {j} como ingrediente agregado.")
        print(f"Tu hamburguesa contiene los siguientes elementos: Mozarella, tomate y el ingrediente añadido: {j}")
    
    elif eleccion_ingrediente == "s":
        s = "salmón"
        print(f"Elegiste una pizza No vegetariana con {s} como ingrediente agregado.")
        print(f"Tu hamburguesa contiene los siguientes elementos: Mozarella, tomate y el ingrediente añadido: {s}")
    
    else:
        print("Entrada no válida")

else:
    print("Opción no válida.")



