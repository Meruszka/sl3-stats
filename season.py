class Season:
    def __init__(self, name) -> None:
        if name == 'Jesień':
            self.name = 'Jesień'
            self.mouths = ['września', 'października', 'listopada']
        elif name == 'Wiosna':
            self.name = 'Wiosna'
            self.mouths = ['marca', 'kwietnia', 'maja']