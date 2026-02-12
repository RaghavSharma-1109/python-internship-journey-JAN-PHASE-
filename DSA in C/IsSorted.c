# include<stdio.h>
int isSorted(int arr[], int n){
    if(n<2){
        return 1;
    }
    for(int i=0;i<n-1;i++){
        if(arr[i]>arr[i+1]){
            return 0;
        }
    }
    return 1;
}
int main(){
    int n;
    printf("Enter no. of elements for array:\n");
    scanf("%d", &n);
    int arr[n];
    for(int i=0; i<n;i++){
        scanf("%d" ,&arr[i]);
    }

    int result;
    result = isSorted(arr,n);
    if(result){
        printf("The array is Sorted.\n");
    }else{
        printf("The array is Not Sorted.\n");
    }
    return 0;
}