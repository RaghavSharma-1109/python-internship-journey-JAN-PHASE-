#include <stdio.h>

int isSorted(int arr[], int n) {
    if (n < 2) return 1;

    int i = 0;

    // Skip equal elements
    while (i < n - 1 && arr[i] == arr[i + 1]) {
        i++;
    }

    // If all elements are equal
    if (i == n - 1) return 1;

    // Determine direction
    int ascending = arr[i] < arr[i + 1];

    for (; i < n - 1; i++) {
        if (ascending && arr[i] > arr[i + 1])
            return 0;
        if (!ascending && arr[i] < arr[i + 1])
            return 0;
    }

    return ascending ? 1 : -1;
}
