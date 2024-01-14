import time
numero = 0
numero2 = 0
minutos = input("Cuantos minutos tardara el temporizador?")

while numero2 != int(minutos):
    if numero2 == 10 and numero != 10 and numero < 10:
        print(10,":",0,numero)
    elif numero == 10 and numero2 != 10 and numero2 < 10:
        print(0,numero2,":",10)
    elif numero2 == 10 and numero == 10:
        print(10,":",10)
    if numero >= 60:
        numero = 0
        numero2 = numero2 + 1
    if numero2 < 10 and numero < 10:
        print(0,numero2,":",0,numero)
    elif numero2 or numero > 10 and not numero2 > 10 and numero > 10:
        if numero2 < 10 and numero > 10:
            print(0,numero2,":",numero)
        elif numero2 > 10 and numero < 10:
            print(numero2,":",0,numero)
    elif numero2 > 10 and numero > 10:
        print(numero2,":",numero)

    numero = numero + 1
    time.sleep(1)
print("El temporizador a terminado!")