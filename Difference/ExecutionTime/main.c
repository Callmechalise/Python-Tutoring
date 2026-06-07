#include <stdio.h>
#include <time.h>

int main() {
    long long i;
    long long limit = 1000000000LL;

    // start time
    clock_t start = clock();

    // counting loop
    for (i = 0; i < limit; i++) {
        // intentionally empty (no printing)
    }

    // end time
    clock_t end = clock();

    // compute time taken
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Counted to %lld\n", limit);
    printf("Time taken: %f seconds\n", time_taken);

    return 0;
}
