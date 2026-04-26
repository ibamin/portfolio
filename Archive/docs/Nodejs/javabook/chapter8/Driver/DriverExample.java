package javabook.chapter8.Driver;

public class DriverExample {
    public static void main(String[] args) {
        Driver driver =new Driver();

        Bus bus = new Bus();
        Taxi taxi = new Taxi();

        driver.dive(bus);
        driver.dive(taxi);
    }
}
