from player import *
from team import *

with open ('team.txt', encoding='utf-8', mode='r') as f:
    data = f.readlines()
    team_name = data[0]
    team = Team(team_name)
    for line in data[1:]:
        name, surname = line.split()
        player = Player(name, surname)
        team.add_player(player)
team.get_all_players()

