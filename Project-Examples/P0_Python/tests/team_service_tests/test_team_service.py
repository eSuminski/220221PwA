from custom_exceptions.bad_team_info import BadTeamInfo
from dal_layer.team_dao.team_dao_imp import TeamDAOImp
from entities.team_class_information import Team
from service_layer.team_services.team_service_imp import TeamServiceImp

"""
Because I need to work with so many different teams that have some kind of bad data I have decided to pre-make these
objects in my code. This way I can call the specific object that I need for my test when necessary
"""

team_dao = TeamDAOImp()
team_service = TeamServiceImp(team_dao)
duplicate_team_name = Team(0, "Pistons", "city name is fine")
duplicate_city_name = Team(0, "name is fine", "Fort Wayne")
non_string_team_name = Team(0, 10.7, "city name is fine")
non_string_city_name = Team(0, "name is fine", True)
duplicate_team_name_update = Team(1, "Pistons", "city name is fine")
duplicate_city_name_update = Team(1, "name is fine", "Fort Wayne")
non_string_team_name_update = Team(1, 10.7, "city name is fine")
non_string_city_name_update = Team(1, "name is fine", True)

"""
create team tests
business logic:
    Teams may not have the same name
    Teams may not be located in the same city
    Teams may not have duplicate Ids (this is handled in the DAL)
"""

"""
In these tests I am trying to think of the different ways that my team data needs to be verified, and for each way
I am writing a test to ensure that my methods, when implemented, will actually perform the necessary validation on 
the data. In particular, these tests are making sure that my Business Rules are being followed, and that the correct
data types are being used for each part of the team data.
"""


def test_check_no_duplicate_names_create_team():
    try:
        team_service.service_create_team(duplicate_team_name)
        assert False
    except BadTeamInfo as e:
        assert str(e) == "This team name already exists in the database"


def test_check_no_duplicate_cities_create_team():
    try:
        team_service.service_create_team(duplicate_city_name)
        assert False
    except BadTeamInfo as e:
        assert str(e) == "This city name already exists in the database"


def test_catch_non_string_city_create_team():
    try:
        team_service.service_create_team(non_string_team_name)
        assert False
    except BadTeamInfo as e:
        assert str(e) == "Please pass in a valid team name"


def test_catch_non_string_team_name_create_team():
    try:
        team_service.service_create_team(non_string_team_name)
        assert False
    except BadTeamInfo as e:
        assert str(e) == "Please pass in a valid team name"


"""
select team test
"""


def test_catch_non_numeric_id():
    try:
        team_service.service_get_team_information_by_id("one")
        assert False
    except BadTeamInfo as e:
        assert str(e) == "Please provide a valid team Id"


"""
update team tests
"""


def test_check_no_duplicate_names_update_team():
    try:
        team_service.service_update_team_by_id(duplicate_team_name_update)
        assert False
    except BadTeamInfo as e:
        assert str(e) == "This team name already exists in the database"


def test_check_no_duplicate_cities_update_team():
    try:
        team_service.service_update_team_by_id(duplicate_city_name_update)
        assert False
    except BadTeamInfo as e:
        assert str(e) == "This city name already exists in the database"


def test_catch_non_string_city_update_team():
    try:
        team_service.service_update_team_by_id(non_string_city_name_update)
        assert False
    except BadTeamInfo as e:
        assert str(e) == "Please pass in a valid city name"


def test_catch_non_string_team_name_update_team():
    try:
        team_service.service_update_team_by_id(non_string_team_name_update)
        assert False
    except BadTeamInfo as e:
        assert str(e) == "Please pass in a valid team name"


"""
delete team test
"""


def test_catch_non_numeric_id_delete_team():
    try:
        team_service.service_delete_team_by_id("one")
        assert False
    except BadTeamInfo as e:
        assert str(e) == "Please provide a valid team Id"
