import java.util.Scanner;

public class ScannerTest {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int i = sc.nextInt();
        System.out.println("Input"+i);

        double d = 81.29;

        int dd = (int)d;

        String ddd = "81.29";

        double dddd = Double.parseDouble(ddd);


        System.out.println(dd+"ddd"+dddd);





        int a = 5;

        int b = 7;


        int c ;

        c = a;
        a = b;
        b = c;


        a = (a+b)-a;

        b = (a+b)-a;


        int ii = 8349;


        int n1,n2,n3,n4;

        n1 = ii/1000;

        n2 = (ii-n1*1000)/100;

        n3 = (ii-n1*1000-n2*100)/10;

        n4 = ii%10;



        boolean  b1 = true;


        boolean  b2 = false;


        if(b1&&b2){
            System.out.println("B1&&B2");
        }

        if(b1&b2){
            System.out.println("B1&&B2");
        }







    }
}
