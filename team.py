import requests
from player import Player
from bs4 import BeautifulSoup
import tqdm

class Team:
    def __init__(self, name):
        self.name = self.no_polish_letters(name)
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
    def fetch_players(self):
        data = requests.get(f'https://www.sl3.com.pl/team/{self.name}/').text
        soup = BeautifulSoup(data, 'html.parser')
        rows = soup.find('tbody').findAll('tr')
        for row in rows:
            number = row.find('td').text
            name, surname = row.find('td', {'class': 'data-name'}).text.split(' ')
            player = Player(name, surname, number)
            self.add_player(player)
    def add_player(self, player):
        self.players.append(player)
    def delete_player(self, player):
        self.players.remove(player)
    def get_all_players(self):
        for player in tqdm(self.players):
            player.to_csv()
