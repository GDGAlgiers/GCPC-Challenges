#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int maxItems(char *list[], char *price) {
    int itemsCount = 0;
    int totalPrice = atoi(price + 1);

    // Convert and sort prices
    int numItems = 0;
    while (list[numItems] != NULL) {
        numItems++;
    }
    int *items = (int *)malloc(numItems * sizeof(int));
    for (int i = 0; i < numItems; i++) {
        items[i] = atoi(list[i] + 1);
    }
    qsort(items, numItems, sizeof(int), compare);

    // Calculate max items
    for (int j = 0; j < numItems; j++) {
        if (items[j] <= totalPrice) {
            itemsCount++;
            totalPrice -= items[j];
        } else {
            break;
        }
    }

    free(items);

    return itemsCount == 0 ? "Insufficient cash!" : itemsCount;
}

int main() {
    char *itemsList[100];
    char totalPrice[10];

    char input[1000];
    fgets(input, sizeof(input), stdin);
    int i = 0;
    char *token = strtok(input, " \n");
    while (token != NULL) {
        itemsList[i] = strdup(token);
        token = strtok(NULL, " \n");
        i++;
    }
    itemsList[i] = NULL;

    scanf("%s", totalPrice);

    printf("%d", maxItems(itemsList, totalPrice));

    return 0;
}
