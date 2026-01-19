# include<stdio.h>
int isPalindrome(int arr[], int n){
    int *left = arr;
    int *right = arr +n-1;
    while(left<right){
        if(*left != *right){
            return 0;
        }
        left++;
        right--;
    }
    return 1;
}
int main(){
    int n;
    printf("Enter the number of elements in array.\n");
    scanf("%d", &n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d", arr[i]);
    }
    int result = isPalindrome(arr,n);
    if(result){
        printf("The array is PALINDROME");
    }else{
        printf("The array is not a PALINDROME");
    }
    return 0;
}
