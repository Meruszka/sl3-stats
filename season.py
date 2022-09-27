class Season:
    def __init__(self, name, year) -> None:
        self.year = year
        if name == 'Jesień':
            self.name = 'Jesień'
            self.mouths = ['września', 'października', 'listopada']
        elif name == 'Wiosna':
            self.name = 'Wiosna'
            self.mouths = ['marca', 'kwietnia', 'maja']