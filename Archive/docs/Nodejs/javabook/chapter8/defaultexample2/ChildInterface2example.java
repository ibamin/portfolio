package javabook.chapter8.defaultexample2;

public class ChildInterface2example {
    public static void main(String[] args) {
        ChildInterface2 ci2 = new ChildInterface2() {
            @Override
            public void method1(){
                System.out.println("method1");
            }
            @Override
            public void method3(){
                System.out.println("method2");
            }
        };

        ci2.method1();
        ci2.method2();
        ci2.method3();
    }
}
