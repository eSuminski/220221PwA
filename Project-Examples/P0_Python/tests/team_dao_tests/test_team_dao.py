"""This module contains team dao unit tests"""
from unittest.mock import MagicMock, patch

from custom_exceptions.bad_team_info import BadTeamInfo
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.team_dao.team_dao_postgres import TeamDAOImpPostgres
from entities.team_class_information import Team

team_dao = TeamDAOImpPostgres()  # I will be using this team dao object for all my team dao unit tests

"""
create team tests
business logic:
    Teams may not have the same name ( this will be handled in the service layer )
    Teams may not be located in the same city ( this will be handled in the service layer )
    Teams may not have duplicate Ids (will handle this here because it directly relates to the database)
"""

"""
The tests in this module were crafted to check two things:

1. when the correct data is provided to the method, the method returns the expected return value

2. when the data you want to work with does not exist, a message indicating it does not exist should be returned
"""


def test_create_team_success():
    test_team = Team(0, "Trail Blazers", "Portland")
    result = team_dao.create_team(test_team)
    print(result.team_id)
    assert result.team_id != 0


def test_catch_non_unique_id():
    """because my database handles the ID, I need to check that providing an ID does not ruin the method"""
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


def test_get_all_teams_success():
    result = team_dao.get_all_teams_information()
    assert len(result) >= 1


@patch("dal_layer.team_dao.team_dao_postgres.TeamDAOImpPostgres.get_all_teams_information")
def test_no_teams_found(mock):
    """this is not actually testing my method, just raising an exception and catching it in the except block"""
    try:
        mock.side_effect = BadTeamInfo("No teams were found")
        team_dao.get_all_teams_information()
        assert False
    except BadTeamInfo as e:
        assert str(e) == "No teams were found"
