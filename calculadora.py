# Funciones para realizar operaciones matemáticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def division(a, b):
    return a // b

# Programa principal
if __name__ == "__main__":
    print("Calculadora Simple")
    while True:
        print("\nOpciones:")
        print("1. Suma")
        print("2. Resta")
        print("4. División")
        print("5. Salir")

        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print("Resultado: ", suma(num1, num2))
        elif opcion == '2':
            print("Resultado: ", resta(num1, num2))
        elif opcion == '4':
            print("Resultado: ", division(num1, num2))
        else:
            print("Opción no válida. Intente nuevamente.")
