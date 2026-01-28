package javabook.chapter7.Example;

public class Child extends Parent{
    private String name;

    public Child(){
        this("ȫ�浿");
        System.out.println("Child() call");
    }

    public Child(String string) {
        this.name=string;
        System.out.println("Child(String name) call");
    }
}
