package com.revature.players;

import com.revature.daos.PlayerDAOImp;
import com.revature.entities.Player;
import org.testng.annotations.Test;
import org.testng.Assert;

import java.util.List;

public class PlayersTests {

    PlayerDAOImp playerDAO = new PlayerDAOImp();

    @Test
    public void createPlayerSuccess(){
        Player newPlayer = new Player(0,"Eric","Suminski");
        Player resultingPlayer = playerDAO.createPlayer(newPlayer);
        Assert.assertNotEquals(resultingPlayer.getPlayerId(),0);
    }

    @Test
    public void selectPlayerByIdSuccess(){
        Player player = playerDAO.selectPlayerById(-1);
        Assert.assertEquals(player.getPlayerId(),-1);
    }

    @Test
    public void selectAllPlayersSuccess(){
        List<Player> players = playerDAO.selectAllPlayers();
        Assert.assertTrue(players.size() >= 1);
    }

    @Test
    public void updatePlayerSuccess(){
        Player player = new Player(-2,"Brandon","names");
        int result = playerDAO.updatePlayerById(player);
        Assert.assertTrue(result != 0);
    }

    @Test
    public void deletePlayerSuccess(){
        int result = playerDAO.deletePlayerById(-3);
        Assert.assertTrue(result != 0);
    }

}
