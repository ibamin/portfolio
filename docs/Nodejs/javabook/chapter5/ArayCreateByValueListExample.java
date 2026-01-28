package javabook.chapter5;

public class ArayCreateByValueListExample {
    public static void main(String[] args) {
        int []score={83,90,87};

        for(int i=0;i<3;i++) 
        System.out.println("Scores["+i+"] : "+score[i]);

        int sum=0;
        for(int i=0;i<3;i++)
        sum+=score[i];
        System.out.println("ÃÑÇÕ : "+sum);
        double avg = (double)sum/3;
        System.out.println("Æò±Õ : "+avg);
    }
}
