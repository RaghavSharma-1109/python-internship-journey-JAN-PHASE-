#include <stdio.h>
int majorityElement(int arr[], int n){
    int candidate = 0;
    int count = 0;
    for(int i=0;i<n;i++){
        if(count == 0){
            candidate = arr[i];
        }
        if(arr[i] == candidate){
            count++;
        }else{
            count--;
        }
    }
    count =0;
    for(int i=0;i<n;i++){
        if(arr[i]==candidate){
            count++;
        }
    }
    if(count>n/2){
        return candidate;
    }
    else{
        return -1;
    }
}
int main(){
    int n;
    printf("Enter number of elements for array:\n");
    scanf("%d", &n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }

    int major = majorityElement(arr,n);
    if(major == -1)
    printf("No majority element exists\n");
    else
    printf("Majority element: %d\n", major);
    return 0;
}