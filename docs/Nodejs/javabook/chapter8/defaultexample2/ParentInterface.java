package javabook.chapter8.defaultexample2;

public interface ParentInterface {
    public void method1();
    public default void method2(){
        System.out.println("ParentInterface");
    }
}
