package javabook.chapter6;

public class koreaExample {
    public static void main(String[] args) {
        korea k1 = new korea("박자바","011225-1234567");
        System.out.println("k1.name : "+k1.name);
        System.out.println("k1.ssn : "+k1.ssn);

        korea k2 = new korea("김자바","930525-0654321");
        System.out.println("k2.name : "+k2.name);
        System.out.println("k2.ssn : "+k2.ssn);
    }
}
