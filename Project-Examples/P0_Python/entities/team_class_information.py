class Team:

    # I need a team name, and I need a team home city
    def __init__(self, team_id: int, team_name:str, home_city:str):
        self.team_id = team_id # it is also good practice to give each object a unique identifier, so each team needs an Id
        self.team_name = team_name
        self.home_city = home_city

    def convert_to_dictionary(self):
        return {
            "teamId": self.team_id,
            "teamName": self.team_name,
            "homeCity": self.home_city
        }





# what is a team actually made of?
"""
teams have players
teams have a home city
teams have an owner
teams have names

this list could go on, but I will focus on three of these: players, home city, and names

players are going to be their own entities, so I don't need to put their information inside of the team class, so
I only need to focus on making sure team entities have a designated home city, and a name
"""