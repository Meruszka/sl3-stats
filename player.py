import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd
import time
import season as s

class Player:
    def __init__(self, name, surname, number, season) -> None:
        self.name = self.no_polish_letters(name)
        self.surname = surname
        self.number = number
        self.link = f'https://www.sl3.com.pl/player/{self.name}-{self.surname}'
        self.seasons = s.Season(season)
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
        return string
    def get_matches_links(self):
        links = []
        data = requests.get(self.link).text
        soup = BeautifulSoup(data, 'html.parser')
        soup = soup.find('div', {'class': 'sp-tab-group'})
        events = soup.find_all('a')
        for event in events:
            if len(event.text.split(' ')) > 3:
                if event.text.split(' ')[2] in self.seasons.mouths:
                    links.append(event['href'])
        return links
    def get_match_data(self, link):
        data = requests.get(link).text
        soup = BeautifulSoup(data, 'html.parser')

    def get_matches_data(self):
        links = self.get_matches_links()
        data = []
        for link in links:
            data.append(self.get_match_data(link))
        return data

p = Player('Szymon', 'Merski', 17, 'Jesień')
print(p.fetch_data())