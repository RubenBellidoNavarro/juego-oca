import os

def clearScreen() -> None:
    '''Limpiamos la pantalla de la terminal.
    
    Input: None
    
    Output: None'''
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')