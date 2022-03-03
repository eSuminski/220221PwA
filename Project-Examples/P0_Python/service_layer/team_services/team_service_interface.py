from abc import ABC, abstractmethod

from entities.team_class_information import Team

"""
This is the interface for the team service object. Inside the class I will define the different User Story operations
that we will need to implement. These methods will need to check and validate the data that is being passed into them
to ensure that all Business Rules and programming logic is being followed. If any Business Rules or programming logic
are not validated, the data must NOT be passed into the data access layer, and instead some sort of error message must
be returned
"""

class TeamServiceInterface(ABC):

    # create
    @abstractmethod
    def service_create_team(self, team: Team) -> Team:
        """This method will validate the team information is correct before passing it to the DAL"""
        pass

    # read
    @abstractmethod
    def service_get_team_information_by_id(self, team_id: str) -> Team:
        """This method will validate a correct identifier is being used before passing it to the DAL"""
        pass

    # update
    @abstractmethod
    def service_update_team_by_id(self, team: Team) -> Team:
        """This method will validate the team information is correct before passing it to the DAL"""
        pass

    # delete
    @abstractmethod
    def service_delete_team_by_id(self, team_id: int) -> bool:
        """This method will validate a correct identifier is being used before passing it to the DAL"""
        pass


