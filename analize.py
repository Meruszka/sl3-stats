import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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
        name = i['name']
        surname = i['surname']
        plt.plot(i['przeciwnik'], i['punkty'], label=name+' '+surname)
    # plt.yticks(np.arange(0, 32, 2.0))
    plt.grid(True)
    # plt.legend()
    plt.show()


def get_mistakes() -> pd.DataFrame:
    df = pd.read_csv('Fetching/mistakes.csv', index_col=False).iloc[::-1]
    return df


def plot_mistakes(mistakes: pd.DataFrame):
    mistakes.plot(x='przeciwnik', y='bledy', kind='line')
    plt.legend()
    plt.show()


plot_player(get_all_players())
