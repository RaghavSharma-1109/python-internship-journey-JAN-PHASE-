# include<stdio.h>
int lower_bound(int arr[], int n, int target){
    int low=0;
    int high=n-1;
    int ans =n;

    while(low<=high){
        int mid = low+ (high - low)/2;
        if(arr[mid]>=target){
            ans = mid;
            high = mid-1;
        }else{
            low=mid+1;
        }
    }
}
int upper_bound(int arr[], int n, int target) {
    int low = 0;
    int high = n - 1;
    int ans = n;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] > target) {
            ans = mid;
            high = mid - 1;   // move left
        } else {
            low = mid + 1;
        }
    }

    return ans;
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
    int first = lower_bound(arr,n,target);
    int last = upper_bound(arr,n,target) -1;

    printf("The first and Last occurence of target is: %d, %d", first, last);
    
    return 0;
}