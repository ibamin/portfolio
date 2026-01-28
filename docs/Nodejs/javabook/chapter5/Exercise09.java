package javabook.chapter5;
import java.util.Scanner;

public class Exercise09 {
    public static void main(String[] args) {
        boolean run=true;
        int studentNum=0;
        int [] scores=null;
        Scanner scanner = new Scanner(System.in);

        while(run){
            System.out.println("----------------------");
            System.out.println("1.학생수 | 2.점수입력 | 3.점수리스트 | 4.분석 | 5.종료");
            System.out.println("----------------------");
            System.out.println("선택>");

            int selectNo = scanner.nextInt();

            if(selectNo==1){
                System.out.println("학생 수를 입력해주세요.");
                System.out.print(">>");
                studentNum = scanner.nextInt();
                scores = new int[studentNum];
                System.out.println(studentNum+"명 입실");
            }
            else if(selectNo==2){
                int n;
                for(int i=0;i<studentNum;i++){
                    System.out.println((i+1)+"번쨰 학생의 점수");
                    System.out.print(">>");
                    n=scanner.nextInt();
                    scores[i] = n;
                }
            }
            else if(selectNo==3){
                int cnt=0;
                for(int n:scores){
                    System.out.println(cnt+"번째 학생의 점수 : "+n);
                }
            }
            else if(selectNo==4){
                int max=0,sum=0,cnt=0;
                double avg=0;
                for(int n:scores){
                    if(max<n) max=n;
                    sum+=n;
                    cnt++;
                 }
                avg = (double)sum/cnt;
                System.out.println("합은 : "+sum);
                System.out.println("평균 : "+avg);
            }
            else if(selectNo==5){
                run=false;
            }
        }
        scanner.close();
    }
}
