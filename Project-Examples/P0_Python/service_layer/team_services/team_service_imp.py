from custom_exceptions.bad_team_info import BadTeamInfo
from entities.team_class_information import Team
from service_layer.team_services.team_service_interface import TeamServiceInterface


class TeamServiceImp(TeamServiceInterface):

    def service_create_team(self, team: Team) -> Team:
        if type(team.team_name) != str:
            raise BadTeamInfo("Please pass in a valid team name")
        elif type(team.home_city) != str:
            raise BadTeamInfo("Please pass in a valid city name")
        for existing_team in self.team_dao.teams_list:
            if existing_team.team_id == team.team_id:
                raise BadTeamInfo("This team name already exists in the database")
            elif existing_team.home_city == team.home_city:
                raise BadTeamInfo("This city name already exists in the database")
        return self.team_dao.create_team(team)

    def service_get_team_information_by_id(self, team_id: int) -> Team:
        pass

    def service_update_team_by_id(self, team: Team) -> Team:
        pass

    def service_delete_team_by_id(self, team_id: int) -> bool:
        pass
