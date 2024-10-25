import os
import string
import sys

def clearScreen() -> None:
    '''Limpiamos la pantalla de la terminal.
    
    Input: None
    
    Output: None'''
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')

def imprimeixMenuPrincipal(jugadorsAssignats):
    clearScreen()
    print("La Oca")
    print("----------")
    print("1) Assignar jugador Vermell".ljust(30))
    print("2) Assignar jugador Blau".ljust(30))
    print("3) Assignar jugador Verd".ljust(30))
    print("4) Assignar jugador Groc".ljust(30))
    print("5) Començar partida")
    print("6) Sortir")

def inputMenuPrincipal():
    return int(input("Escull una opció [1 - 6]: "))

def nomValid(nomJugador):
    #El nombre del jugador sólo puede contener letras y espacios:
    nomValid = True
    for char in nomJugador:
        noEsLletra = char.lower() not in string.ascii_lowercase
        noEsEspai = char != " "
        if noEsLletra and noEsEspai:
            nomValid = False
    return nomValid

def assignaColor(color, jugadorsAssignats):
    if color == "Vermell":
        colorFitxa = "Vermella"
    elif color == "Blau":
        colorFitxa = "Blava"
    elif color == "Verd":
        colorFitxa = "Verda"
    elif color == "Groc":
        colorFitxa = "Groga"

    clearScreen()
    while True:
        nomJugador = input(f"Escull un jugador per la fitxa {colorFitxa}: ")
        if nomValid(nomJugador):
            jugadorsAssignats[color] = nomJugador
            return
        print(f'El nom escollit no és vàlid.')

def jocPotIniciar(jugadorsAssignats):
    #Cuenta los jugadores asignados:
    quantitatJugadors = 0
    for fitxa in jugadorsAssignats:
        if jugadorsAssignats[fitxa] is not None:
            quantitatJugadors += 1

    #Si hay al menos 2 jugadores, retorna True:
    if quantitatJugadors >= 2:
        return True
    return False

def sortirJoc():
    sys.exit()

def menuPrincipal():
    jugadorsAssignats =  {
                        "Vermell":None,
                        "Blau":None,
                        "Verd":None,
                        "Groc":None
                        }
    while True:
        imprimeixMenuPrincipal(jugadorsAssignats)
        opcioEscollida = inputMenuPrincipal()
        if opcioEscollida == 1:
            assignaColor("Vermell", jugadorsAssignats)
        elif opcioEscollida == 2:
            assignaColor("Blau", jugadorsAssignats)
        elif opcioEscollida == 3:
            assignaColor("Verd", jugadorsAssignats)
        elif opcioEscollida == 4:
            assignaColor("Groc", jugadorsAssignats)
        elif opcioEscollida == 5:
            if jocPotIniciar(jugadorsAssignats):
                break
            continue
        elif opcioEscollida == 6:
            sortirJoc()


def main():
    menuPrincipal()

if __name__ == "__main__":
    main()