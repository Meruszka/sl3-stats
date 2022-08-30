class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
    def add_player(self, player):
        self.players.append(player)
    def delete_player(self, player):
        self.players.remove(player)
    def get_all_players(self):
        for player in self.players:
            player.df.to_csv(f'data_{player.name}-{player.surname}.csv')
