package com.revature.daos;

import com.revature.entities.Player;

import java.util.List;

public interface PlayerDAO {
    // all interface fields are, by default, public static final
    // public: can access it anywhere
    // static: belongs to the class scope
    // final: the field is immutable
    String interfaceField = "this is my interface string";

    // interface methods are, by default, public abstract
    // public: the method can be accessed anywhere
    // abstract: the behavior of the method is not defined until it is inherited

    // create player
    // a Player object is the return type, createPlayer is the method name, player is a Player object that we will provide as an argument
    Player createPlayer(Player player);

    // select player/s
    Player selectPlayerById(int id);

    // here we declare that we are expecting back an object that implements the List interface that holds Player objects
    List<Player> selectAllPlayers();

    // update player
    int updatePlayerById(Player player);

    // delete player
    int deletePlayerById(int id);
}
