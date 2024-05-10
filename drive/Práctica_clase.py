# Genere en pantalla un saludo con su nombre. Utilice todos los recursos que dese.
print ("Hola, Jamil")
# Realice un ejemplo de: Suma, Resta, Multiplicación y División
x = 2
y = 4
print (x + y)
# Utilizando Variables y tipos de datos solicite datos al usuario: NOMBRE, EDAD, ALTURA, PESO
# luego imprima esos datos en pantalla
nombre = ("Jamil")
edad = ("18")
altura = ("1.70m")
peso = ("55kg")
print (nombre)
print (edad)
print (altura)
print (peso)
# Se tiene la siguente Lista: frutas = ["manzana", "plátano", "naranja"]
# Acceder a un elemento de la lista de posición [0])
# Agregar un elemento a la lista "pera" 
frutas = ["manzana", "plátano", "naranja"]
primer_fruta = frutas[0]
print("La primera fruta es:", primer_fruta)
frutas.append("pera")
print("Lista de frutas después de agregar 'pera':", frutas)
# Se plantea lo siguiente: (Condicionales) 
# pida un número entero
# imprima en pantalla si es positivo o negativo 
numero = int(input("Por favor, ingresa un número entero: "))
if numero > 0:
    print("El número ingresado es positivo.")
elif numero < 0:
    print("El número ingresado es negativo.")
elif numero == 0:
    print("El número ingresado es cero.")