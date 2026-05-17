dinero = 30

print ("¡Bienvenido a la tienda de michis!")

while dinero > 0:
    
    print (f"Tu dinero: {dinero}")
    
    print ("Gato misterioso - 15 monedas")
    
    print ("Gato normal - 5 monedas")
    
    print ("Gato explosivo - 10 monedas")
    
    opcion = input ("¿Qué gato quieres comprar? (misterioso/normal/explosivo): ")
    
    if opcion == "misterioso":
        
        print ("Seguro? ¡Es un gato misterioso!")
        
        confirmacion = input ("¿Estas super seguro? (si/no): ")
        
    if confirmacion == "si":
        
        dinero = dinero - 15
        
        print ("¡Has comprado un gato misterioso!")
        
    if confirmacion == "no":
        
        print ("Buena eleccion, el gato misterioso es peligroso")
        
    if opcion == "misterioso":
        
        print ("El gato misterioso ha roto mi tienda... ¡Fuera de mi tienda!")
        dinero = -500
        
    elif opcion == "normal":
        
        dinero = dinero - 5
        
        print ("¡Has comprado un gato normal!")
        
    elif opcion == "explosivo":
        
        dinero = dinero - 10
        
        print ("¡Has comprado un gato explosivo!")
        
if dinero <= 0:
    
    print ("Te has quedado sin dinero... ¡Fuera de mi tienda!")
