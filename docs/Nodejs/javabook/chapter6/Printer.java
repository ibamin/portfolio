package javabook.chapter6;

public class Printer {
    Printer printer = new Printer();

    static void println(int n){
        System.out.println(n);
    }
    static void println(boolean tf){
        System.out.println(tf);
    }
    static void println(double d){
        System.out.println(d);
    }
    static void println(String name){
        System.out.println(name);
    }
}
