public class ReverseInteger{
    public int reverse(int x) {
        if (x == 0 || x == Integer.MIN_VALUE || x == Integer.MAX_VALUE) {
            return 0;
        }
        if (x < 0) {
            return -1 * reverse(-1 * x);
        }
        long result = 0;
        while (x > 0) {
            result *= 10;
            result += x % 10;
            x /= 10;
        }
        if (result > Integer.MAX_VALUE || result < Integer.MIN_VALUE) {
            return 0;
        }
        return (int) result;
    }


    public static void main(String[] args) {
        ReverseInteger testing = new ReverseInteger();
        System.out.println(testing.reverse(103));
        System.out.println(testing.reverse(-103));
        System.out.println(testing.reverse(0));
    }
}