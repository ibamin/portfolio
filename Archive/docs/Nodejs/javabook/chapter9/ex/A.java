package javabook.chapter9.ex;

import javabook.chapter7.dog;

public class A {
    A() { System.out.println("A 按眉啊 积己凳");}

    class B{
        B() { System.out.println("B 按眉啊 积己凳");}
        int field1;
        void method1() {}
    }

    static class c{
        c() {System.out.println("c 按眉啊 积己凳");}
        int field1;
        static int field2;
        void method1() {}
        static void method2() {}
    }

    void method(){
        class D{
            D(){System.out.println("D 按眉啊 积己凳");}
            int field1;
            void method1() {}
        }
        D d = new D();
        d.field1=3;
        d.method1();
    }
}
