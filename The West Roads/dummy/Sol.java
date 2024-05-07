import java.io.IOException;
import java.util.Scanner;

public class Sol {
    public static long solve(long x) {
        long sum = 0;
        for (long i = 1; i < x; i++) {
            sum += i;
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        try {
            long x = Integer.parseInt(scanner.nextLine());

            System.out.println(solve(x));
        } finally {
            scanner.close();
        }
    }
}
