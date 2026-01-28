package javabook.chapter4;
import java.util.Scanner;

public class Exercise07 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int s,n,money=0;

        off:while(true){
            System.out.println("----------------");
            System.out.println("1.예금 | 2.출금 | 3.잔고 | 4.종료");
            System.out.println("----------------");
            System.out.print("선택>");

            s=scanner.nextInt();
            switch(s){
                case 1:
                System.out.print("예금액>");
                n=scanner.nextInt();
                money+=n;
                break;
                case 2:
                System.out.print("출금액>");
                n=scanner.nextInt();
                money-=n;
                break;
                case 3:
                System.out.println("잔고>"+money);
                break;
                default:
                System.out.println("프로그램 종료");
                break off;
            }
            scanner.close();
        }
    }
}
