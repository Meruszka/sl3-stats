from cProfile import label
from player import Player
import pandas as pd
import matplotlib.pyplot as plt


def get_player(name, surname, number) -> pd.DataFrame:
    df = Player(name, surname, number).from_csv()
    df = df[df['Sety'] != 0]
    return df

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

def plot_player(player_data):
    plt.plot(player_data["Sezon"].values, player_data["Pkt/Set"].values, label='pkt/set')
    plt.plot(player_data["Sezon"].values, player_data["Ataki / Set"].values, label='ataki/set')
    plt.plot(player_data["Sezon"].values, player_data["Bloki / Set"].values, label='bloki/set')
    plt.plot(player_data["Sezon"].values, player_data["Asy /  Set"].values, label='asy/set')
    print(player_data["Sety"])
    plt.legend()
    plt.show()

p1 = get_player('Mikołaj', 'Stempin', 6)
p1 = set_position(p1)
plot_player(p1)