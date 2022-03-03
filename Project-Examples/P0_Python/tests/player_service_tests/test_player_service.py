from custom_exceptions.bad_player_info import BadPlayerInfo
from dal_layer.player_dao.player_dao_imp import PlayerDAOImp
from entities.player_class_information import Player
from service_layer.player_services.player_service_imp import PlayerServiceImp

player_dao = PlayerDAOImp()
player_service = PlayerServiceImp(player_dao)

"""
Note: this is not an exhaustive lists of tests: just some examples of different types of tests you could write
"""


def test_catch_first_name_too_long_create():
    player = Player(0, 1, "This is too long of a first name", "this is fine", 1000)
    try:
        player_service.service_create_player(player)
        assert False
    except BadPlayerInfo as e:
        assert str(e) == "First name is too long"


def test_catch_last_name_too_long_create():
    player = Player(0, 1, "this is fine", "This is too long of a last name", 1000)
    try:
        player_service.service_create_player(player)
        assert False
    except BadPlayerInfo as e:
        assert str(e) == "Last name is too long"


def test_catch_jersey_number_already_taken_on_team_create():
    player = Player(0, 1, "this is fine", "this is fine", 22)
    try:
        player_service.service_create_player(player)
        assert False
    except BadPlayerInfo as e:
        assert str(e) == "Jersey number already taken"


def test_non_int_provided_for_id_get_player():
    try:
        player_service.service_get_player_information_by_id("1")
    except BadPlayerInfo as e:
        assert str(e) == "Please provide a valid Id"


def test_catch_first_name_too_long_update():
    player = Player(1, 1, "This is too long of a first name", "this is fine", 1000)
    try:
        player_service.service_update_player_information(player)
        assert False
    except BadPlayerInfo as e:
        assert str(e) == "First name is too long"


def test_catch_last_name_too_long_update():
    player = Player(0, 1, "this is fine", "This is too long of a last name", 1000)
    try:
        player_service.service_update_player_information(player)
        assert False
    except BadPlayerInfo as e:
        assert str(e) == "Last name is too long"


def test_catch_jersey_number_already_taken_on_team_update():
    player = Player(0, 1, "this is fine", "this is fine", 22)
    try:
        player_service.service_update_player_information(player)
        assert False
    except BadPlayerInfo as e:
        assert str(e) == "Jersey number already taken"


def test_non_int_provided_for_id_delete():
    try:
        player_service.service_delete_player_by_id("1")
    except BadPlayerInfo as e:
        assert str(e) == "Please provide a valid Id"
