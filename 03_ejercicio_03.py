# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("¿Cuál es tu nombre?\n").lower()
sexo = input("¿Cuál es tu sexo? (m) Masculino o (f) femenino\n").lower()
        
if sexo == "f" and nombre < "m" or sexo == "m" and nombre >= "n":
    
    print(f"Te llamas {nombre.capitalize()} y perteneces al grupo A.")

elif sexo == "f" and nombre >= "m" or sexo == "m" and nombre < "n":
    print(f"Te llamas {nombre.capitalize()} y perteneces al grupo B.")

else:
    print("Sexo no válido")