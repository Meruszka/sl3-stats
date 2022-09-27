import requests
from bs4 import BeautifulSoup
from player import Player

class Game:
    def __init__(self, link) -> None:
        self.link = link
        self.players = []
    
    def fetch_data(self):
        page = requests.get(self.link).text
        soup = BeautifulSoup(page, 'html.parser')
        soup = soup.find_all('div', {'class': 'sp-template sp-template-event-performance sp-template-event-performance-values'})
        for h in soup:
            team_name = h.find('h4').text
            if team_name == 'Wolves Volley':
                soup = h
            else:
                enemy = team_name
        table = soup.find('tbody')
        rows = table.find_all('tr')
        for row in rows:
            name = row.find('td', {'class': 'data-name'}).text.split(' ')[0]
            surname = row.find('td', {'class': 'data-name'}).text.split(' ')[1]
            number = row.find('td', {'class': 'data-number'}).text
            punkty = row.find('td', {'class': 'data-punktycznie'}).text
            sety = row.find('td', {'class': 'data-sety'}).text
            mvp = row.find('td', {'class': 'data-mvp'}).text
            ataki = row.find('td', {'class': 'data-a'}).text
            bloki = row.find('td', {'class': 'data-b'}).text
            asy = row.find('td', {'class': 'data-digs'}).text
            self.players.append(Player(name, surname, number, punkty, sety, mvp, ataki, bloki, asy, enemy))
        for player in self.players:
            player.add_to_csv()