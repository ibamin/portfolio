package javabook.chapter7;

public class SupersonicAirplaneExample {
    public static void main(String[] args) {
        SupersonicAirplan sa =new SupersonicAirplan();
        sa.takeoff();
        sa.fly();
        sa.flyMode=SupersonicAirplan.SUPERSONIC;
        sa.fly();
        sa.flyMode = SupersonicAirplan.NORMAL;
        sa.fly();
        sa.land();
    }
}
