# en un supermercado se ha implementado la estrategia de desuente, segun el valor de la compra y la balota que el cliente saque de la bolsa secreta. las condiciones se alistan a conatinuacion: 1 si el valor de la compra es superior a 50.000 pesos y saca: A. balota roja el descuento sera del 10%, B. balota verde el descuento sera del 15%, C. balota azul el desuento sera del 20%, D. balota amarilla el descuento sera del 50%, E. balota negra el descuento sera del 100%. si la compra es inferior a 50.000 pesos no participa del sorteo, para este caso se muetra un mensaje y se imprima solo el valor a pagar. elabore un algoritmo que permita leer la compra evaluar las condiciones e imprima el valor de la compra, e color de la bola el valor del descuento y el valor a pagar 

precio= int(input("valor compra"))

balotaroja= (precio-0.1)
balotaverde= (precio-0.15)
balotaazul= (precio-0.2)
balotaamarilla= (precio-0.5)
balotanegra= (precio-100)
if precio > 50000:
    balota = input("que balota obtuvo")
    if balota == "roja":
        print(f"su descuento es:{balotaroja}")
    elif balota == "verde":
         print(f"su descuento es:{balotaverde}")
    elif balota == "azul":
         print(f"su descuento es:{balotaazul}")
    elif balota == "amarilla":
         print(f"su descuento es:{balotaamarilla}")
    elif balota == "negra":
         print(f"su descuento es:{balotanegra}")
else: print("no tiene descuento")
     