package javabook.chapter3;

public class LogincalOperatorExample {
    public static void main(String[] args) {
        int charcode ='A';

        if((charcode>=65)&&(charcode<=90)){
            System.out.println("대문자 이군요");
        }
        if((charcode>=97)&&(charcode<=122)){
            System.out.println("소문자 이군요");
        }
        if((charcode<48)&&(charcode>57)){
            System.out.println("0~9숫자 이군요");
        }
        
        int value=6;

        if((value%2==0)|(value%3==0)){
            System.out.println("2 또는 3의 배수 이군요");
        }
        if((value%2==0)||(value%3==0)){
            System.out.println("2 또는 3의 배수 이군요");
        }
    }
}
