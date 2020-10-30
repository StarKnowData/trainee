public class ForIfTest {
    public static void main(String[] args){
        for(int i=1000;i<2080;i++){
            // 能被 4 整除，但是不能被 100 整除，或者能被 400 整除
            if(( i%4==0 && i%100!=0 )||(i%400==0)){
                System.out.println(i+" 年 是 闰年");
            }
        }
    }
}
