
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class AES {
    public static String encrypts(String data, String key) throws Exception {
        byte[] encryptData = encrypt(data.getBytes("UTF-8"), key.getBytes());
        System.out.println(Base64.encodes(encryptData));
        return Base64.encodes(encryptData);
    }

    public static byte[] encrypt(byte[] data, byte[] key) throws Exception {
    	IvParameterSpec zeroIv = new IvParameterSpec("0000000000000000".getBytes());
        SecretKeySpec seckey = new SecretKeySpec(key, "AES");
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, seckey, zeroIv);
        byte[] encryptedData = cipher.doFinal(data);
        return encryptedData;

    }

    
}
