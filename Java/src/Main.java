public class Main {
    public static void main(String[] args) throws Exception {
        String data = "123";
        String key  = "0000000000000000";
        String result = AES.encrypts(data,key);
        System.out.println(result);
    }
}
