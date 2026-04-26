package javabook.chapter3;

public class Exercise04 {
    public static void main(String[] args) {
        int pencile=534;
        int students=30;

        int pencilesPerStudent=pencile/students;
        System.out.println(pencilesPerStudent);

        int pencilsLeft=pencile%students;
        System.out.println(pencilsLeft);
    }
}
