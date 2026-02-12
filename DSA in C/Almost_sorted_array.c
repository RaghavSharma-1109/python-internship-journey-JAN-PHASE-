# include<stdio.h>
int main(){
    int n;
    printf("Enter number of element for array:\n");
    scanf("%d\n", &n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }

    int l= -1;
    int r= -1;
    for(int i=0;i<n-1;i++){
        if(arr[i]>arr[i+1]){
            if(l== -1){
                l=i;
            }
            r=i;
        }
    }

    if(l== -1){
        printf("1");
        return 0;
    }

    int temp = arr[l];
    arr[l] = arr[r+1];
    arr[r+1] = temp;

    for(int i=0; i<n-1;i++){
        if(arr[i]>arr[i+1]){
            printf("0");
            return 0;
        }
    }
    printf("1");
    return 0;
}