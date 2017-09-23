import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Testing {
    public static int triple(int x) {
        System.out.println("I am tripling " + x);
        return x * 3;
    }
    public static boolean isEven(int x) {
        return x % 2 == 0;
    }
    public boolean isOdd(int x) {
        return !isEven(x);
    }

    public static void main(String[] args) {
        List<Integer> list =  Stream.of(1,2,3).collect(Collectors.toList());

        list.stream()
                .map(Testing::triple)
                .filter(Testing::isEven)
                .forEach(System.out::println);

    }
}