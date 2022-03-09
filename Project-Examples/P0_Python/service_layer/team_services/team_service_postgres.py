from psycopg import OperationalError

from custom_exceptions.bad_team_info import BadTeamInfo
from dal_layer.team_dao.team_dao_postgres import TeamDAOImpPostgres
from entities.team_class_information import Team
from service_layer.team_services.team_service_interface import TeamServiceInterface


class TeamServiceImpPostgres(TeamServiceInterface):

    def __init__(self, team_dao):
        self.team_dao: TeamDAOImpPostgres = team_dao

    def service_create_team(self, team: Team) -> Team:
        if type(team.team_name) != str:
            raise BadTeamInfo("Please pass in a valid team name")
        elif type(team.home_city) != str:  # this is checking that the home city is a string
            raise BadTeamInfo("Please pass in a valid city name")  # raise exception if we are not working with a string
        teams = self.team_dao.get_all_teams_information()
        if len(teams) >= 1:
            for existing_team in teams:  # here we need to loop through existing teams to validate business rules
                if existing_team.team_name == team.team_name:  # here we are checking for duplicate team names
                    raise BadTeamInfo(
                        "This team name already exists in the database")  # raise exception for duplicate team names
                elif existing_team.home_city == team.home_city:  # here we are checking for duplicate city names
                    raise BadTeamInfo(
                        "This city name already exists in the database")  # raise exception if their are duplicates
            return self.team_dao.create_team(team)  # assuming all validation checked out, we pass data into DAL
        else:
            return self.team_dao.create_team(team)

    def service_get_team_information_by_id(self, team_id: str) -> Team:
        try:
            id_as_int = int(team_id)
            return self.team_dao.get_team_information_by_id(id_as_int)
            # return self.team_dao.get_team_information_by_id(int(team_id))
        except ValueError:
            raise BadTeamInfo("Please provide a valid team Id")

    def service_update_team_by_id(self, team: Team) -> Team:
        if type(team.team_name) != str:
            raise BadTeamInfo("Please pass in a valid team name")
        elif type(team.home_city) != str:  # this is checking that the home city is a string
            raise BadTeamInfo("Please pass in a valid city name")  # raise exception if we are not working with a string
        teams = self.team_dao.get_all_teams_information()
        if len(teams) >= 1:
            for existing_team in teams:  # here we need to loop through existing teams to validate business rules
                if existing_team.team_id != team.team_id:
                    if existing_team.team_name == team.team_name:  # here we are checking for duplicate team names
                        raise BadTeamInfo(
                            "This team name already exists in the database")  # raise exception for duplicate team names
                    elif existing_team.home_city == team.home_city:  # here we are checking for duplicate city names
                        raise BadTeamInfo(
                            "This city name already exists in the database")  # raise exception if their are duplicates
                return self.team_dao.update_team_by_id(team)  # assuming all validation checked out, we pass data into DAL
        else:
            raise BadTeamInfo("There are no teams to update!")

    def service_delete_team_by_id(self, team_id: int) -> bool:
        try:
            return self.team_dao.delete_team_by_id(int(team_id))
        except ValueError:
            raise BadTeamInfo("Please provide a valid team Id")