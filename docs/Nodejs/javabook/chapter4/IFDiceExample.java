package javabook.chapter4;

public class IFDiceExample {
    public static void main(String[] args) {
        int num = (int)(Math.random()*6)+1;

        if(num==1){
            System.out.println("주사위의 눈은 : 1");
        }else if(num==2){
            System.out.println("주사위의 눈은 : 2");
        }else if(num==3){
            System.out.println("주사위의 눈은 : 3");
        }else if(num==4){
            System.out.println("주사위의 눈은 : 4");
        }else if(num==5){
            System.out.println("주사위의 눈은 : 5");
        }else if(num==6){
            System.out.println("주사위의 눈은 : 6");
        }
    }
}
