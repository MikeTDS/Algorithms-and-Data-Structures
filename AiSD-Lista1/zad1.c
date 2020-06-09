#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

int queue[MAX];
int last;
time_t temp;

int get_size(){
    return last+1;
}

void add_new_element(int x){
    if(last < MAX-1){
        last++;
        queue[last] = x;
    }
}

void remove_element(){
    for(int i=0; i<get_size(); i++){
        queue[i]=queue[i+1];
    }
    last--;
}

int get_first(){
    if(get_size != 0)
        return queue[0];
    else
        return -1;
}

int get_last(){
    if(get_size != 0)
        return queue[last];
    else
        return -1;
}

void initialize_queue(){
    srand((unsigned)time(&temp));
    last = -1;
}

void generate_queue(){
    printf("Generated queue: ");
    for(int i=0; i<30; i++){
        int rd = rand()%100;
        add_new_element(rd);
        printf("%d ", rd);
    }
    printf("\n");
}

void show_queue(){

    printf("Pierwszy element = %d\n", get_first());
    printf("Ostatni element = %d\n",get_last());
    printf("Rozmiar = %d\n", get_size());
    printf("\n");
    printf("Dodawanie elementu: 100\n");
    add_new_element(100);
    printf("Ostatni element = %d\n", get_last());
    printf("Rozmiar = %d\n", get_size());
    printf("\n");
    printf("Usuwanie elementu\n");
    remove_element();
    printf("Pierwszy element = %d\n", get_first());
    printf("Rozmiar = %d\n", get_size());
    printf("\n");
    printf("Dodawanie elementu: 101\n");
    add_new_element(101);
    printf("Ostatni element = %d\n", get_last());
    printf("Rozmiar = %d\n", get_size());
    printf("\n");
    printf("Usuwanie elementu\n");
    remove_element();
    printf("Pierwszy element = %d\n", get_first());
    printf("Rozmiar = %d\n", get_size());
}

int main(){
    initialize_queue();
    generate_queue();
    show_queue();
    return 0;
}