package javabook.chapter6;

public class calculatorExample {
    public static void main(String[] args) {
        calculator mycalcu=new calculator();

        double result = mycalcu.areaRectangle(10);
        double result2 = mycalcu.areaRectangele(10,20);

        System.out.println("정삭각형 넓이 = "+result);
        System.out.println("직사각형 넓이 = "+result2);
    }
}
