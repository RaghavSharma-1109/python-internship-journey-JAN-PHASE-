# include<stdio.h>
int can_be_strictly_increasing(int arr[], int n){

    int removed = 0; 
    for(int i=0; i<n-1; i++){
        if(arr[i]>=arr[i+1]){
            removed++;
            if(removed>1){
                return 0;
            }
            if(i>0 && arr[i-1]>=arr[i+1]){
                arr[i+1] = arr[i];
            }
        }
    }
    return 1;
}
int main(){
    int n;
    printf("Enter number of element in array:\n");
    scanf("%d",&n);
    int arr[n];
    for(int i=0; i<n;i++){
        scanf("%d", &arr[i]);
    }
    if(can_be_strictly_increasing(arr,n)){
        printf("You array is strictly increasing!!\n");
    }else{
    printf("Your array can't be strictly increasing.\n");
    }
    return 0;
}
