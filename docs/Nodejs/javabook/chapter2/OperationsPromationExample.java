package javabook.chapter2;

public class OperationsPromationExample {
    public static void main(String[] args) {
        byte bytevalue1=10;
        byte bytevalue2=20;
        //byte bytevalue3=bytevalue1+bytevalue2; 컴파일 에러
        int intvalue1 = bytevalue1+bytevalue2;
        System.out.println(intvalue1);

        char charvalue1='A';
        char charvalue2=1;
        //char charvalue3 = charvalue1+charvalue2 컴파일 에러
        int intvalue2=charvalue1+charvalue2;
        System.out.println("유니코드="+ intvalue2);
        System.out.println("출력문자="+(char)intvalue2);

        int intvalue3=10;
        int intvalue4=intvalue3/4;
        System.out.println(intvalue4);

        int intvalue5=10;
        //int intvalue6=10/4.0; 컴파일 에러
        double doublevalue =intvalue5/4.0;
        System.out.println(doublevalue);
    }
}
