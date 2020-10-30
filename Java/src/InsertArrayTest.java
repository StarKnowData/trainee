import java.util.Arrays;

public class InsertArrayTest {
    public static void main(String[] args){

        int[] test = {8,4,2,1,23,344,12};

        Arrays.sort(test);

        for (int i:test) {
            System.out.println(i);
        }


        int i = test.length;

        int[] test2 = new int[i+1];

        for(int j=0;j<i;j++){
            test2[j] = test[j];
        }

        test2[i] = 10;

        Arrays.sort(test2);

        for (int m:test2) {
            System.out.println(m);
        }


    }
}
