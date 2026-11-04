#include <stdio.h>
#include <stdlib.h>

#define N 3

int goal[N][N] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 0}
};

int heuristic(int state[N][N]) {
    int h = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (state[i][j] != 0 &&
                state[i][j] != goal[i][j]) {
                h++;
            }
        }
    }

    return h;
}

int isGoal(int state[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (state[i][j] != goal[i][j])
                return 0;
        }
    }

    return 1;
}

void printState(int state[N][N], int g) {
    int h = heuristic(state);

    printf("\nMatrix:\n");

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf("%d ", state[i][j]);

        printf("\n");
    }

    printf("\ng = %d\n", g);
    printf("h = %d\n", h);
    printf("f = %d\n", g + h);
}

void copyState(int source[N][N], int dest[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            dest[i][j] = source[i][j];
        }
    }
}

void solve(int state[N][N]) {
    int g = 0;

    while (!isGoal(state)) {
        printState(state, g);

        int x, y;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (state[i][j] == 0) {
                    x = i;
                    y = j;
                }
            }
        }

        int bestState[N][N];
        int bestH = 100;

        int dx[4] = {-1, 1, 0, 0};
        int dy[4] = {0, 0, -1, 1};

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx >= 0 && nx < N &&
                ny >= 0 && ny < N) {

                int temp[N][N];

                copyState(state, temp);

                temp[x][y] = temp[nx][ny];
                temp[nx][ny] = 0;

                int h = heuristic(temp);

                if (h < bestH) {
                    bestH = h;
                    copyState(temp, bestState);
                }
            }
        }

        if (bestH >= heuristic(state)) {
            printf("\nNo better move found.\n");
            break;
        }

        copyState(bestState, state);
        g++;
    }

    printState(state, g);

    if (isGoal(state))
        printf("\nGoal State Reached!\n");
    else
        printf("\nCould not reach Goal State.\n");
}

int main() {
    int state[N][N];

    printf("Enter Initial State:\n");

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &state[i][j]);
        }
    }

    solve(state);

    return 0;
}