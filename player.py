import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

class Player:
    def __init__(self, name, surname, number):
        self.name = self.no_polish_letters(name)
        self.surname = surname
        self.number = number
        self.link = f'https://www.sl3.com.pl/player/{self.name}-{self.surname}'
        self.data = self.fetch_data()
        self.df = self.data_to_pandas()
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
    def fetch_data(self):
        data = requests.get(self.link).text
        soup = BeautifulSoup(data, 'html.parser')
        tables = soup.findAll('div', {'class': 'sp-template sp-template-player-statistics'})
        return tables
    def get_data(self, table):
        data = {}
        for row in table.find('thead').findAll('th'):
            key = row.text
            class_ = row.get('class')[0]
            value = table.find('tbody').find('td', {'class': class_}).text
            data[key] = value
        return data
    def data_to_pandas(self):
        data = []
        for table in self.data[:-1]:
            data.append(self.get_data(table))
        df = pd.DataFrame(data)
        return df
    def to_csv(self):
        t = time.strftime('%Y-%m-%d')
        self.df.to_csv(f'./data/{self.name}-{self.surname}_{self.number}_{t}.csv')
