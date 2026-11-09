#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> numeros = {1, 3, 5, 7};
    vector<int> dobles;

    // Recorré numeros y agregá cada número multiplicado por 2 a dobles.

    for (int numero : numeros) {
        int doble = numero * 2;
        dobles.push_back(doble);
        cout << doble << ' ';
    }
    cout << '\n';
    return 0;
}