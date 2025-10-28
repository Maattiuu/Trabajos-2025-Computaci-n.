def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if b!=0:
        return a/b
    else:
            return "ERROR: Division por cero, neles pasteles"
            
    print("operaciones disponibles")
    print("1.Suma")
    print("2.Resta")
    print("3.multiplicacion")
    print("4.Division")
    
    opcion = input ("Elegi la opcion (1/2/3/4);:")
    
    num1 = float(input("Ingresa el primer numero brou"))
    num2 = float(input("Ingresa el segundo numero brou"))
    
    if opcion == '1':
        print("Resutado", sumar(num1, num2))
    elif opcion == '2':
        print("Resutado", restar(num1, num2))
    elif opcion == '3':
        print("Resutado", multiplicar(num1, num2))
    elif opcion == '4':
        print("Resutado", dividir(num1, num2))
    else:
            print("Operacion Valida")