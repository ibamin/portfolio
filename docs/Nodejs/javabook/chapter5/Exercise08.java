package javabook.chapter5;

public class Exercise08 {
    public static void main(String[] args) {
        int [][]array={{95,86},{83,92,96},{78,83,93,87,88}};
        int sum=0,cnt=0;
        double avg=0;

        for(int i=0;i<array.length;i++)
        for(int data:array[i]){
        sum+=data;
        cnt++;
    }

        avg=(double)sum/cnt;

        System.out.println("sum : "+sum);
        System.out.println("avg : "+avg);
    }
}
