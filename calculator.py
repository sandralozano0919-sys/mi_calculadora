def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def main():
    print("=== Calculadora Básica ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    while True:
        opcion = input("Elija una opción: ")

        if opcion == "5":
            print("Adiós.")
            break

        if opcion not in ["1","2","3","4"]:
            print("Opción no válida.")
            continue

        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            print("Resultado:", suma(a,b))
        elif opcion == "2":
            print("Resultado:", resta(a,b))
        elif opcion == "3":
            print("Resultado:", multiplicacion(a,b))
        elif opcion == "4":
            print("Resultado:", division(a,b))

if __name__ == "__main__":
    main()
