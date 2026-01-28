package javabook.chapter9.ex;

public class Main {
    public static void main(String[] args) {
        A a = new A();

        A.B b= a.new B();
        b.field1=3;
        b.method1();

        A.c c = new A.c();
        c.field1=3;
        c.method1();
        A.c.field2=3;
        A.c.method2();

        a.method();
    }
}
