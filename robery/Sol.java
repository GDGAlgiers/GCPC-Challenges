import java.io.IOException;
import java.util.Scanner;

public class Sol {
    static int n_row = 0;
    static int n_col = 0;
    static int[][] visit;
    static String[][] maze;

    public static String findEscape(int x, int y) {
        visit[x][y] = 1;

        if (x == 0 || x == n_row - 1 || y == 0 || y == n_col - 1) { // check if current position is possible escape
            return x + "," + y;
        }

        if (maze[x - 1][y].equals("1") && visit[x - 1][y] == 0) { // check if element on top is free and not visited
            String neighborEscape = findEscape(x - 1, y);
            if (!neighborEscape.equals("")) {
                return x + "," + y + "-" + neighborEscape;
            }
        }

        if (maze[x][y + 1].equals("1") && visit[x][y + 1] == 0) { // check if element on right is free and not visited
            String neighborEscape2 = findEscape(x, y + 1);
            if (!neighborEscape2.equals("")) {
                return x + "," + y + "-" + neighborEscape2;
            }
        }

        if (maze[x + 1][y].equals("1") && visit[x + 1][y] == 0) { // check if element under is free and not visited
            String neighborEscape3 = findEscape(x + 1, y);
            if (!neighborEscape3.equals("")) {
                return x + "," + y + "-" + neighborEscape3;
            }
        }

        if (maze[x][y - 1].equals("1") && visit[x][y - 1] == 0) { // check if element on left is free and not visited
            String neighborEscape4 = findEscape(x, y - 1);
            if (!neighborEscape4.equals("")) {
                return x + "," + y + "-" + neighborEscape4;
            }
        }

        return "";
    }

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        try {
            n_row = Integer.parseInt(scanner.nextLine());
            n_col = Integer.parseInt(scanner.nextLine());
            String input_maze = scanner.nextLine();
            int x0 = scanner.nextInt();
            int y0 = scanner.nextInt();

            maze = new String[n_row][n_col];
            visit = new int[n_row][n_col];

            String[] lst = input_maze.split(" ");
            int index = 0;
            for (int i = 0; i < n_row; i++) {
                for (int j = 0; j < n_col; j++) {
                    maze[i][j] = lst[index++];
                }
            }

            System.out.println(findEscape(x0, y0));
        } finally {
            scanner.close();
        }
    }
}
