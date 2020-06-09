#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct node {
    int value;
    struct node *next;
} node_t;

node_t *list1;
node_t *list2;

time_t temp_time;
clock_t clck;

void initialize_list(node_t *list){
    list = (node_t *)malloc(sizeof(node_t));
}

void add_first(node_t **list, int value){
    node_t *node = (node_t *)malloc(sizeof(node_t));
    node->value = value;
    //ustawiam wczesniejszy pierwszy element jako nastepny nowego
    node->next = *list;
    //podmieniam pierwszy element na nowy
    *list = node;
}

void add_last(node_t *list, int value){
    node_t *node = (node_t *)malloc(sizeof(node_t));
    node->value = value;
    node->next = NULL;

    //ustawiam aktualny na pierwszy
    node_t *current = list;
    //iteruje tak dlugo, az nie trafie na ostatni element
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = node;
}

void remove_node(node_t **list, int index) {
    node_t *current = *list;
    node_t *temp = NULL;

    if (index == 0) {
        if(*list != NULL){
            //przechowuje drugi element
            temp = (*list)->next;
            //usuwam pierwszy
            free(*list);
            //ustawiam drugi jako pierwszy
            *list = temp;
        }
    }

    else{
        //iteruje do jednego przed tym, co mam usunac
        for (int i = 0; i < index-1; i++) {
            if (current->next == NULL) {
                printf("Nie ma elementu o tym indeksie.\n");
                return;
            }
            current = current->next;
        }
        //przechowuje ten co mam usunac (n)
        temp = current->next;
        //podstawiam do next w n-1 (czyli pod n), n+1 (pod warunkiem, ze nie jest ostatni)
        if(temp->next != NULL)
            current->next = temp->next;
        else{
            current->next = NULL;
        }
        free(temp);
    }
}



void print_list(node_t *list){
    //ustawiam aktualny na pierwszy
    node_t *current = list;
    //iteruje tak dlugo, az nie trafie na koniec listy
    while (current != NULL) {
        printf("%d ", current->value);
        current = current->next;
    }
    printf("\n");
}

void generate_random_list(node_t **list, int size){
    initialize_list(*list);
    for(int i=0; i<size; i++){
        add_first(list, rand()%100);
    }
}

int get_element(node_t *list, int index){
    node_t *current = list;
    for (int i = 0; i < index; i++) {
        if (current->next == NULL) {
            printf("Nie ma elementu o tym indeksie.\n");
            return -1;
        }
        current = current->next;
    }
    return current->value;
}

void merge(node_t **list1, node_t**list2){
    node_t *current = *list1;
    while(current->next!=NULL){
        current = current->next;
    }
    current->next = *list2;
    *list2 = NULL;
}

int main(){
    int size = 10000;
    srand((unsigned)time(&temp_time));
    generate_random_list(&list1, size);
    print_list(list1);

    //merge
    // generate_random_list(&list2, size);
    // print_list(list2);
    // merge(&list1, &list2);
    // print_list(list1);
    // print_list(list2);

    //opreacje
    // add_first(*list1, 100);
    // add_last(list1, 101);
    // print_list(list1);
    
    //losowy element
    int el_id = 0;
    double rand_time_taken = 0;
    for(int i=0; i<10000; i++){
        el_id = rand() % size;
        clck = clock();
        int element = get_element(list1, el_id);
        clck = clock() - clck;
        rand_time_taken += ((double)clck)/CLOCKS_PER_SEC;
    }
    double rand_avg_time = rand_time_taken/10000;
    printf("Random, average time: %fs\n", rand_avg_time);

    //dokladny element
    el_id = 5000;
    double time_taken = 0;
    for(int i=0; i<10000; i++){
        clck = clock();
        int element = get_element(list1, el_id);
        clck = clock() - clck;
        time_taken += ((double)clck)/CLOCKS_PER_SEC;
    }
    double avg_time = time_taken/10000;
    printf("Id = %d, average time: %fs\n",el_id, avg_time);
}
