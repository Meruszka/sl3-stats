def set_position(player_data):
    #Ustala pozycje w każdym sezonie...
    player_data['Pozycja'] = None
    # Libero nie atakuje
    player_data.loc[player_data['Ataki / Set'] == '0.00', 'Pozycja'] = 'Libero'

    # Setter atakuje mało, serwuje
    player_data.loc[player_data['Ataki / Set'] <= 0.50, 'Pozycja'] = 'Setter'

    # Attak najwięcej atakuje
    player_data.loc[player_data['Ataki / Set'] >= 1.00, 'Pozycja'] = 'Attack'
    
    # Middle najwięcej blokuje (chyba)
    player_data.loc[player_data['Bloki / Set'] >= 0.5, 'Pozycja'] = 'Middle'

    return player_data  