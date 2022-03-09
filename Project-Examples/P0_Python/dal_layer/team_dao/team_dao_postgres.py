from custom_exceptions.id_not_found import IdNotFound
from dal_layer.team_dao.team_dao_interface import TeamDAOInterface
from entities.team_class_information import Team
from util.postgres_connection import connection


class TeamDAOImpPostgres(TeamDAOInterface):

    def create_team(self, team: Team) -> Team:
        sql = "insert into teams values(default, %s, %s) returning team_id"
        cursor = connection.cursor()
        cursor.execute(sql, (team.team_name, team.home_city))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        team.team_id = generated_id
        return team

    def get_team_information_by_id(self, team_id: int) -> Team:
        sql = "select * from teams where team_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [team_id])
        team_record = cursor.fetchone()
        if team_record is None:
            raise IdNotFound("No team matches the id given: please try again!")
        team = Team(*team_record)
        return team

    def update_team_by_id(self, team: Team) -> Team:
        sql = "update teams set team_name = %s, home_city = %s where team_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (team.team_name, team.home_city, team.team_id))
        connection.commit()
        if cursor.rowcount != 0:
            return team
        else:
            raise IdNotFound("No team matches the id given: please try again!")

    def delete_team_by_id(self, team_id: int) -> bool:
        sql = "delete from teams where team_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [team_id])
        connection.commit()
        if cursor.rowcount != 0:
            return True
        else:
            raise IdNotFound("No team matches the id given: please try again!")