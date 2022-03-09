from abc import ABC, abstractmethod

from entities.team_class_information import Team

"""
This is the interface for the team data access object. Inside the class I will define the different CRUD operations
that we will need to interact with all team data inside of the database. These methods will be used by the service
layer to make the necessary changes to the database. Note that these methods don't HAVE to fulfill any User stories:
they are a tool used by your service layer to be able to fulfill the requirements of the user stories.
"""

class TeamDAOInterface(ABC):

    # create
    @abstractmethod
    def create_team(self, team: Team)-> Team: # passing in all the team data we need in this team parameter
        """this method will be used to handle adding new team data into my database"""
        pass

    # read
    @abstractmethod
    def get_team_information_by_id(self, team_id: int)-> Team:
        """this method will be used to handle retrieving new team data from my database"""
        pass

    @abstractmethod
    def get_all_teams_information(self):
        """will be used to perform data validation"""
        pass

    # update
    @abstractmethod
    def update_team_by_id(self, team: Team)-> Team:
        """this method will be used to handle updating team data inside my database"""
        pass

    # delete
    @abstractmethod
    def delete_team_by_id(self, team_id: int)-> bool:
        """this method will be used to remove team data from my database"""
        pass
