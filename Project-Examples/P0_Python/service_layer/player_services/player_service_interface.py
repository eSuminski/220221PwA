from abc import ABC, abstractmethod

from dal_layer.player_dao.player_dao_imp import PlayerDAOImp
from dal_layer.player_dao.player_dao_interface import PlayerDAOInterface
from entities.player_class_information import Player


class PlayerServiceInterface(ABC):

    def __init__(self, player_dao: PlayerDAOInterface):
        self.player_dao: PlayerDAOImp = player_dao

    @abstractmethod
    def service_create_player(self, player: Player) -> Player:
        pass

    @abstractmethod
    def service_get_player_information_by_id(self, player_id: int) -> Player:
        pass

    @abstractmethod
    def service_update_player_information(self, player: Player) -> Player:
        pass

    @abstractmethod
    def service_delete_player_by_id(self, player_id: int) -> bool:
        pass
