
import java.util.Arrays;

public class Base64 {

    private static final byte[] CHUNK_SEPARATOR = { 13, 10 };
    private static final byte[] STANDARD_ENCODE_TABLE = { 65, 66, 67, 68, 69,
            70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
            87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
            108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
            121, 122, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 43, 47 };
    private static final byte[] URL_SAFE_ENCODE_TABLE = { 65, 66, 67, 68, 69,
            70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
            87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
            108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
            121, 122, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 45, 95 };
    private static final byte[] DECODE_TABLE = { -1, -1, -1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
            -1, -1, 62, -1, 62, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
            -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
            12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1,
            -1, 63, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
            40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51 };
    private final byte[] encodeTable;
    private final byte[] decodeTable = DECODE_TABLE;
    private final byte[] lineSeparator;
    private final int decodeSize;
    private final int encodeSize;

    private final int encodedBlockSize;
    private final int lineLength;
    private final int chunkSeparatorLength;

    public Base64() {
        this(0, CHUNK_SEPARATOR, false);
    }

    public Base64(int lineLength, byte[] lineSeparator, boolean urlSafe) {
        this.chunkSeparatorLength = lineSeparator == null ? 0 : lineSeparator.length;
        this.encodedBlockSize = 4;
        boolean useChunking = (lineLength > 0) && (this.chunkSeparatorLength > 0);
        this.lineLength = (useChunking ? lineLength / encodedBlockSize * encodedBlockSize : 0);
        if (lineSeparator != null) {
            if (containsAlphabetOrPad(lineSeparator)) {
                String sep = StringUtils.newStringUtf8(lineSeparator);
                throw new IllegalArgumentException("lineSeparator must not contain base64 characters: [" + sep + "]");
            }
            if (lineLength > 0) {
                this.encodeSize = (4 + lineSeparator.length);
                this.lineSeparator = new byte[lineSeparator.length];
                System.arraycopy(lineSeparator, 0, this.lineSeparator, 0, lineSeparator.length);
            } else {
                this.encodeSize = 4;
                this.lineSeparator = null;
            }
        } else {
            this.encodeSize = 4;
            this.lineSeparator = null;
        }
        this.decodeSize = (this.encodeSize - 1);
        this.encodeTable = (urlSafe ? URL_SAFE_ENCODE_TABLE : STANDARD_ENCODE_TABLE);
    }

    private boolean containsAlphabetOrPad(byte[] arrayOctet) {
        if (arrayOctet == null) 
            return false;
        for (byte element : arrayOctet) 
            if ((61 == element) || (isInAlphabet(element))) 
                return true;
        return false;
    }

    public boolean isInAlphabet(String basen) {
        return isInAlphabet(StringUtils.getBytesUtf8(basen), true);
    }

    public boolean isInAlphabet(byte[] arrayOctet, boolean allowWSPad) {
        for (int i = 0; i < arrayOctet.length; i++) 
            if ((!isInAlphabet(arrayOctet[i])) && ((!allowWSPad) || ((arrayOctet[i] != 61) && (!isWhiteSpace(arrayOctet[i]))))) 
                return false;
        return true;
    }

    private static boolean isWhiteSpace(byte byteToCheck) {
        switch (byteToCheck) {
        case 9:
        case 10:
        case 13:
        case 32:
            return true;
        }
        return false;
    }

    private boolean isInAlphabet(byte octet) {
        return (octet >= 0) && (octet < this.decodeTable.length) && (this.decodeTable[octet] != -1);
    }

    public byte[] decode(byte[] pArray) {
        if ((pArray == null) || (pArray.length == 0)) 
            return pArray;
        
        Context context = new Context();
        decode(pArray, 0, pArray.length, context);
        decode(pArray, 0, -1, context);
        byte[] result = new byte[context.pos];
        readResults(result, 0, result.length, context);
        return result;
    }
    
    public static byte[] decodes(byte[] pArray) {
        
        return new Base64().decode(pArray);
    }

    public static String encodes(byte[] encrypted) {

        return StringUtils.newStringUtf8(new Base64().encode(encrypted));
    }
    
    public byte[] encode(byte[] pArray)
    {
      if ((pArray == null) || (pArray.length == 0)) {
        return pArray;
      }
      Context context = new Context();
      encode(pArray, 0, pArray.length, context);
      encode(pArray, 0, -1, context);
      byte[] buf = new byte[context.pos - context.readPos];
      readResults(buf, 0, buf.length, context);
      return buf;
    }
    
    private void encode(byte[] in, int inPos, int inAvail, Context context)
    {
        if (context.eof) 
            return;
        if (inAvail < 0) {
            context.eof = true;
            if ((0 == context.modulus) && (this.lineLength == 0)) 
                return;
            byte[] buffer = ensureBufferSize(this.encodeSize, context);
            int savedPos = context.pos;
            switch (context.modulus) {
            case 0: 
                break;
            case 1: 
                buffer[(context.pos++)] = this.encodeTable[(context.ibitWorkArea >> 2 & 0x3F)];
              
                buffer[(context.pos++)] = this.encodeTable[(context.ibitWorkArea << 4 & 0x3F)];
                if (this.encodeTable == STANDARD_ENCODE_TABLE) {
                    buffer[(context.pos++)] = 61;
                    buffer[(context.pos++)] = 61;
                }
                break;
            case 2: 
                buffer[(context.pos++)] = this.encodeTable[(context.ibitWorkArea >> 10 & 0x3F)];
                buffer[(context.pos++)] = this.encodeTable[(context.ibitWorkArea >> 4 & 0x3F)];
                buffer[(context.pos++)] = this.encodeTable[(context.ibitWorkArea << 2 & 0x3F)];
                if (this.encodeTable == STANDARD_ENCODE_TABLE) 
                    buffer[(context.pos++)] = 61;
                break;
            default: 
                throw new IllegalStateException("Impossible modulus " + context.modulus);
            }
            context.currentLinePos += context.pos - savedPos;
            if ((this.lineLength > 0) && (context.currentLinePos > 0)) {
                System.arraycopy(this.lineSeparator, 0, buffer, context.pos, this.lineSeparator.length);
                context.pos += this.lineSeparator.length;
            }
        } else {
            for (int i = 0; i < inAvail; i++) {
              byte[] buffer = ensureBufferSize(this.encodeSize, context);
              context.modulus = ((context.modulus + 1) % 3);
              int b = in[(inPos++)];
              if (b < 0) 
                  b += 256;
              context.ibitWorkArea = ((context.ibitWorkArea << 8) + b);
              if (0 == context.modulus) {
                  buffer[(context.pos++)] = this.encodeTable[(context.ibitWorkArea >> 18 & 0x3F)];
                  buffer[(context.pos++)] = this.encodeTable[(context.ibitWorkArea >> 12 & 0x3F)];
                  buffer[(context.pos++)] = this.encodeTable[(context.ibitWorkArea >> 6 & 0x3F)];
                  buffer[(context.pos++)] = this.encodeTable[(context.ibitWorkArea & 0x3F)];
                  context.currentLinePos += 4;
                  if ((this.lineLength > 0) && (this.lineLength <= context.currentLinePos)) {
                      System.arraycopy(this.lineSeparator, 0, buffer, context.pos, this.lineSeparator.length);
                      context.pos += this.lineSeparator.length;
                      context.currentLinePos = 0;
                  }
              }
            }
        }
    }
    
    private int readResults(byte[] b, int bPos, int bAvail, Context context) {
        if (context.buffer != null) {
            int len = Math.min(available(context), bAvail);
            System.arraycopy(context.buffer, context.readPos, b, bPos, len);
            context.readPos += len;
            if (context.readPos >= context.pos) {
                context.buffer = null;
            }
            return len;
        }
        return context.eof ? -1 : 0;
    }

    private int available(Context context) {
        return context.buffer != null ? context.pos - context.readPos : 0;
    }

    private void decode(byte[] in, int inPos, int inAvail, Context context) {
        if (context.eof) 
            return;
        if (inAvail < 0) 
            context.eof = true;
        for (int i = 0; i < inAvail; i++) {
            byte[] buffer = ensureBufferSize(this.decodeSize, context);
            byte b = in[(inPos++)];
            if (b == 61) {
                context.eof = true;
                break;
            }
            if ((b >= 0) && (b < DECODE_TABLE.length)) {
                int result = DECODE_TABLE[b];
                if (result >= 0) {
                    context.modulus = ((context.modulus + 1) % 4);
                    context.ibitWorkArea = ((context.ibitWorkArea << 6) + result);
                    if (context.modulus == 0) {
                        buffer[(context.pos++)] = ((byte) (context.ibitWorkArea >> 16 & 0xFF));
                        buffer[(context.pos++)] = ((byte) (context.ibitWorkArea >> 8 & 0xFF));
                        buffer[(context.pos++)] = ((byte) (context.ibitWorkArea & 0xFF));
                    }
                }
            }
        }
        if ((context.eof) && (context.modulus != 0)) {
            byte[] buffer = ensureBufferSize(this.decodeSize, context);
            switch (context.modulus) {
            case 1:
                break;
            case 2:
                context.ibitWorkArea >>= 4;
                buffer[(context.pos++)] = ((byte) (context.ibitWorkArea & 0xFF));
                break;
            case 3:
                context.ibitWorkArea >>= 2;
                buffer[(context.pos++)] = ((byte) (context.ibitWorkArea >> 8 & 0xFF));
                buffer[(context.pos++)] = ((byte) (context.ibitWorkArea & 0xFF));
                break;
            default:
                throw new IllegalStateException("Impossible modulus "
                        + context.modulus);
            }
        }
    }

    private byte[] ensureBufferSize(int size, Context context) {
        if ((context.buffer == null)
                || (context.buffer.length < context.pos + size)) {
            return resizeBuffer(context);
        }
        return context.buffer;
    }

    private int getDefaultBufferSize() {
        return 8192;
    }

    private byte[] resizeBuffer(Context context) {
        if (context.buffer == null) {
            context.buffer = new byte[getDefaultBufferSize()];
            context.pos = 0;
            context.readPos = 0;
        } else {
            byte[] b = new byte[context.buffer.length * 2];
            System.arraycopy(context.buffer, 0, b, 0, context.buffer.length);
            context.buffer = b;
        }
        return context.buffer;
    }

    private static class Context {
        int ibitWorkArea;
        long lbitWorkArea;
        byte[] buffer;
        int pos;
        int readPos;
        boolean eof;
        int currentLinePos;
        int modulus;

        public String toString() {
            return String
                    .format("%s[buffer=%s, currentLinePos=%s, eof=%s, ibitWorkArea=%s, lbitWorkArea=%s, modulus=%s, pos=%s, readPos=%s]",
                            new Object[] { getClass().getSimpleName(),
                                    Arrays.toString(this.buffer),
                                    Integer.valueOf(this.currentLinePos),
                                    Boolean.valueOf(this.eof),
                                    Integer.valueOf(this.ibitWorkArea),
                                    Long.valueOf(this.lbitWorkArea),
                                    Integer.valueOf(this.modulus),
                                    Integer.valueOf(this.pos),
                                    Integer.valueOf(this.readPos) });
        }
    }

}
