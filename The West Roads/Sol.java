import java.io.IOException;
import java.util.Scanner;

public class Sol {
    public static int solve(int x) {
        return x * (x -1) / 2;
    }

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        try {
            int x = Integer.parseInt(scanner.nextLine());
            System.out.println(solve(x));
        } finally {
            scanner.close();
        }
    }
}
