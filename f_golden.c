#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main() {
    double phi = (1 + sqrt(5)) / 2;
    int list[10];
    list[0] = 1;
    list[1] = 1;

    for (int i=2; i<10; i++)
    {
        double tmp = phi * list[i-1];
        list[i] = (int) round(tmp);
        printf("%f : %d \n", tmp, list[i]);
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", list[i]);
    }

    return EXIT_SUCCESS;
}