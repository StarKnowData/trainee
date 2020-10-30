public class InsertArrayTest2 {
    public static void main(String[] args){

        int[] scores = {99,85,82,63,60};

        int i = 65;


        int len = scores.length;

        int[] insertedScores = new int[len+1];


        for(int k = 0; k<len;k++){
            insertedScores[k] = scores[k];
        }

        insertedScores[len] = 0;
        int k = 0;
        for( ;k<len;k++){
            if(i>scores[k]){
                break;
            }
        }

        System.out.println("K==="+k);
        //{99,85,82,63,60};

        //{99,85,82,63,60,0};

        // 99 85 82 63 63,60

        // 63->65
        int il = insertedScores.length;

        for(int m = il-1; m> il-k;m-- ){
            insertedScores[m] = insertedScores[m-1];
        }

        insertedScores[k] = i;

        for(int n = 0; n<il;n++){
            System.out.print(insertedScores[n]+"  ");
        }



    }
}
