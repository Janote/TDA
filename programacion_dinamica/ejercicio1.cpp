#include <iostream>
#include<vector>
using namespace std;

vector<int> M;

int ejercitoDelReyBU(int n);
int ejercitoDelRey(int i);

int main(int argc, char const *argv[])
{
    int n;
    cout << "Ejercito del Rey de: ";
    cin >> n;
    M.resize(n+1,-1);
    M[0] = 1;
    M[1] = 1;
    // cout  <<  ejercitoDelRey(n) << '\n';

    cout  <<  ejercitoDelReyBU(n) << '\n';
}

// Complejidad Temporal y Espacial: O(n)

int ejercitoDelRey(int i) {
    if (i > 1 && M[i] == -1) {
        M[i] = ejercitoDelRey(i-1) + ejercitoDelRey(i-2);
    }
    return M[i];
}


int ejercitoDelReyBU(int n) {
    // Me creo un vector de 2 posiciones inicializadas ambas en 1.
    vector<int> rec(2,1);

    for (int i = 2; i <= n; i++)
    {
        int nuevo = rec[0] + rec[1];
        rec[0] = rec[1];
        rec[1] = nuevo;
    }
    return rec[1];
}