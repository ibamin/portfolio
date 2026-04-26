package javabook.chapter3;

public class AccuracyExample {
    public static void main(String[] args) {
        int apple=1;
        double pieceUnit=apple*10;
        int number=7;

        double result=(pieceUnit-number)/10.0;

        System.out.println("사과 한개에서 ");
        System.out.println("0.7 조각을 빼면 ");
        System.out.println(result+"조각이 남는다.");
    }
}
