package javabook.chapter6;

public class personExample {
   public static void main(String[] args) {
    person p1 = new person("123456-1234567","계백");

    System.out.println(p1.nation);
    System.out.println(p1.ssn);
    System.out.println(p1.name);

    //p1.nation ="usa";
    //p1.ssn="654321-7654321";
    p1.name="을지문덕";
   }
}
