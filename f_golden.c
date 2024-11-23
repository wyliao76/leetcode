#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main() {
    int n;
    double phi;
    int* list;

    printf("Type a number: \n");
    scanf("%d", &n);

    phi = (1 + sqrt(5)) / 2;
    list = (int*) calloc(n, sizeof(size_t));
    list[0] = 0;
    list[1] = 1;
    list[2] = 1;

    for (int i=3; i<n; i++)
    {
        double tmp = phi * list[i-1];
        list[i] = (int) round(tmp);
        // printf("%f : %d \n", tmp, list[i]);
    }

    for (int i = 0; i < n; i++)
    {
        printf("%d", list[i]);
        if (i != n - 1) {
            printf(", ");
        }
    }
    printf("\n");

    free(list);
    return EXIT_SUCCESS;
    // 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
}