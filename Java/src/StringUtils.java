
import java.io.UnsupportedEncodingException;

public class StringUtils {

    public static String left(String src, int length) {
        
        if(isEmpty(src)) return src;
        if(src.length() > length) return src.substring(0, length);
        StringBuilder sb = new StringBuilder(src);
        while(sb.length() < length) sb.append(' ');
        return sb.toString();
    }
    
    public static boolean isEmpty(String src) {
        
        return src == null || src.length() == 0;
    }

    public static byte[] getBytesUtf8(String str) {
        
        if(str == null) return null;
        try {
            return str.getBytes("UTF-8");
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e);
        }
    }

    public static String newStringUtf8(byte[] bytes) {
        try {
            return bytes == null ? null : new String(bytes, "UTF-8");
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e);
        }
    }
    
}
