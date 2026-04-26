package javabook.chapter7.Example;

public class SnowTireExample {
    public static void main(String[] args) {
        snowTire snowTire=new snowTire();
        Tire tire =snowTire;

        snowTire.run();
        tire.run();
    }
}
