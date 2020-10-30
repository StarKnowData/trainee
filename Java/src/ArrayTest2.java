public class ArrayTest2 {
    public static void main(String[] args){


        int[] scores = {60,90,89,70,85};

        double avg = 0.0 ;
        int sum = 0;

        for(int i:scores){
            sum+=i;
        }

        avg = sum/5;

        System.out.println(avg);
    }
}
