def operaciones_basicas(a, b):
    print(f"\nsuma: {a + b}\n")
    print(f"\nresta_1: {a - b}\n")
    print(f"\nresta_2: {b - a}\n")
    print(f"\nmultiplicacion: {a * b}\n")
    print(f"\ndivision_1: {a / b}\n")
    print(f"\ndivision_2: {b / a}\n")

S = True

while S == True:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    operaciones_basicas(num1, num2)

    x = input("Realizar otra operacion: (S/N)").upper()
    if x == "N":
        S = False
        print("adios")