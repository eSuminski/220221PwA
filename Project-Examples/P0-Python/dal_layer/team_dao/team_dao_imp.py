from entities.team_class_information import Team
from team_dao_interface import TeamDAOInterface


class TeamDAOImp(TeamDAOInterface):
    def create_team(self, team: Team):
        pass

    def get_team_information_by_id(self, team_id: int):
        pass

    def update_team_by_id(self, team: Team):
        pass

    def delete_team_by_id(self, team_id: int):
        pass
