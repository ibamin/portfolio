package javabook.chapter8.Tire;

public class CarExample {
    public static void main(String[] args) {
        Car myCar = new Car();

        myCar.run();

        myCar.tires[0] = new kumhoTire();
        myCar.tires[1] = new kumhoTire();

        myCar.run();
    }
}
