# Voy a tratar de armar mi propio juego de piedra, papel o tijera.
import random, sys

print('Bienvenido a piedra, papel o tijera by Pestita')

wins = 0
losses = 0
ties = 0

while True:
    print ('Wins = ' + str(wins) + ' Losses = ' + str(losses) + ' Ties = ' + str(ties))

    #Eleccion del jugador
    while True:
        print ('Elegis vos primero: piedra (pi), papel (pa) o tijera (t)? Para salir elige (q)')
        jugador = input()
        if jugador == 'pi' or jugador == 'pa' or jugador == 't':
            break
        if jugador == 'q':
            sys.exit()
        else:
            print ('Escribiste cualquier cosa')

    #Display de eleccion del jugador
    if jugador == 'pi':
        print ('Elegiste piedra, yo elijo ...')
    elif jugador == 'pa':
        print ('Elegiste papel, yo elijo ...')
    elif jugador == 't':
        print ('Elegiste tijera, yo elijo ...')

    #Eleccion y display de maquina aleatoria
    eleccion_maquina = random.randint (1, 3)
    if eleccion_maquina == 1:
        maquina = 'pi'
        print ('Piedra')
    elif eleccion_maquina == 2:
        maquina = 'pa'
        print ('Papel')
    elif eleccion_maquina == 3:
        maquina = 't'
        print ('Tijera')

    #Batalla empates
    if jugador == 'pi' and maquina == 'pi':
        print ('Es un empate')
        ties = ties + 1
    elif jugador == 'pa' and maquina == 'pa':
        print ('Es un empate')
        ties = ties + 1
    elif jugador == 't' and maquina == 't':
        print ('Es un empate')
        ties = ties + 1

    #Batalla victorias
    if jugador == 'pi' and maquina == 't':
        win()
    elif jugador == 'pa' and maquina == 'pi':
        win()
    elif jugador == 't' and maquina == 'pa':
        win()

    #Batalla derrotas
    if jugador == 'pi' and maquina == 'pa':
        loose()
    elif jugador == 'pa' and maquina == 't':
        loose()
    elif jugador == 't' and maquina == 'pi':
        loose()

def loose():
    print ('Perdiste')
    losses = losses + 1

def win():
    print ('Ganaste')
    wins = wins + 1