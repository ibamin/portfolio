package javabook.chapter6;

public class shopserviceExample {
    public static void main(String[] args) {
        shopservice obj1 = shopservice.getInstance();
        shopservice obj2 = shopservice.getInstance();

        if(obj1==obj2) System.out.println("같은 shopservice 객체 입니다");
        else System.out.println("다른 shopservice 객체 입니다.");
    }
}
