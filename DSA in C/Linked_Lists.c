#include <stdio.h>
#include <stdlib.h>
struct Node{
    int data;
    struct Node* next;
};
struct Node* top = NULL;
void push(){
    struct Node* newNode;
    int value;

    printf("Enter the value:\n");
    scanf("%d", &value);

    newNode = (struct Node*) malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next =top;

    top = newNode;

    printf("%d Pushed\n", value);
}
void pop(){
    if(top == NULL){
        printf("Stack Underflow\n");
        return;
    }
    int temp = top;
    printf("%d popped\n", top->data);
    top = top->next;

    free(temp);
}
void peek(){
    if(top==NULL){
        printf("ُEmpty Stack\n");
        return;
    }
    printf("%d -> top element.", top-> data);
}
void display(){
    struct Node* temp =top;
    if(top==NULL){
        printf("Empty Stack\n");
        return;
    }
    printf("Stack elements:\n");

    while(temp != NULL){
        printf("%d\n", temp->data);
        temp = temp->next;
    }
}
int main(){

    int choice;

    while(1){

        printf("\n1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit\n");
        printf("Enter choice: ");
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
                exit(0);

            default:
                printf("Invalid choice\n");
        }
    }
}