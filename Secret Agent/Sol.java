import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Sol {
    private static final Map<Character, String[]> digitEquivalent = new HashMap<Character, String[]>() {{
        put('0', new String[]{"0", "8"});
        put('1', new String[]{"1", "2", "4"});
        put('2', new String[]{"1", "2", "3", "5"});
        put('3', new String[]{"2", "3", "6"});
        put('4', new String[]{"1", "4", "5", "7"});
        put('5', new String[]{"2", "4", "5", "6", "8"});
        put('6', new String[]{"3", "5", "6", "9"});
        put('7', new String[]{"4", "7", "8"});
        put('8', new String[]{"0", "5", "7", "8", "9"});
        put('9', new String[]{"6", "8", "9"});
    }};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String pin = scanner.nextLine();
        scanner.close();
        List<String> combinations = SecretAgent(pin);
        System.out.println(String.join(" ", combinations));
    }

    public static List<String> SecretAgent(String pin) {
        List<String> comb = new ArrayList<>();
        for (int i = pin.length() - 1; i >= 0; i--) {
            String[] arr = digitEquivalent.get(pin.charAt(i));
            comb = getCombinations(arr, comb);
        }
        return comb;
    }

    public static List<String> getCombinations(String[] arr1, List<String> arr2) {
        List<String> combination = new ArrayList<>();
        if (arr1.length == 0) return arr2;
        if (arr2.isEmpty()) return List.of(arr1);

        for (String s1 : arr1) {
            for (String s2 : arr2) {
                combination.add(s1 + s2);
            }
        }
        return combination;
    }
}
