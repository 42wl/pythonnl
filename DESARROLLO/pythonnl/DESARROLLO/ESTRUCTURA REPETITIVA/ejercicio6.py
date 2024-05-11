#Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un total de n personas 

import random

hombres=0
mujeres=0

for i in range (20):
    sexo = random.choice(['hombre' , 'mujer'])
    
    if sexo == 'hombre':
        hombres +=1
    else:
        mujeres +=1
        
print(f'hay {hombres} hombres en el salon')
print(f'hay {mujeres} mujeres en el salon')

    