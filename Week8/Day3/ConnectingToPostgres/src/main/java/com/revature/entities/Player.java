package com.revature.entities;

import java.util.Objects;

// we are making this Player class a Java Bean Class
public class Player {
    // Java Bean classes have all their fields as private
    private int playerId;
    private String firstName;
    private String lastName;

    // Java Bean classes have two constructors: a no args, and one that sets all the fields
    public Player(){}

    public Player(int playerId, String firstName, String lastName){
        this.playerId = playerId;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    /*
    *  We need public getter and setter methods for the fields
    *  We need to override the equals, hashcode, and toString methods
    */

    public int getPlayerId() {
        return playerId;
    }

    public void setPlayerId(int playerId) {
        this.playerId = playerId;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Player player = (Player) o;
        return playerId == player.playerId && Objects.equals(firstName, player.firstName) && Objects.equals(lastName, player.lastName);
    }

    @Override
    public int hashCode() {
        return Objects.hash(playerId, firstName, lastName);
    }

    @Override
    public String toString() {
        return "Player{" +
                "playerId=" + playerId +
                ", firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                '}';
    }
}
