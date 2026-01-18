class PointSystem:
    def __init__(self):
        self.player_points = 0
        self.enemy_points = 0

    def increase_player(self):
        self.player_points += 1
    
    def increase_enemy(self):
        self.enemy_points += 1