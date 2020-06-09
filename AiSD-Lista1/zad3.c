#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct node {
    int value;
    struct node *next;
    struct node *prev;
} node_t;

node_t *list1;
node_t *list2;

int size1 = 0;
int size2 = 0;

time_t temp_time;
clock_t clck;

void initialize_list(node_t **list, int val, int *size){
    (*list) = (node_t *)malloc(sizeof(node_t));
    (*list)->next = *list;
    (*list)->prev = *list;
    (*list)->value= val;
    *size = 1;
}

void add_first(node_t **list, int value, int *size){
    node_t *new_node = (node_t *)malloc(sizeof(node_t));
    new_node->value = value;

    node_t *old_start = *list;
    node_t *end = old_start->prev;

    new_node->next = old_start;
    new_node->prev = end;

    old_start->prev = new_node;
    end->next = new_node;

    (*list) = new_node;

    (*size)++;
}

void add_last(node_t **list, int value, int *size){
    node_t *new_node = (node_t *)malloc(sizeof(node_t));
    new_node->value = value;

    node_t *old_end = (*list)->prev;
    
    new_node->next = (*list);
    new_node->prev = old_end;

    old_end->next = new_node;
    (*list)->prev = new_node;

    (*size)++;
}

void remove_node(node_t **list, int index, int *size){
    int id = index % *size;
    node_t *to_del = *list;
    if(id <= (*size)/2){
        for(int i=0; i<id; i++){
            to_del = to_del->next;
        }
    }
    else{
        for(int i=0; i<(*size)-id; i++){
            to_del = to_del->prev;
        }
    }

    node_t *end = (to_del)->prev;
    node_t *new_start = (to_del)->next;
    end->next = new_start;
    new_start->prev = end;

    if(id == 0)
        *list = new_start;
    
    free(to_del);
    (*size)--;
}

int get_element(node_t **list, int index, int *size){
    int id = index % *size;
    node_t *ans = *list;
    if(id <= (*size)/2){
        for(int i=0; i<id; i++){
            ans = ans->next;
        }
    }
    else{
        for(int i=0; i<(*size)-id; i++){
            ans = ans->prev;
        }
    }
    return ans->value;
}

void print_list(node_t *list, int size){
    node_t *current = list;
    for(int i=0; i<size; i++){
        printf("%d ", current->value);
        current = current->next;
    }
    printf("\n");
}

void generate_random(node_t **list, int *size, int my_size){
    initialize_list(list, rand()%100, size);
    for(int i=0; i<my_size-1; i++){
        add_first(list, rand()%100, size);
    }
}

void merge(node_t **list1, node_t **list2, int *size1, int *size2){
    node_t *first_start = *list1;
    node_t *second_start = *list2;
    node_t *first_end = first_start->prev;
    node_t *second_end = second_start->prev;
    
    first_end->next = second_start;
    second_start->prev = first_end;

    second_end->next = first_start;
    first_start->prev = second_end;
    
    *list2 = NULL;
    (*size1) += (*size2);
}

int main(){
    int size = 10000;
    srand((unsigned)time(&temp_time));
    generate_random(&list1, &size1, size);
    print_list(list1, size1);
    
    //losowy element
    int el_id = 0;
    double rand_time_taken = 0;
    for(int i=0; i<10000; i++){
        el_id = rand() % size;
        clck = clock();
        int element = get_element(&list1, el_id, &size1);
        clck = clock() - clck;
        rand_time_taken += ((double)clck)/CLOCKS_PER_SEC;
    }
    double rand_avg_time = rand_time_taken/10000;
    printf("Random, average time: %fs\n", rand_avg_time);

    //dokladny element
    el_id = 7500;
    double time_taken = 0;
    for(int i=0; i<10000; i++){
        clck = clock();
        int element = get_element(&list1, el_id, &size1);
        clck = clock() - clck;
        time_taken += ((double)clck)/CLOCKS_PER_SEC;
    }
    double avg_time = time_taken/10000;
    printf("Id = %d, average time: %fs\n",el_id, avg_time);

    //merge
    generate_random(&list1, &size1, 5);
    generate_random(&list2, &size2, 7);
    print_list(list1, size1);
    print_list(list2, size2);
    merge(&list1, &list2, &size1, &size2);
    print_list(list1, size1);
    //print_list(list2, size2);
}
