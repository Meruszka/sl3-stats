import pandas as pd

class Player:
    def __init__(self, name, surname, number, punkty, sety,  mvp, ataki, bloki, asy, enemy) -> None:
        self.name = self.no_polish_letters(name)
        self.surname = self.no_polish_letters(surname)
        self.number = number
        self.punkty = punkty
        self.sety = sety
        self.mvp = mvp
        self.ataki = ataki
        self.bloki = bloki
        self.asy = asy
        self.enemy = enemy
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
        df1 = pd.read_csv('players.csv')
        df2 = pd.DataFrame([[self.name, self.surname, self.number, self.punkty, self.sety, self.mvp, self.ataki, self.bloki, self.asy, self.enemy]], columns=['name', 'surname', 'number', 'punkty', 'sety', 'mvp', 'ataki', 'bloki', 'asy', 'przeciwnik'])
        df = pd.concat([df1, df2])
        df.to_csv('players.csv', index=False)