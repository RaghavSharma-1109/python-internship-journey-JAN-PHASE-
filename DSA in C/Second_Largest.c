#include <stdio.h>
#include <limits.h>

int main() {
    int n;
    scanf("%d", &n);

    if (n < 2) {
        printf("-1");
        return 0;
    }

    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int largest = INT_MIN;
    int second_largest = INT_MIN;
    int found = 0;

    for (int i = 0; i < n; i++) {
        if (arr[i] > largest) {
            second_largest = largest;
            largest = arr[i];
            if (second_largest != INT_MIN)
                found = 1;
        } else if (arr[i] < largest && arr[i] > second_largest) {
            second_largest = arr[i];
            found = 1;
        }
    }

    if (!found) {
        printf("-1");
    } else {
        printf("%d", second_largest);
    }
    return 0;
}
