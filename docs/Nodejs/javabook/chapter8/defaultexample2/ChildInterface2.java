package javabook.chapter8.defaultexample2;

public interface ChildInterface2 extends ParentInterface{
    @Override
    default void method2() {
        // TODO Auto-generated method stub
        ParentInterface.super.method2();
    }

    public void method3();
}
