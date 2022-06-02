calificacion = input ("Introduce tu calificaciñon del AL-900: ")
# Comparamos si su calificación es menor que un determinado valor
valor = int(calificacion)
if valor < 700:
    print("Ves, por no estudiar")
elif valor > 1000:
    print("Mentiroso, no se puede sacar más de 1000 puntos")
else:
    print("Gracias por estudiar")


edad = input("Introduce tu edad: ")
num = int(edad)

if num >= 18 and num <= 100:
    print("Vienvenido al mom")
elif num >= 120: 
    print("A caso eres chavelo")
elif num < 0:
    print("Ni que fueras viajero del tiempo")
else: 
    print("No te podemos vender cigarros")

