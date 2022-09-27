import requests
from bs4 import BeautifulSoup
from player import Player
import pandas as pd

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
    
    def count_mistakes(self):
        page = requests.get(self.link).text
        soup = BeautifulSoup(page, 'html.parser')
        table = soup.find_all('div', {'class': 'sp-template sp-template-event-performance sp-template-event-performance-values'})
        for h in table:
            team_name = h.find('h4').text
            if team_name != 'Wolves Volley':
                table = h
                break
        tfoot = table.find('tfoot')
        # score = ilość zdobytych punktów przez przeciwnika
        score1 = tfoot.find('td', {'class': 'data-punktycznie'}).text

        result = soup.find('div', {'class': 'sp-section-content sp-section-content-results'}) # wynik meczu
        tbody = result.find('tbody')
        rows = tbody.find_all('tr')
        for row in rows:
            if row.find('td', {'class': 'data-name'}).text != 'Wolves Volley':
                s1 = row.find('td', {'class': 'data-one'}).text
                s2 = row.find('td', {'class': 'data-two'}).text
                s3 = row.find('td', {'class': 'data-tiebreak'}).text
                score2 = int(s1) + int(s2) + int(s3)
            else:
                pass
        # zwraca ilość popełnionych przez Wolves Volley błędów
        df = pd.DataFrame([[int(score2) - int(score1), team_name]], columns=['bledy', 'przeciwnik'])
        df1 = pd.read_csv('mistakes.csv')
        df = pd.concat([df1, df])
        df.to_csv('mistakes.csv', index=False)
        return int(score2) - int(score1), team_name
