#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ROW_COL 1000
#define MAX_STR 1000

int n_row, n_col, x_init, y_init;
char maze[MAX_ROW_COL][MAX_ROW_COL];
int visit[MAX_ROW_COL][MAX_ROW_COL];

char *solve(int x, int y)
{
    char *temp = malloc(2*MAX_ROW_COL * MAX_ROW_COL * sizeof(char));
    char *neighborEscape = malloc(2*MAX_ROW_COL * MAX_ROW_COL * sizeof(char));

    visit[x][y] = 1;
    if ((x == 0) || (x == n_row - 1) || (y == 0) || (y == n_col - 1)) // check if current position is possible escape
    {
        sprintf(temp, "%d,%d", x, y);
        return temp;
    }
    if ((maze[x - 1][y] == '1') && (visit[x - 1][y] == 0)) // check if element on top is free and not visited
    {
        neighborEscape = solve(x - 1, y);
        if (neighborEscape != "")
        {
            sprintf(temp, "%d,%d-%s", x, y, neighborEscape);
            free(neighborEscape);
            return temp;
        }
    }
    if ((maze[x][y + 1] == '1') && (visit[x][y + 1] == 0)) // check if element on right is free and not visited
    {
        neighborEscape = solve(x, y + 1);
        if (neighborEscape != "")
        {
            sprintf(temp, "%d,%d-%s", x, y, neighborEscape);
            free(neighborEscape);
            return temp;
        }
    }
    if ((maze[x + 1][y] == '1') && (visit[x + 1][y] == 0)) // check if element under is free and not visited
    {
        neighborEscape = solve(x + 1, y);
        if (neighborEscape != "")
        {
            sprintf(temp, "%d,%d-%s", x, y, neighborEscape);
            free(neighborEscape);
            return temp;
        }
    }
    if ((maze[x][y - 1] == '1') && (visit[x][y - 1] == 0)) // check if element on left is free and not visited
    {
        neighborEscape = solve(x, y - 1);
        if (neighborEscape != "")
        {
            sprintf(temp, "%d,%d-%s", x, y, neighborEscape);
            free(neighborEscape);
            return temp;
        }
    }
    free(temp);
    return "";
}

int main(int argc, char *argv[])
{
    char input_maze[2*MAX_ROW_COL * MAX_ROW_COL -1];
    scanf("%d", &n_row);
    scanf("%d", &n_col);
    scanf(" %[^\n]", input_maze);
    scanf("%d", &x_init);
    scanf("%d", &y_init);

    int i,j,k =0;
    while (k<strlen(input_maze))
    {   
        maze[i][j] = input_maze[k];
        if (j == n_col-1)
        {
            i++;
            j = 0;
        }
        else
            j++;
        k += 2;
    }
    
    printf("%s\n", solve(x_init, y_init));
}