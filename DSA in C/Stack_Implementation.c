# include<stdio.h>
#define SIZE 5

int stack[SIZE];
int top = -1;
void push(){
    int value;
    
    if(top==SIZE-1){
        printf("Stack Overflow\n");
        
    }
    printf("Enter value:");
    scanf("%d", &value);

    top++;
    stack[top] = value;
}
void pop(){

    if(top == -1){
        printf("Stack UnderFlow\n");
    }
    printf("Removed: %d\n", stack[top]);
    top--;
}
void peek(){
    if(top ==-1){
        printf("Stack is Empty.\n");
    }
    printf("Top Element: %d\n", stack[top]);
}
void display(){

    if(top == -1){
        printf("Stack Empty\n");
    }

    for(int i = top; i >= 0; i--){
        printf("%d\n", stack[i]);
    }
}
int main(){
    int choice;

    while(1){
        printf("1 Push\n 2 Pop\n 3 Peek\n 4 Display\n 5 Exit\n");
        printf("Enter Choice:\n");
        scanf("%d",&choice);
        switch(choice){
            case 1:
                push();
                break;
            
            case 2:
                pop();
                break;
            
            case 3:
                peek();
                break;
            case 4:
                display();
                break;
            
            case 5:
                return 0;
            default:
                printf("Invalid Choice")
        }
    }
}