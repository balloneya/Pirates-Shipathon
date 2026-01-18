#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int n;
    cout << "Enter integer n: ";
    cin >> n;
    int countOfN = 0;
    for (int i = 1; i <= n; i++)
    {
        int a, b, c;
        cout << "Enter values of a , b , c: ";
        cin >> a >> b >> c;
        if ((a == 1) && (b == 1))
        {
            countOfN++;
        }
        else if ((b == 1) && (c == 1))
        {
            countOfN++;
        }
        else if ((a == 1) && (c == 1))
        {
            countOfN++;
        }
        else if ((a == 1) && (b == 1) && (c == 1))
        {
            countOfN++;
        }
        cout << endl;
    }
    cout << countOfN;
}