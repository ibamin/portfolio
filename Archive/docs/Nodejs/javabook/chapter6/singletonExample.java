package javabook.chapter6;

public class singletonExample {
 public static void main(String[] args) {
    /*
     * singleton obj1 = new singleton(); //오류
     * singleton obj2 = new singleton(); //오류
     */

    singleton obj1 = singleton.getInstance();
    singleton obj2 = singleton.getInstance();

    if(obj1==obj2) System.out.println("같은 singleton 객체입니다");
    else System.out.println("다른 singleton 객체입니다");
 }   
}
