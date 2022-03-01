from abc import ABC, abstractmethod

from entities.team_class_information import Team


class TeamServiceInterface(ABC):

    # create
    @abstractmethod
    def service_create_team(self, team: Team) -> Team:
        pass

    # read
    @abstractmethod
    def service_get_team_information_by_id(self, team_id: int) -> Team:
        pass

    # update
    @abstractmethod
    def service_update_team_by_id(self, team: Team) -> Team:
        pass

    # delete
    @abstractmethod
    def service_delete_team_by_id(self, team_id: int) -> bool:
        pass


