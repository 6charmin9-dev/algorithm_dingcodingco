import java.lang.reflect.Array;
import java.util.Arrays;

public class TempleteUtils {
    public static void print(Object obj) {
        Class<?> clazz = obj.getClass();
        if (clazz.isArray()) {
           if (clazz == int[].class) {
                System.out.println(Arrays.toString((int[]) obj));
            } else if (clazz == long[].class) {
                System.out.println(Arrays.toString((long[]) obj));
            } else if (clazz == double[].class) {
                System.out.println(Arrays.toString((double[]) obj));
            } else if (clazz == char[].class) {
                System.out.println(Arrays.toString((char[]) obj));
            } else if (clazz == boolean[].class) {
                System.out.println(Arrays.toString((boolean[]) obj));
            } else if (clazz == byte[].class) {
                System.out.println(Arrays.toString((byte[]) obj));
            } else if (clazz == short[].class) {
                System.out.println(Arrays.toString((short[]) obj));
            } else if (clazz == float[].class) {
                System.out.println(Arrays.toString((float[]) obj));
            } else { // 객체 배열
                System.out.println(Arrays.toString((Object[]) obj));
            } 
        } else {
            System.out.println(obj);
        }
    }
}
