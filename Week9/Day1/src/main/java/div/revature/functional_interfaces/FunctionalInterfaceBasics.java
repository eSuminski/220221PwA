package div.revature.functional_interfaces;


@FunctionalInterface // make sure to add this annotation to your interface to make it a funcitonal one
public interface FunctionalInterfaceBasics {
    /*
        this one method can be reimplemented on the fly while you are coding. For this functional interface to work
        properly it must be the only property of the functional interface
     */
    int math(int numOne);
}
