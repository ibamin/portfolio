package javabook.chapter5;

public class ArrayInArrayExample {
    public static void main(String[] args) {
        int [][]mathScores = new int[2][3];
        for(int i=0;i<mathScores.length;i++){
            for(int j=0;j<mathScores.length;j++){
                System.out.println("mathScores["+i+"]["+j+"] = "+mathScores[i][j]);
            }
        }

        int [][]englishScores = new int[2][];
        englishScores[0]=new int[2];
        englishScores[1]=new int[3];
        for(int i=0;i<englishScores.length;i++){
            for(int j=0;j<englishScores[i].length;j++){
                System.out.println("englishScores["+i+"]["+j+"] = "+englishScores[i][j]);
            }
        }

        int [][]javascore = {{95,80},{92,96,80}};
        for(int i=0;i<javascore.length;i++){
            for(int j=0;j<javascore[i].length;j++){
                System.out.println("javaScores["+i+"]["+j+"] = "+javascore[i][j]);
            }
        }
    }
}
