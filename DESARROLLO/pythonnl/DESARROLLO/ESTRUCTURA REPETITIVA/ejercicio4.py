#Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se digitara por teclado. imprimir el multiplicando, el multiplicador y el producto 
numero= int(input("ingresar un numero para la tabla de multiplicar:"))
for multiplicador in range(1,11):
            producto = numero * multiplicador 
            print(numero, "x", multiplicador , "=", producto)
            
            