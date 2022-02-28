from abc import ABC, abstractmethod

from entities.team_class_information import Team


class TeamDAOInterface(ABC):

    # create
    @abstractmethod
    def create_team(self, team: Team): # passing in all the team data we need in this team parameter
        pass

    # read
    @abstractmethod
    def get_team_information_by_id(self, team_id: int):
        pass

    # update
    @abstractmethod
    def update_team_by_id(self, team: Team):
        pass

    # delete
    @abstractmethod
    def delete_team_by_id(self, team_id: int):
        pass
