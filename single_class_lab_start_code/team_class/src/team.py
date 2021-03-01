class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.coach = coach
        self.players = players
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player) 

    def has_player(self, player_name):
        return player_name in self.players   

    def play_game(self, won):
        if won:
            self.points += 3
        
