#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t >> endl;
    for (int i = 1; i <= t; i++)
    {
        int n;
        cin >> n >> endl;
        string strOfNumber = to_string(n);
        if (length(strOfNumber) == 1)
        {
            cout << "1" << endl
                 << n;
        }
        else
        {
            for (int j = 1; j < length(strOfNumber); j++)
            {
                if (strOfNumber[j] == 0)
                {
                    continue;
                }
                else
                {
                }
            }
        }
    }
    return 0;
}