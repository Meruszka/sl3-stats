import requests
from bs4 import BeautifulSoup
from season import Season

class Team:
    def __init__(self, name, season, year) -> None:
        self.name = self.no_polish_letters(name)
        self.season = Season(season, year)
        self.players = []
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
                    games.append(row['href'])
        self.games = games
        return games
t = Team('wilki północy', 'Jesień', '2022')
t.fetch_games()
