import java.io.IOException;
import java.util.Scanner;

public class Sol {
    public static long solve(long x) {
        return x * (x -1)/2;
    }

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        try {
            long x = Long.parseLong(scanner.nextLine());

            System.out.println(solve(x));
        } finally {
            scanner.close();
        }
    }
}
