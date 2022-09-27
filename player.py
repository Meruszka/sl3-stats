import pandas as pd

class Player:
    def __init__(self, name, surname, number, punkty, sety,  mvp, ataki, bloki, asy) -> None:
        self.name = self.no_polish_letters(name)
        self.surname = self.no_polish_letters(surname)
        self.number = number
        self.punkty = punkty
        self.sety = sety
        self.mvp = mvp
        self.ataki = ataki
        self.bloki = bloki
        self.asy = asy
        self.link = f'https://www.sl3.com.pl/player/{self.name}-{self.surname}'
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
    def add_to_csv(self):
        df = pd.read_csv('players.csv')
        df = df.append({
            'name': self.name,
            'surname': self.surname,
            'number': self.number,
            'punkty': self.punkty,
            'sety': self.sety,
            'mvp': self.mvp,
            'ataki': self.ataki,
            'bloki': self.bloki,
            'asy': self.asy,
            'link': self.link
        }, ignore_index=True)
        df.to_csv('players.csv', index=False)