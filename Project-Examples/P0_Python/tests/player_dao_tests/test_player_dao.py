from custom_exceptions.id_not_found import IdNotFound
from dal_layer.player_dao.player_dao_imp import PlayerDAOImp
from entities.player_class_information import Player

player_dao = PlayerDAOImp()

"""
create player tests
business logic:
    Players may not have the same Id ( this will be handled in the service layer )
    Players may not have the same jersey number on the same team ( this will be handled in the service layer )
"""

"""
The tests in this module were crafted to check two things:

1. when the correct data is provided to the method, the method returns the expected return value

2. when the data you want to work with does not exist, a message indicating it does not exist should be returned
"""


def test_create_player_success():
    test_player = Player(0,1,"New","Player",10)
    result = player_dao.create_player(test_player)
    assert result.player_id != 0


def test_catch_non_unique_id():
    """because my database handles the ID, I need to check that providing an ID does not ruin the method"""
    test_player = Player(1,1,"Bad","Id",0)
    result = player_dao.create_player(test_player)
    assert result.player_id != 1


"""
get player tests
"""


def test_get_player_info_by_id_success():
    result = player_dao.get_player_by_id(1)
    assert result.player_id == 1


def test_get_team_using_non_existant_id():
    try:
        player_dao.get_player_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No player matches the id given: please try again!"


"""
update player tests
"""


def test_update_team_by_id_success():
    new_player_name = Player(1,1, "Batman", "Fort Wayne", 50)
    result = player_dao.update_player_by_id(new_player_name)
    assert result.first_name == "Batman"


def test_update_team_using_non_existant_id():
    try:
        new_player_name = Player(0,1, "Batman", "Fort Wayne",50)
        player_dao.update_player_by_id(new_player_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No player matches the id given: please try again!"


"""
delete team tests
"""


def test_delete_team_by_id_success():
    result = player_dao.delete_player_by_id(1)
    assert result


def test_delete_team_with_non_existant_id():
    try:
        player_dao.delete_player_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No player matches the id given: please try again!"

