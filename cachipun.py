import random

import random as r

# from random import funcion 

def cachipun():

    opciones= ["piedra","papel","tijera"]#opciones del computador

    jugador= input("Ingrese una opción (piedra,papel,tijera): ").lower()



    if jugador not in opciones: # si la elección no está en las opciones,lanza error.

        print("Opción no válida")



    else:

        oponente= random.choice(opciones)

        print(f"El oponente escogió: {oponente}")

   

    # situaciones donde gana el jugador

        if (jugador == "piedra" and oponente ==" tijera") or (jugador== "papel" and oponente== "piedra") or (jugador=="tijera" and oponente==" papel"):

            print("Ganaste")

   

    # situación donde empatan

        elif  jugador == oponente:

            print("Empate")

       

    # situación donde el jugador pierde

        else:

            print("Perdiste")

if __name__ == "__main__":
   cachipun()