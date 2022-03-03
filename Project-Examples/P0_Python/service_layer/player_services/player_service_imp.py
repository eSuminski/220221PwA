from custom_exceptions.bad_player_info import BadPlayerInfo
from entities.player_class_information import Player
from service_layer.player_services.player_service_interface import PlayerServiceInterface


class PlayerServiceImp(PlayerServiceInterface):

    def service_create_player(self, player: Player) -> Player:
        if len(player.first_name) > 20:
            raise BadPlayerInfo("First name is too long")
        elif len(player.last_name) > 20:
            raise BadPlayerInfo("Last name is too long")
        for p in self.player_dao.player_list:
            if p.team_id == player.team_id and p.jersey_number == player.jersey_number:
                raise BadPlayerInfo("Jersey number already taken")
        return self.player_dao.create_player(player)

    def service_get_player_information_by_id(self, player_id: int) -> Player:
        if type(player_id) == int:
            return self.player_dao.get_player_by_id(player_id)
        else:
            raise BadPlayerInfo("Please provide a valid Id")

    def service_update_player_information(self, player: Player) -> Player:
        if len(player.first_name) > 20:
            raise BadPlayerInfo("First name is too long")
        elif len(player.last_name) > 20:
            raise BadPlayerInfo("Last name is too long")
        for p in self.player_dao.player_list:
            if p.team_id == player.team_id and p.jersey_number == player.jersey_number:
                raise BadPlayerInfo("Jersey number already taken")
        return self.player_dao.update_player_by_id(player)

    def service_delete_player_by_id(self, player_id: int) -> bool:
        if type(player_id) == int:
            return self.player_dao.delete_player_by_id(player_id)
        else:
            raise BadPlayerInfo("Please provide a valid Id")
