from custom_exceptions.id_not_found import IdNotFound
from dal_layer.player_dao.player_dao_interface import PlayerDAOInterface
from entities.player_class_information import Player


class PlayerDAOImp(PlayerDAOInterface):
    player_list = [Player(1, 1, "The", "joker", 22)]
    id_generator = 2

    # Create
    def create_player(self, player: Player) -> Player:
        player.player_id = self.id_generator
        self.id_generator += 1
        self.player_list.append(player)
        return player

    # Read
    def get_player_by_id(self, player_id: int) -> Player:
        for player in self.player_list:
            if player.player_id == player_id:
                return player
        raise IdNotFound("No player matches the id given: please try again!")

    # Update
    def update_player_by_id(self, player: Player) -> Player:
        for old_player in self.player_list:
            if old_player.player_id == player.player_id:
                old_player = player
                return old_player
        raise IdNotFound("No player matches the id given: please try again!")

    # Delete
    def delete_player_by_id(self, player_id: int) -> bool:
        for player in self.player_list:
            if player.player_id == player_id:
                self.player_list.remove(player)
                return True
        raise IdNotFound("No player matches the id given: please try again!")