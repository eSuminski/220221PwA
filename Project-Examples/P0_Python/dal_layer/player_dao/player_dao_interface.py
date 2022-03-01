from abc import ABC, abstractmethod

from entities.player_class_information import Player


class PlayerDAOInterface(ABC):

    # Create
    @abstractmethod
    def create_player(self, player: Player) -> Player:
        pass

    # Read
    @abstractmethod
    def get_player_by_id(self, player_id: int) -> Player:
        pass

    # Update
    @abstractmethod
    def update_player_by_id(self, player: Player) -> Player:
        pass

    # Delete
    @abstractmethod
    def delete_player_by_id(self, player_id: int) -> bool:
        pass
