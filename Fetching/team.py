import requests
from bs4 import BeautifulSoup
from season import Season
from game import Game
import pandas as pd

class Team:
    def __init__(self, name, season, year) -> None:
        self.name = self.no_polish_letters(name)
        self.season = Season(season, year)
        self.make_csv()
        self.fetch_games()
    def no_polish_letters(self, string):
        dict = {
            'ą': 'a',
            'ć': 'c',
            'ę': 'e',
            'ł': 'l',
            'ń': 'n',
            'ó': 'o',
            'ś': 's',
            'ź': 'z',
            'ż': 'z'
        }
        for letter in string:
            if letter in dict:
                string = string.replace(letter, dict[letter])
        return string.replace(' ', '-')
    def fetch_games(self):
        page = requests.get(f'https://www.sl3.com.pl/team/{self.name}').text
        soup = BeautifulSoup(page, 'html.parser')
        soup = soup.find('div', {'class': "sp-tab-content sp-tab-content-events"})
        soup = soup.find_all('tbody')
        rows = soup[0].find_all('tr')
        games = []
        for row in rows:
            if len(set(self.season.mouths).intersection(row.text.split(' '))) > 0:
                year = row.text.split(' ')[0][0:4]
                if self.season.year == year:
                    row = row.find('td', {'class': 'data-results'})
                    row = row.find('a')
                    if row.text != '-':
                        games.append(row['href'])
        for game in games:
            Game(game).fetch_data()
        print(f'Zespoł {self.name} w sezonie {self.season.name} {self.season.year} grał {len(games)} meczów.')
    def make_csv(self):
        pd.DataFrame(columns=['name', 'surname', 'number', 'punkty', 'sety', 'mvp', 'ataki', 'bloki', 'asy']).to_csv('players.csv', index=False)