# include<stdio.h>
int main(){
    int n;
    printf("Enter number of elements for array: \n");
    scanf("%d", &n);

    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int x;
    printf("Enter the element you want to count frequency of:\n");
    scanf("%d",&x);
    int count =0;
    for(int i=0;i<n;i++){
        if(arr[i] == x){
            count++;
        }
    }
    printf("The count of frequency of your element is: %d\n",count);
    return 0;
}