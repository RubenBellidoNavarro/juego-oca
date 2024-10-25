import os
import string

def clearScreen() -> None:
    '''Limpiamos la pantalla de la terminal.
    
    Input: None
    
    Output: None'''
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')

def imprimeixMenuPrincipal():
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
    return int(input("Escull una opció [0 - 5]: "))

def nomValid(nomJugador):
    #El nombre del jugador sólo puede contener letras y espacios:
    nomValid = True
    for char in nomJugador:
        noEsLletra = char.lower() not in string.ascii_lowercase
        noEsEspai = char != " "
        if noEsLletra and noEsEspai:
            nomValid = False
    return nomValid

def assignaColor(color, jugadorsAsignats):
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
        nomJugador = input(f"Escull un jugador per la firxa {colorFitxa}: ")
        if nomValid(nomJugador):
            jugadorsAsignats[color] = nomJugador
            return
        print(f'El nom escollit no és vàlid.')

def jocPotIniciar(jugadorsAsignats):
    #Cuenta los jugadores asignados:
    quantitatJugadors = 0
    for fitxa in jugadorsAsignats:
        if jugadorsAsignats[fitxa] is not None:
            quantitatJugadors += 1

    #Si hay al menos 2 jugadores, retorna True:
    if quantitatJugadors >= 2:
        return True
    return False

def menuPrincipal():
    jugadorsAsignats =  {
                        "Vermell":None,
                        "Blau":None,
                        "Verd":None,
                        "Groc":None
                        }
    while True:
        imprimeixMenuPrincipal(jugadorsAsignats)
        opcioEscollida = inputMenuPrincipal()
        if opcioEscollida == 1:
            assignaColor("Vermell", jugadorsAsignats)
        elif opcioEscollida == 2:
            assignaColor("Blau", jugadorsAsignats)
        elif opcioEscollida == 3:
            assignaColor("Verd", jugadorsAsignats)
        elif opcioEscollida == 4:
            assignaColor("Groc", jugadorsAsignats)
        elif opcioEscollida == 5:
            if jocPotIniciar(jugadorsAsignats):
                break
            continue
        elif opcioEscollida == 6:
            sortirJoc(jugadorsAsignats)


def main():
    menuPrincipal()

if __name__ == "__main__":
    pass