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

matchOutcomes = {
    'pi/pi': 'tie',
    'pa/pa': 'tie',
    't/t': 'tie',
    'pi/t': 'win',
    'pa/pi': 'win',
    't/pa': 'win',
    'pi/pa': 'loose',
    'pa/t': 'loose',
    't/pi': 'loose',
}

def main():
    print ('Wins = ' + str(wins) + ' Losses = ' + str(losses) + ' Ties = ' + str(ties))

    jugador = playerSelection()
    print ("Elegiste {}, yo elijo ...".format(selectionText[jugador]))

    eleccion_maquina = machineSelection()
    print("{}".format(selectionText[eleccion_maquina]).capitalize())

    outcome = matchOutcomes[jugador + '/' + eleccion_maquina]
    if outcome == 'tie':
        tie()
    elif outcome == 'win':
        win()
    elif outcome == 'loose':
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

while True:
    main()