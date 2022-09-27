import requests
from bs4 import BeautifulSoup
from season import Season
from team import Team

class Game:
    def __init__(self, link) -> None:
        self.link = link
        self.players = []
    
    def fetch_data(self):
        page = requests.get(self.link).text
        soup = BeautifulSoup(page, 'html.parser')
        soup = soup.find_all('div', {'class': 'sp-template sp-template-event-performance sp-template-event-performance-values'})
        for h in soup:
            # Tutaj jest problem z nazwą drużyny!! Nie wiem jak to rozwiązać
            if h.find('h4').text == 'Wolves Volley':
                soup = h
                break
        rows = soup.find('tbody')
        for row in rows:
            number = row.find('td', {'class': 'data-number'}).text
            name = row.find('td', {'class': 'data-name'}).text
            punkty = row.find('td', {'class': 'data-punktycznie'}).text
            sety = row.find('td', {'class': 'data-sety'}).text
            mvp = row.find('td', {'class': 'data-mvp'}).text
            ataki = row.find('td', {'class': 'data-a'}).text
            bloki = row.find('td', {'class': 'data-b'}).text
            asy = row.find('td', {'class': 'data-digs'}).text
            self.players.append({
                'number': number,
                'name': name.split(' ')[0],
                'surname': name.split(' ')[1],
                'punkty': punkty,
                'sety': sety,
                'mvp': mvp,
                'ataki': ataki,
                'bloki': bloki,
                'asy': asy
            })