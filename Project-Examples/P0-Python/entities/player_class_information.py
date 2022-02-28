class Player:

    def __init__(self, player_id:int, team_id:int, first_name:str, last_name:str, jersey_number:int):
        self.player_id = player_id
        self.team_id = team_id
        self.first_name = first_name
        self.last_name = last_name
        self.jersey_number = jersey_number

"""
what do real players have in real life?

players have names
players have jersey numbers
players have a team they play for
players have families
players have friends
etc.

I am going to stick with their name, their jersey number, and their team
"""