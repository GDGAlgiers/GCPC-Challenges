import java.util.Scanner;

public class Main {

    public static int max(int a, int b) {
        return (a >= b) ? a : b;
    }

    public static void solve() {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int r = scanner.nextInt();
        int c = scanner.nextInt();
        System.out.println(max(n - r, r - 1) + max(m - c, c - 1));
        scanner.close();
    }

    public static void main(String[] args) {
        solve();
    }
}
