#La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad
#de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo
#dígito de la placa de cada carro, se puede determinar el color de la calcomanía
#utilizando la siguiente relación
amarilla=0
rosa=0
roja=0
verde=0
azul=0
while True:
    ingresoAuto=int(input("ingrese el digito de la placa :"))
    ultimoDigito=int(ingresoAuto)%10
    if ingresoAuto==-9:
        break 
             
    if ultimoDigito == 1 or ultimoDigito == 2:
        amarilla+=1
        print("a ingresado un auto con calcomania amarilla")
    elif ultimoDigito == 3 or ultimoDigito == 4:
        rosa+=1
        print("a ingresado un auto con calcomania rosa")
    elif ultimoDigito == 5 or ultimoDigito == 6:
         roja+=1
         print("a ingresado un auto con calcomania roja")
    elif ultimoDigito == 7 or ultimoDigito == 8:
        verde+=1
        print("a ingresado un auto con calcomania verde")
    elif ultimoDigito == 0 or ultimoDigito ==9:
        azul+=1
        print("a ingresado un auto con calcomania azul")
        
        
        
print(f"{amarilla} tiene calcomania amarilla")   
print(f"{rosa} tiene calcomania rosa")  
print(f"{roja} tiene calcomania roja")  
print(f"{verde} tiene calcomania verde")  
print(f"{azul} tiene calcomania azul")

print("la cantidad de autos con calcomania amarilla:",amarilla)
print("la cantidad de autos con calcomania rosa:",rosa)
print("la cantidad de autos con calcomania roja:",roja)
print("la cantidad de autos con calcomania verde:",verde)
print("la cantidad de autos con calcomania azul:",azul)

  