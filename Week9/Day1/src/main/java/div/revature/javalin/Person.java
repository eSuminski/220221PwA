package div.revature.javalin;

/*
    this basc entity is used for our javalin example routes
 */

import java.util.Objects;

public class Person {
    private int personId;
    private String firstname;
    private String lastName;

    public Person(){}

    public Person(int personId, String firstname, String lastName) {
        this.personId = personId;
        this.firstname = firstname;
        this.lastName = lastName;
    }

    public int getPersonId() {
        return personId;
    }

    public void setPersonId(int personId) {
        this.personId = personId;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
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
        Person person = (Person) o;
        return personId == person.personId && firstname.equals(person.firstname) && lastName.equals(person.lastName);
    }

    @Override
    public int hashCode() {
        return Objects.hash(personId, firstname, lastName);
    }

    @Override
    public String toString() {
        return "Person{" +
                "personId=" + personId +
                ", firstname='" + firstname + '\'' +
                ", lastName='" + lastName + '\'' +
                '}';
    }
}
