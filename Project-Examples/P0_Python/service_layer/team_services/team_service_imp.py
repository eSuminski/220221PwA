from custom_exceptions.bad_team_info import BadTeamInfo
from dal_layer.team_dao.team_dao_interface import TeamDAOInterface
from entities.team_class_information import Team
from service_layer.team_services.team_service_interface import TeamServiceInterface


class TeamServiceImp(TeamServiceInterface):

    def __init__(self, team_dao: TeamDAOInterface):
        self.team_dao = team_dao

    def service_create_team(self, team: Team) -> Team:
        if type(team.team_name) != str:  # this is checking that the team name is a string
            raise BadTeamInfo("Please pass in a valid team name")  # raise exception if we are not working with a string
        elif type(team.home_city) != str:  # this is checking that the home city is a string
            raise BadTeamInfo("Please pass in a valid city name")  # raise exception if we are not working with a string
        for existing_team in self.team_dao.teams_list:  # here we need to loop through existing teams to validate business rules
            if existing_team.team_name == team.team_name:  # here we are checking for duplicate team names
                raise BadTeamInfo(
                    "This team name already exists in the database")  # raise exception for duplicate team names
            elif existing_team.home_city == team.home_city:  # here we are checking for duplicate city names
                raise BadTeamInfo(
                    "This city name already exists in the database")  # raise exception if their are duplicates
        return self.team_dao.create_team(team)  # assuming all validation checked out, we pass data into DAL

    def service_get_team_information_by_id(self, team_id: int) -> Team:
        if type(team_id) == int:
            return self.team_dao.get_team_information_by_id(team_id)
        else:
            raise BadTeamInfo("Please provide a valid team Id")

    def service_update_team_by_id(self, team: Team) -> Team:
        if type(team.team_name) != str:  # this is checking that the team name is a string
            raise BadTeamInfo("Please pass in a valid team name")  # raise exception if we are not working with a string
        elif type(team.home_city) != str:  # this is checking that the home city is a string
            raise BadTeamInfo("Please pass in a valid city name")  # raise exception if we are not working with a string
        for existing_team in self.team_dao.teams_list:  # here we need to loop through existing teams to validate business rules
            if existing_team.team_name == team.team_name:  # here we are checking for duplicate team names
                raise BadTeamInfo("This team name already exists in the database")  # raise exception for duplicate team names
            elif existing_team.home_city == team.home_city:  # here we are checking for duplicate city names
                raise BadTeamInfo("This city name already exists in the database")  # raise exception if their are duplicates
        return self.team_dao.update_team_by_id(team)  # assuming all validation checked out, we pass data into DAL

    def service_delete_team_by_id(self, team_id: int) -> bool:
        if type(team_id) == int:
            return self.team_dao.delete_team_by_id(team_id)
        else:
            raise BadTeamInfo("Please provide a valid team Id")
