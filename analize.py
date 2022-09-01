from cProfile import label
from player import Player
import pandas as pd
import matplotlib.pyplot as plt


def get_player(name, surname, number) -> pd.DataFrame:
    df = Player(name, surname, number).from_csv()
    df= df[df['Sety'] != 0]
    print(df)
    return df

def plot_player(player_data):
    plt.plot(player_data["Sezon"].values, player_data["Pkt/Set"].values, label='pkt/set')
    plt.show()

plot_player(get_player('Michał', 'Niewiadomski', 25))