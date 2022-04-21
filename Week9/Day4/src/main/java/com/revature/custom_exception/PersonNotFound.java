package com.revature.custom_exception;

public class PersonNotFound extends RuntimeException{
    public PersonNotFound(String message) {
        super(message);
    }
}
