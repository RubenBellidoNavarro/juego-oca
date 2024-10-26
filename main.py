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

#region MenuPrincipal
def jugadorAssignat(color:str, jugadorsAssignats:dict) -> bool:
    '''Comprobamos si a una ficha se le ha asignado un jugador.
    
    Input:
        -color(str): color de la ficha a comprobar.
        -jugadorsAssignats(dict): diccionario con estructura {'color':'nomJugador'}.
        
    Output: Bool'''
    if jugadorsAssignats[color] is None:
        return False
    return True

def imprimeixMenuPrincipal(jugadorsAssignats:dict) -> None:
    '''Se encarga de imprimir el menú principal del juego, con las posibles variaciones
    que este tenga dependiendo del estado del juego.
    
    Input:
        -jugadorsAssignats(dict): diccionario con estructura {'color':'nomJugador'}.
        
    Output: None'''
    clearScreen()

    print("La Oca")

    print("----------")

    jugador1 = '(no assignat)'
    if jugadorAssignat("Vermell",jugadorsAssignats):
        jugador1 = f'({jugadorsAssignats["Vermell"]})'
    print("1) Assignar jugador Vermell".ljust(30) + jugador1)

    jugador2 = '(no assignat)'
    if jugadorAssignat("Blau",jugadorsAssignats):
        jugador2 = f'({jugadorsAssignats["Blau"]})'
    print("2) Assignar jugador Blau".ljust(30) + jugador2)

    jugador3 = '(no assignat)'
    if jugadorAssignat("Verd",jugadorsAssignats):
        jugador3 = f'({jugadorsAssignats["Verd"]})'
    print("3) Assignar jugador Verd".ljust(30) + jugador3)

    jugador4 = '(no assignat)'
    if jugadorAssignat("Groc",jugadorsAssignats):
        jugador4 = f'({jugadorsAssignats["Groc"]})'
    print("4) Assignar jugador Groc".ljust(30) + jugador4)

    potIniciar = ""
    if not jocPotIniciar(jugadorsAssignats):
        potIniciar = "(no disponible)"
    print("5) Començar partida" + potIniciar.rjust(24))

    print("6) Sortir")

def inputMenuPrincipal():
    '''Pide al usuario que escoja una opción en el menú principal.
    
    Input: None
    
    Output: None'''
    inputUsuari = input("Escull una opció [1 - 6]: ")

    if inputUsuari.lower() == "assignar jugador vermell":
        inputUsuari = "1"
    elif inputUsuari.lower() == "assignar jugador blau":
        inputUsuari = "2"
    elif inputUsuari.lower() == "assignar jugador verd":
        inputUsuari = "3"
    elif inputUsuari.lower() == "assignar jugador groc":
        inputUsuari = "4"
    elif inputUsuari.lower() == "començar partida":
        inputUsuari = "5"
    elif inputUsuari.lower() == "sortir":
        inputUsuari = "6"

    if inputUsuari.isdigit():
        inputUsuari = int(inputUsuari)
        if inputUsuari in range (1,7):
            return inputUsuari

def nomValid(nomJugador):
    '''Comprueba que el nombre introducido sea válido (sólo contiene letras y espacios).
    
    Input: 
        -nomJugador(str): nombre del jugador a validar.
        
    Output: bool'''
    nomValid = True
    for char in nomJugador:
        noEsLletra = char.lower() not in string.ascii_lowercase
        noEsEspai = char != " "
        if noEsLletra and noEsEspai:
            nomValid = False
    return nomValid

def assignaColor(color, jugadorsAssignats):
    '''Modifica el nombre asociado a una ficha de un color determinado.
    
    Input:
        -color(str): color de la ficha cuyo nombre ha se modificarse.
        -jugadorsAssignats(dict): diccionario con estructura {'color':'nomJugador'}.
        
    Output: None'''
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
    '''Comprueba si puede comenzar la partida (al menos 2 jugadores asignados).
    
    Input:
        -jugadorsAssignats(dict): diccionario con estructura {'color':'nomJugador'}.
        
    Output: bool'''
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
    '''Sale del programa.
    
    Input:None
    
    Output:None'''
    sys.exit()

def menuPrincipal():
    '''Gestiona el menú principal del juego y sus funcionalidades.
    Retorna el diccionario 'jugadorsAssignats'.
    
    Input: None
    
    Output:
        -jugadorsAssignats(dict): diccionario con estructura {'color':'nomJugador'}.'''
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
                return jugadorsAssignats
        elif opcioEscollida == 6:
            sortirJoc()
#endregion MenuPrincipal

def generaJugadors(jugadorsAssignats:dict)->dict:
    '''Genera el diccionario de jugadores que participan en la partida.
    
    Input:
        -jugadorsAssignats(dict): diccionario con estructura {'color':'nomJugador'}.
        
    Output:
        -jugadorsPartida(dict)'''
    iconasJugadors =    {
                        'Groc':'G',
                        'Vermell':'V',
                        'Blau':'B',
                        'Verd':'D'
                        }
    jugadorsPartida = {}
    for colorFitxa in jugadorsAssignats:
        nomJugador = jugadorsAssignats[colorFitxa]
        if nomJugador is not None:
            jugadorsPartida[colorFitxa] =   {
                                            'nomJugador' = nomJugador,
                                            'posicio' = 0
                                            }
    return jugadorsPartida

def joc(jugadorsAssignats)->None:
    '''Gestiona la partida y sus funcionalidades.
    
    Input:
        -jugadorsAssignats(dict): diccionario con estructura {'color':'nomJugador'}.
    
    Output: None'''
    jugadors = generaJugadors()

def main():
    jugadorsAssignats = menuPrincipal()
    joc(jugadorsAssignats)

if __name__ == "__main__":
    main()