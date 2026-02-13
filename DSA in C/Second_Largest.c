#include <stdio.h>
#include <limits.h>
int Second_Larget(int arr[], int n){
    int largest = INT_MIN;
    int second_largest = INT_MIN;

    for (int i = 0; i < n; i++) {
        if (arr[i] > largest) {
            second_largest = largest;
            largest = arr[i];
        } else if (arr[i] < largest && arr[i] > second_largest) {
            second_largest = arr[i];
        }
    }
    if (second_largest == INT_MIN)
        return -1;
    return second_largest;

}
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
    int sec_largest = Second_Larget(arr, n);
    printf("The second Largest element in array is: %d", sec_largest);

    return 0;
}