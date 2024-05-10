import java.util.Scanner;

public class Sol {
    public static String sol(String s) {
        String[] words = s.replace("Ctrl + C", "#c").replace("Ctrl + V", "#v").replace("Ctrl + X", "#x").split(" ");
        StringBuilder out = new StringBuilder();
        String copied = "";

        for (int i = 0; i < words.length; i++) {
            if (words[i].equals("#c")) {
                copied = out.toString();
            } else if (words[i].equals("#v")) {
                out.append(copied);
            } else if (words[i].equals("#x")) {
                copied = i < words.length - 1 ? out.toString() : out.substring(0, out.length() - 1);
                out.setLength(0);
            } else {
                out.append(words[i]).append(i < words.length - 1 ? " " : "");
            }
        }

        return out.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inline = scanner.nextLine();
        System.out.println(sol(inline));
        scanner.close();
    }
}
