# include<stdio.h>
int main(){
    int n;
    printf("Enter number of elements for array:\n");
    scanf("%d", &n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }
    int freq[1000000] = {0};

    for(int i=0;i<n;i++){
        freq[arr[i]]++;
    }
    int found = -1;

    for(int i=0;i<n;i++){
        if(freq[arr[i]] ==1){
            found = arr[i];
            break;
        }
    }
    
    if(found ==-1){
        printf("No non repeating element found.\n");
    }else{
        printf("First non repeating element is: %d", found);
    }
    return 0;
}