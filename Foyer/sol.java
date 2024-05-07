import java.util.Arrays;
import java.util.Scanner;

public class Sol {

    public static int sol(String[] items, String price) {
        int itemsCount = 0;
        int totalPrice = Integer.parseInt(price.substring(1));

        // Convert and sort prices
        int[] prices = new int[items.length];
        for (int i = 0; i < items.length; i++) {
            prices[i] = Integer.parseInt(items[i].substring(1));
        }
        Arrays.sort(prices);

        // Calculate max items
        for (int item : prices) {
            if (item <= totalPrice) {
                itemsCount++;
                totalPrice -= item;
            } else {
                break;
            }
        }

        return itemsCount == 0 ? "Insufficient cash!" : itemsCount;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] itemsList = scanner.nextLine().split(" ");
        String totalPrice = scanner.next();

        System.out.println(sol(itemsList, totalPrice));
        scanner.close();
    }
}
