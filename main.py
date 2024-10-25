import os

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
    print("1) Assignar jugador Vermell")
    print("2) Assignar jugador Blau")
    print("3) Assignar jugador Verd")
    print("4) Assignar jugador Groc")
    print("5) Començar partida")
    print("6) Sortir")

def main():
    #Se presenta el menú de juego con las opciones disponibles
    #El usuario elige opción por consola:
        #Si no hay al menos 2 jugadores asignados, no puede comenzar la partida
        #Si el jugador asigna un input no válido, sigue preguntando input hasta que este sea correcto

    #Comienzo partida