from Fetching.player import Player
import pandas as pd
import matplotlib.pyplot as plt


def get_player(number) -> pd.DataFrame:
    df = pd.read_csv('Fetching/players.csv', index_col=False).iloc[::-1]
    player = df[df['number'] == number]
    return player

def get_all_players() -> list:
    df = pd.read_csv('Fetching/players.csv', index_col=False).iloc[::-1]
    players = []
    for i in df['number'].unique():
        players.append(get_player(i))
    return players

def plot_player(players: list):
    for i in players:
        name = i['name'].values[0]
        surname = i['surname'].values[0]
        plt.plot(i['przeciwnik'], i['punkty'], label=name+' '+surname)
    plt.legend()
    plt.show()

plot_player(get_all_players())
