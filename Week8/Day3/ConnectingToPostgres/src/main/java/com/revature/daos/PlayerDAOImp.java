package com.revature.daos;

import com.revature.entities.Player;
import com.revature.utils.DatabaseConnection;

import javax.xml.transform.Result;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class PlayerDAOImp implements PlayerDAO{

    @Override
    public Player createPlayer(Player player) {
        try(Connection connection = DatabaseConnection.createConnection()){
            // make our sql statement
            String sql = "insert into players values(default, ?, ?)";
            // create a prepared statement object
            PreparedStatement ps = connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
            // use ps object to execute our query and pass in necessary paramenters
            ps.setString(1, player.getFirstName());
            ps.setString(2, player.getLastName());
            ps.execute();
            // create a result set from our query
            ResultSet rs = ps.getGeneratedKeys();
            // retrieve info from rs
            rs.next();
            player.setPlayerId(rs.getInt("player_id"));
            // return updated player object
            return player;
        } catch(SQLException e){
            e.printStackTrace();
            return null;
        }
    }

    @Override
    public Player selectPlayerById(int id) {
        try(Connection connection = DatabaseConnection.createConnection()){
            String sql = "select * from players where player_id = ?";
            PreparedStatement ps = connection.prepareStatement(sql);
            ps.setInt(1,id);
            ResultSet rs = ps.executeQuery(); // executeQuery returns a result set object with the results
            rs.next();
            Player player = new Player(
                    rs.getInt("player_id"),
                    rs.getString("first_name"),
                    rs.getString("last_name")
            );
            return player;
        } catch(SQLException e){
            e.printStackTrace();
            return null;
        }
    }

    @Override
    public List<Player> selectAllPlayers() {
        try(Connection connection = DatabaseConnection.createConnection()){
            String sql = "select * from players";
            // can create a statement, not prepared statement, if there are no parameters to add
            Statement s = connection.createStatement();
            s.execute(sql);
            ResultSet rs = s.getResultSet();
            List<Player> players = new ArrayList<>();
            while(rs.next()){
                Player player = new Player(
                        rs.getInt("player_id"),
                        rs.getString("first_name"),
                        rs.getString("last_name")
                );
                players.add(player);
            }
            return players;
        } catch(SQLException e){
            e.printStackTrace();
            return null;
        }
    }

    @Override
    public int updatePlayerById(Player player) {
        try(Connection connection = DatabaseConnection.createConnection()){
            String sql = "update players set first_name = ?, last_name = ? where player_id = ?";
            PreparedStatement ps = connection.prepareStatement(sql);
            ps.setString(1, player.getFirstName());
            ps.setString(2, player.getLastName());
            ps.setInt(3, player.getPlayerId());
            return ps.executeUpdate();
        } catch(SQLException e){
            e.printStackTrace();
            return 0;
        }
    }

    @Override
    public int deletePlayerById(int id) {
        try(Connection connection = DatabaseConnection.createConnection()){
            String sql = "delete from players where player_id = ?";
            PreparedStatement ps = connection.prepareStatement(sql);
            ps.setInt(1,id);
            return ps.executeUpdate();
        } catch(SQLException e){
            e.printStackTrace();
            return 0;
        }
    }
}
