package javabook.chapter3;

public class StringEqualsExample {
    public static void main(String[] args) {
        String strvar1 ="Ω≈πŒ√∂";
        String strvar2 = "Ω≈πŒ√∂";
        String strvar3 = new String("Ω≈πŒ√∂");

        System.out.println(strvar1==strvar2);
        System.out.println(strvar1==strvar3);
        System.out.println();
        System.out.println(strvar1.equals(strvar2));
        System.out.println(strvar1.equals(strvar3));
    }
}
