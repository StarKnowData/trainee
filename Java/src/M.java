class A {

    public int i = 10;
    private static A aa = new A();
    private A() {
    }

    public static A getA() {
        if(aa==null){

        }
        System.out.printf("its a endless loop %d \n", aa.aa.aa.aa.aa.aa.aa.aa.i);
        return aa;
    }
}

public class M {
    public static void main(String[] args) {
        A a = A.getA();
        System.out.printf("i = %d \n", a.i);
    }
}