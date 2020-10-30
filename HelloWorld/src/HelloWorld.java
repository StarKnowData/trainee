public class HelloWorld {
    public static void main(String[] args){
        System.out.println("Hello World");

        for(int i = 1 ;i<10;i++){
            for(int j = 1 ; j<=i;j++){
                System.out.print(i+"*"+j+"="+i*j+" ");
            }
            System.out.println();
        }
    }
}
