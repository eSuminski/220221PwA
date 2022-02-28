"""This module contains team dao unit tests"""
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.team_dao.team_dao_imp import TeamDAOImp
from entities.team_class_information import Team

team_dao = TeamDAOImp()  # I will be using this team dao object for all my team dao unit tests

"""
create team tests
business logic:
    Teams may not have the same name ( this will be handled in the service layer )
    Teams may not be located in the same city ( this will be handled in the service layer )
    Teams may not have duplicate Ids (will handle this hear because it directly relates to the database)
"""


def test_create_team_success():
    test_team = Team(0, "Trail Blazers", "Portland")
    result = team_dao.create_team(test_team)
    assert result.team_id != 0


def test_catch_non_unique_id():
    test_team = Team(1, "Lakers", "L.A.")
    result = team_dao.create_team(test_team)
    assert result.team_id != 1


"""
get team tests
"""


def test_get_team_info_by_id_success():
    result = team_dao.get_team_information_by_id(1)
    assert result.team_id == 1


def test_get_team_using_non_existant_id():
    try:
        team_dao.get_team_information_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No team matches the id given: please try again!"


"""
update team tests
"""


def test_update_team_by_id_success():
    new_team_name = Team(1, "Batman", "Fort Wayne")
    result = team_dao.update_team_by_id(new_team_name)
    assert result.team_name == "Batman"


def test_update_team_using_non_existant_id():
    try:
        new_team_name = Team(0, "Batman", "Fort Wayne")
        team_dao.update_team_by_id(new_team_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No team matches the id given: please try again!"


"""
delete team tests
"""


def test_delete_team_by_id_success():
    result = team_dao.delete_team_by_id(1)
    assert result


def test_delete_team_with_non_existant_id():
    try:
        team_dao.delete_team_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No team matches the id given: please try again!"
