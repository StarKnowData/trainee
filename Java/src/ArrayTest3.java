import java.util.Scanner;

public class ArrayTest3 {

    public static void main(String[] args){

        int[] test = {8,4,2,1,23,344,12};
        // 循环输出数列的值

        for(int i=0;i<test.length;i++){
            System.out.println(test[i]);
        }
        int sum=0;
        for(int i=0;i<test.length;i++){
            sum+=test[i];
        }

        System.out.println(sum);

        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();

        for(int i=0;i<test.length;i++){
            if(num==test[i]){
                System.out.println("包含"+num);
            }
        }

    }
}
