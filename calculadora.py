# Funciones para realizar operaciones matemáticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b
  
def multiplicacion(a, b):
    return a * b
  
def division(a, b):
    return a // b

def potencia(a, b):
    return a ** b 

# Programa principal
if __name__ == "__main__":
    print("Calculadora Simple")
    while True:
        print("\nOpciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicar")
        print("4. División")
        print("5. Potencia")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1/2/3/4/5/6): ")

        if opcion == '6':
            print("¡Hasta luego!")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print("Resultado: ", suma(num1, num2))
        elif opcion == '2':
            print("Resultado: ", resta(num1, num2))
        elif opcion == '3':
            print("Resultado: ", multiplicacion(num1, num2))    
        elif opcion == '4':
            print("Resultado: ", division(num1, num2))
        elif opcion == '5':
            print("Resultado: ", potencia(num1, num2))
        else:
            print("Opción no válida. Intente nuevamente.")
