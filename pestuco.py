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
    global wins, losses, ties
    print ('Wins = ' + str(wins) + ' Losses = ' + str(losses) + ' Ties = ' + str(ties))

    jugador = playerSelection()
    print ("Elegiste {}, yo elijo ...".format(selectionText[jugador]))

    eleccion_maquina = machineSelection()
    print("{}".format(selectionText[eleccion_maquina]).capitalize())

    outcome = matchOutcomes[jugador + '/' + eleccion_maquina]
    if outcome == 'tie':
        ties = tie(ties)
    elif outcome == 'win':
        wins = win(wins)
    elif outcome == 'loose':
        losses = loose(losses)

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

def loose(losses):
    print ('Perdiste')
    return losses + 1

def win(wins):
    print ('Ganaste')
    return wins + 1

def tie(ties):
    print ('Es un empate')
    return ties + 1

while True:
    main()