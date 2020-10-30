import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class InsertList {



    public static void main(String[] args){

        int[] scores = {99,85,82,63,60};

        List list = new ArrayList();


        for(int i : scores){
            list.add(i);
        }


        int ss = 65;


        list.add(ss);



        list.sort(new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                return 0;
            }
        });




    }

}
