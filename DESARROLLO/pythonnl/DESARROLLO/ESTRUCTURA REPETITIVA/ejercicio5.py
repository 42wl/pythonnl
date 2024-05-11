#. Una persona debe realizar un muestreo con 50 personas para determinar el promedio de peso de los niños, jovenes, adultos y ancianos que existen en su zona 
niño=0-12
joven=13-29
adulto=30-59
ancianos=60 

"contadores"
pesoniño=0
pesojoven=0
pesoadulto=0
pesoanciano=0

cantidadniño=0
cantidadjoven=0
cantidadadulto=0
cantidadanciano=0

for i in range(50):
    edad=int(input("ingrese la edad"))
    peso=int(input("ingrese el peso"))
if 0<=edad<=12:
    pesoniño+=peso
    cantidadniño+=1
elif 13<=edad<=29:
    pesojoven+=peso
    cantidadjoven+=1
elif 30<= edad<=59:
    pesoadulto+=peso
    cantidadadulto+=1
else:
    pesoanciano+=peso
    cantidadanciano+=1
    
promedioniño=pesoniño/cantidadniño if cantidadniño> 0 else 0 
promediojoven=pesojoven/cantidadjoven if cantidadjoven> 0 else 0 
promedioadulto=pesoadulto/cantidadadulto if cantidadadulto> 0 else 0 
promedioanciano=pesoanciano/cantidadanciano if cantidadanciano> 0 else 0

print("promedio de peso de niño:",promedioniño)
print("promedio de peso de joven:",promediojoven)
print("promedio de peso adulto:",promedioadulto)
print("promedio de peso ancianos:",promedioanciano)    
