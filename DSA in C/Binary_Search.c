# include<stdio.h>
int binary_search(int arr[], int n, int target) {
    int low = 0;
    int high = n - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if(arr[mid]==target){
            return mid;
        }
        else if(arr[mid]<target){
            low = mid+1;
        }
        else if(arr[mid]>target){
            high=mid-1;
        }
    }

    return -1; // if not found
}
int main(){
    int n;
    printf("Enter number of elements for your array:");
    scanf("%d", &n);

    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }

    int target;
    printf("Enter your target:");
    scanf("%d", &target);

    int ind= binary_search(arr,n,target);
    printf("%d", ind);
    return 0;
}