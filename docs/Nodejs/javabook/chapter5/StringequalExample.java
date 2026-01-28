package javabook.chapter5;

public class StringequalExample {
    public static void main(String[] args) {
        String strver1="신민철";
        String strver2="신민철";

        if(strver1==strver2){
            System.out.println("strver1과 strver2가 같은 객체를 참조");
        }else{
            System.out.println("strver1과 strver2가 다른 객체를 참조");
        }
        
        if(strver1.equals(strver2)){
            System.out.println("strver1과 strver2는 문자열이 같음" + strver1 + " " +strver2);
        }

        String strver3 = new String("신민철");
        String strver4= new String ("신민철");

        if(strver3==strver4){
            System.out.println("strver3과 strver4가 같은 객체를 참조");
        }else{
            System.out.println("strver3과 strver4가 다른 객체를 참조");
        }

        if(strver3.equals(strver4)){
            System.out.println("strver3과 strver4는 문자열이 같음");
        }
    }
}
