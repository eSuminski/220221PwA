from custom_exceptions.id_not_found import IdNotFound
from dal_layer.team_dao.team_dao_interface import TeamDAOInterface
from entities.team_class_information import Team


class TeamDAOImp(TeamDAOInterface):

    teams_list = []
    id_generator = 2

    def __init__(self):
        team_needed_for_id_catch = Team(1, "Pistons", "Fort Wayne")
        self.teams_list.append(team_needed_for_id_catch)

    def create_team(self, team: Team)-> Team:
        # team needs to be given an Id, and it needs to be added to the list
        team.team_id = self.id_generator # this changes the team's Id to whatever the id generator is set to
        self.id_generator += 1 # this ensures that the next team will have a newly generated Id
        self.teams_list.append(team) # this adds the new team to my team database
        return team # this returns the team object with its newly generated Id

    def get_team_information_by_id(self, team_id: int)-> Team:
        for team in self.teams_list:
            if team.team_id == team_id:
                return team
        raise IdNotFound("No team matches the id given: please try again!")

    def update_team_by_id(self, team: Team)-> Team:
        for old_team in self.teams_list:
            if team.team_id == old_team.team_id:
                old_team = team
                return old_team
        raise IdNotFound("No team matches the id given: please try again!")

    def delete_team_by_id(self, team_id: int)-> bool:
        for team in self.teams_list:
            if team.team_id == team_id:
                self.teams_list.remove(team)
                return True
        raise IdNotFound("No team matches the id given: please try again!")
