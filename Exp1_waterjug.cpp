#include <stdio.h>
#include <stdlib.h>

#define MAX_JARS 10
#define MAX_STATES 100000

typedef struct State {
    int amount[MAX_JARS];
    struct State *parent;
    struct State *next;
} State;

typedef struct {
    State *front;
    State *rear;
} Queue;

typedef struct {
    State *top;
} Stack;

int n, capacity[MAX_JARS], target;

State* createState(int amount[], State *parent) {
    State *s = (State*)malloc(sizeof(State));

    if (s == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }

    for (int i = 0; i < n; i++)
        s->amount[i] = amount[i];

    s->parent = parent;
    s->next = NULL;

    return s;
}

int isSameState(int a[], int b[]) {
    for (int i = 0; i < n; i++) {
        if (a[i] != b[i])
            return 0;
    }
    return 1;
}

int isVisited(int visited[][MAX_JARS], int count, int state[]) {
    for (int i = 0; i < count; i++) {
        if (isSameState(visited[i], state))
            return 1;
    }
    return 0;
}

void markVisited(int visited[][MAX_JARS], int *count, int state[]) {
    for (int i = 0; i < n; i++)
        visited[*count][i] = state[i];

    (*count)++;
}

int isGoal(int state[]) {
    for (int i = 0; i < n; i++) {
        if (state[i] == target)
            return 1;
    }
    return 0;
}

void printState(int state[]) {
    printf("(");
    for (int i = 0; i < n; i++) {
        printf("%d", state[i]);
        if (i < n - 1)
            printf(", ");
    }
    printf(")");
}

void printPath(State *state) {
    if (state == NULL)
        return;

    printPath(state->parent);
    printState(state->amount);
    printf("\n");
}

int getLevel(State *state) {
    int level = 0;

    while (state->parent != NULL) {
        level++;
        state = state->parent;
    }

    return level;
}

void enqueue(Queue *q, State *state) {
    if (q->rear == NULL) {
        q->front = q->rear = state;
    } else {
        q->rear->next = state;
        q->rear = state;
    }
}

State* dequeue(Queue *q) {
    if (q->front == NULL)
        return NULL;

    State *temp = q->front;
    q->front = q->front->next;

    if (q->front == NULL)
        q->rear = NULL;

    temp->next = NULL;
    return temp;
}

void push(Stack *s, State *state) {
    state->next = s->top;
    s->top = state;
}

State* pop(Stack *s) {
    if (s->top == NULL)
        return NULL;

    State *temp = s->top;
    s->top = s->top->next;
    temp->next = NULL;

    return temp;
}

void BFS() {
    printf("\nBFS Tree Level-wise:\n");

    Queue q;
    q.front = q.rear = NULL;

    int (*visited)[MAX_JARS] =
        malloc(MAX_STATES * sizeof(*visited));

    if (visited == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }

    int visitedCount = 0;
    int start[MAX_JARS] = {0};

    State *initial = createState(start, NULL);

    enqueue(&q, initial);
    markVisited(visited, &visitedCount, start);

    int currentLevel = -1;

    while (q.front != NULL) {
        State *current = dequeue(&q);

        int level = getLevel(current);

        if (level != currentLevel) {
            currentLevel = level;
            printf("\nLevel %d:\n", level);
        }

        printState(current->amount);
        printf("\n");

        if (isGoal(current->amount)) {
            printf("\nPath:\n");
            printPath(current);
            free(visited);
            return;
        }

        for (int i = 0; i < n; i++) {
            int newState[MAX_JARS];

            for (int j = 0; j < n; j++)
                newState[j] = current->amount[j];

            newState[i] = capacity[i];

            if (!isVisited(visited, visitedCount, newState)) {
                markVisited(visited, &visitedCount, newState);
                State *next = createState(newState, current);
                enqueue(&q, next);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j)
                    continue;

                int newState[MAX_JARS];

                for (int k = 0; k < n; k++)
                    newState[k] = current->amount[k];

                int transfer = newState[i];
                int availableSpace = capacity[j] - newState[j];

                if (transfer > availableSpace)
                    transfer = availableSpace;

                newState[i] -= transfer;
                newState[j] += transfer;

                if (!isVisited(visited, visitedCount, newState)) {
                    markVisited(visited, &visitedCount, newState);
                    State *next = createState(newState, current);
                    enqueue(&q, next);
                }
            }
        }
    }

    printf("\nNo solution found using BFS.\n");
    free(visited);
}

void DFS() {
    printf("\nDFS:\n");

    Stack s;
    s.top = NULL;

    int (*visited)[MAX_JARS] =
        malloc(MAX_STATES * sizeof(*visited));

    if (visited == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }

    int visitedCount = 0;
    int start[MAX_JARS] = {0};

    State *initial = createState(start, NULL);

    push(&s, initial);
    markVisited(visited, &visitedCount, start);

    while (s.top != NULL) {
        State *current = pop(&s);

        printState(current->amount);
        printf("\n");

        if (isGoal(current->amount)) {
            printf("\nPath:\n");
            printPath(current);
            free(visited);
            return;
        }

        for (int i = 0; i < n; i++) {
            int newState[MAX_JARS];

            for (int j = 0; j < n; j++)
                newState[j] = current->amount[j];

            newState[i] = capacity[i];

            if (!isVisited(visited, visitedCount, newState)) {
                markVisited(visited, &visitedCount, newState);
                State *next = createState(newState, current);
                push(&s, next);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j)
                    continue;

                int newState[MAX_JARS];

                for (int k = 0; k < n; k++)
                    newState[k] = current->amount[k];

                int transfer = newState[i];
                int availableSpace = capacity[j] - newState[j];

                if (transfer > availableSpace)
                    transfer = availableSpace;

                newState[i] -= transfer;
                newState[j] += transfer;

                if (!isVisited(visited, visitedCount, newState)) {
                    markVisited(visited, &visitedCount, newState);
                    State *next = createState(newState, current);
                    push(&s, next);
                }
            }
        }
    }

    printf("\nNo solution found using DFS.\n");
    free(visited);
}

int main() {
    int choice;

    printf("Enter number of jars: ");
    scanf("%d", &n);

    if (n <= 0 || n > MAX_JARS) {
        printf("Invalid number of jars!\n");
        return 1;
    }

    printf("\nEnter capacity of each jar:\n");

    for (int i = 0; i < n; i++) {
        printf("Capacity of Jar %d: ", i + 1);
        scanf("%d", &capacity[i]);

        if (capacity[i] <= 0) {
            printf("Invalid capacity!\n");
            return 1;
        }
    }

    printf("\nEnter target amount: ");
    scanf("%d", &target);

    int possible = 0;

    for (int i = 0; i < n; i++) {
        if (target <= capacity[i]) {
            possible = 1;
            break;
        }
    }

    if (!possible) {
        printf("\nTarget cannot fit in any jar.\n");
        return 1;
    }

    printf("\nChoose search algorithm:\n");
    printf("1. Breadth First Search (BFS)\n");
    printf("2. Depth First Search (DFS)\n");

    printf("\nEnter choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            BFS();
            break;

        case 2:
            DFS();
            break;

        default:
            printf("\nInvalid choice!\n");
    }

    return 0;
}