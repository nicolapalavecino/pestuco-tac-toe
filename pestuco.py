# Voy a tratar de armar mi propio juego de piedra, papel o tijera.
import random, sys

print('Bienvenido a piedra, papel o tijera by Pestita')

wins = 0
losses = 0
ties = 0

selectionText = {
    'pi': 'piedra',
    'pa': 'papel',
    't': 'tijera'
}

while True:
    print ('Wins = ' + str(wins) + ' Losses = ' + str(losses) + ' Ties = ' + str(ties))

    #Eleccion del jugador
    jugador = playerSelection()

    #Display de eleccion del jugador
    print ("Elegiste {}, yo elijo ...".format(selectionText[jugador]))

    #Eleccion y display de maquina aleatoria
    eleccion_maquina = machineSelection()
    print("{}".format(selectionText[eleccion_maquina]).capitalize())

    #Batalla empates
    if jugador == 'pi' and maquina == 'pi':
        tie()
    elif jugador == 'pa' and maquina == 'pa':
        tie()
    elif jugador == 't' and maquina == 't':
        tie()

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

def playerSelection():
    while True:
        print ('Elegis vos primero: piedra (pi), papel (pa) o tijera (t)? Para salir elige (q)')
        selection = input()
        if selection == 'pi' or selection == 'pa' or selection == 't':
            return selection
        if selection == 'q':
            sys.exit()
        else:
            print ('Escribiste cualquier cosa')

def machineSelection():
    options = ['pi', 'pa', 't']
    return options[random.randint(0,2)]

def loose():
    print ('Perdiste')
    losses = losses + 1

def win():
    print ('Ganaste')
    wins = wins + 1

def tie():
    print ('Es un empate')
    ties = ties + 1