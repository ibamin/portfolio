package javabook.chapter9.ex5;

public class Anonymous {
    Vehicle field = new Vehicle() {
        @Override
        public void run() {
            System.out.println("Anonymous field");
        }
    };

    void method1(){
        Vehicle localVar = new Vehicle() {
            @Override
            public void run(){
                System.out.println("Anonymous method1()");
            }
        };
    }

    void method2(Vehicle v){
        v.run();
    }
}
