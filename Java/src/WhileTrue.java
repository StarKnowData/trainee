public class WhileTrue {
    public static void main(String[] args){
        System.out.println("Whiletre");


        int i = 0;

        while(true){
            i++;

            System.out.println("while"+i);

            if(i>1000000){
                break;
            }
        }
    }
}
