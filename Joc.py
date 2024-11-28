def joc(jugadorsAssignats)->None:
    '''Gestiona la partida y sus funcionalidades.
    
    Input:
        -jugadorsAssignats(dict): diccionario con estructura {'color':'nomJugador'}.
    
    Output: None'''
    jugadors = generaJugadors(jugadorsAssignats)
    tauler = generaTauler()
    asignaJugadorsTauler() #Pone a los jugadores en la casilla que toca (en este caso, en la 0)
    imprimeixTauler()