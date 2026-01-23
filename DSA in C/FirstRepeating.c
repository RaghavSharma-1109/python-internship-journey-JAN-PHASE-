# include<stdio.h>
int main(){
    int n;
    printf("Enter number of elements for array:\n");
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&n);
    }
    found = -1;
    int freq[1000000] = {0};
    for(int i=0; i<n;i++){
        if(freq[arr[i]] ==1){
            found = arr[i];
            break;
        }
        freq[arr[i]]++;
    }
    if (found == -1) {
        printf("No repeating element found\n");
    } else {
        printf("First repeating element is: %d\n", found);
    }

    return 0;
}