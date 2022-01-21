print(      "Calculadora"     )
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicación")
print("4.- División")
print("5.- Potencial")
print("6.- Raíz Cuadrada")
print("7.- Porcentaje")

menu = int(input("¿Qué operación deseas relizar: "))

if menu == 1:
    n1 = int(input("Inserta el primer número: "))
    n2 = int(input("Inserta el segundo número: "))
    suma = n1 + n2
    print(f"El resultado de la suma es: {suma}")

elif menu == 2:
    n1 = int(input("Inserta el primer número: "))
    n2 = int(input("Inserta el segundo número: "))
    resta = n1 - n2
    print(f"El resultado de la resta es: {resta}")

elif menu == 3:
    n1 = int(input("Inserta el primer número: "))
    n2 = int(input("Inserta el segundo número: "))
    multiplicacion = n1 * n2
    print(f"El resultado de la multiplicación es: {multiplicacion}")

elif menu == 4:
    n1 = int(input("Inserta el primer número: "))
    n2 = int(input("Inserta el segundo número: "))
    division = n1 / n2
    print(f"El resultado de la División es: {division}")
elif menu == 5:
    n1 = int(input("Inserta la base: "))
    n2 = int(input("Inserta el exponnte: "))
    potencia = n1 ** n2
    print(f"El resultado de la Potencia es: {potencia}")

elif menu == 6:
    n1 = int(input("Inserta a que número quiere sacar la raíz: "))
    raiz = n1 ** 0.5
    print(f"El resultado de la Raíz Cuadrada: {raiz}")

elif menu == 7:
    n1 = int(input("Inserta el número: "))
    n2 = int(input("Inserta el porcentaje: "))
    porcentaje_1 = n2 / 100
    porcentaje_2 = 1 - porcentaje_1
    porcentaje_4 = n1 * porcentaje_2
    print(f"El resultado del con el porcentaje aplicado: {porcentaje_4}")
