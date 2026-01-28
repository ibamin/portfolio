package javabook.chapter7.Example;

public class Parent {
    public String nation;

    public Parent(){
        this("¥Î«—πŒ±π");
        System.out.println("Parent() call");
    }

    public Parent(String string) {
        this.nation=string;
        System.out.println("Parent(String nation) call");
    }
}
