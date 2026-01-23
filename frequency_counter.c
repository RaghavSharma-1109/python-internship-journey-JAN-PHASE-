# include<stdio.h>
int main(){
    int n;
    printf("Enter number of elements for array.\n");
    scanf("%d" ,&n);
    int arr[n];
    for(int i=0; i<n;i++){
        scanf("%d", &arr[i]);
    }
    for(int i=0;i<n;i++){
        int flag =0;
        for(int j=0; j<i;j++){
            if(arr[i] == arr[j]){
                flag =1;
                break;
            }
        }
        if(flag ==1){
            continue;
        }
        int count = 0;
        for(int k=i; k<n; k++){
            if(arr[i] == arr[k]){
                count++;
            }
        }
        printf("%d --> %d\n", arr[i], count);

    }
    return 0;
}