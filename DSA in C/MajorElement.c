# include<stdio.h>
int main(){
    typedef struct {
        int value;
        int index;
    }pair;
    int arr[] = {8, 2, 6, 4};
    int n = 4;
    int target = 8;

    pair pairs[n];
    for(int i=0;i<n;i++){
        pairs[i].value = arr[i];
        pairs[i].index =i;
    }
    for(int j=0;i<n-1;j++){
        for(int i=0;i<n-i-1;i++){
            if(pairs[i].value>pairs[i+1].value){
                pair temp = pairs[i];
                pairs[i] = pairs[i+1];
                pairs[i+1] = temp;
            }
        }
    }
    int right = n-1;
    int left = 0;

    while(left<right){
        int sum = pairs[left.value] + pairs[right].value;

        if(sum == target){
            printf("Indices: %d and %d\n",
                pairs[left].index,
                pairs[right].index);
            break;
        }else if(sum<target) {
            left++;
        }
        else{
            right ++;
        }
    }
}