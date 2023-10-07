# Importar el módulo de la calculadora
import calculadora

# Programa principal
if __name__ == "__main__":
    while True:
        print("\nCalculadora Simple")
        print("Opciones:")
        print("1. Realizar cálculos")
        print("2. Salir")

        opcion = input("Seleccione una opción (1/2): ")

        if opcion == '2':
            print("¡Hasta luego!")
            break
        elif opcion == '1':
            print("\nOperaciones disponibles:")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")

            operacion = input("Seleccione una operación (1/2/3/4): ")

            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if operacion == '1':
                print("Resultado: ", calculadora.suma(num1, num2))
            elif operacion == '2':
                print("Resultado: ", calculadora.resta(num1, num2))
            elif operacion == '3':
                print("Resultado: ", calculadora.multiplicacion(num1, num2))
            else:
                print("Operación no válida. Intente nuevamente.")
