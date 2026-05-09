#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int lights[3][3];

int x[4] = {1, 0, -1, 0};
int y[4] = {0, -1, 0, 1};

void switch_light(int i, int j) {
    lights[i][j] = !lights[i][j];

    int k;
    for(k = 0; k < 4; k++) {
        int ni = i + x[k], nj = j + y[k];
        if(ni >= 0 && ni < 3 && nj >= 0 && nj < 3) {
            lights[ni][nj] = !lights[ni][nj];
        }
    }
}

int main() {
    int i, j, aux;
    while(cin >> aux) {
        for(i = 0; i < 3; i++) {
            for(j = 0; j < 3; j++) {
                lights[i][j] = 1;
            }
        }

        if(aux % 2 == 1) {
            switch_light(0, 0);
        }

        for(i = 1; i < 3; i++) {
            cin >> aux;
            if(aux % 2 == 1) {
                switch_light(0, i);
            }
        }

        for(i = 1; i < 3; i++) {
            for(j = 0; j < 3; j++) {
                cin >> aux;
                if(aux % 2 == 1) {
                    switch_light(i, j);
                }
            }
        }

        for(i = 0; i < 3; i++) {
            for(j = 0; j < 3; j++) {
                cout << lights[i][j];
            }

            cout << endl;
        }
    }

    return 0;
}