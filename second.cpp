#include <iostream>
#include <cmath>
#include <list>
#include <vector>
#include <set>
using namespace std;

int main()
{
    vector<int> numbers;
    int inputValue;
    cout << "Enter numbers to add in list 1(add zero at end to stop): " << endl;
    do
    {
        cin >> inputValue;
        if (inputValue != 0)
        {
            numbers.push_back(inputValue);
        }
    } while (inputValue != 0);
    vector<int> numbers2;
    int inputValue2;
    cout << "Enter numbers to add in list 2(add zero at end to stop): " << endl;
    do
    {
        cin >> inputValue2;
        if (inputValue2 != 0)
        {
            numbers2.push_back(inputValue2);
        }
    } while (inputValue2 != 0);
    set<int> commonNumbers;
    for (int i = 0; i < (numbers.size()); i++)
    {
        for (int j = 0; j < (numbers2.size()); j++)
        {
            if (numbers[i] == numbers2[j])
            {
                commonNumbers.insert(numbers2[j]);
            }
        }
    }
    if (commonNumbers.size() == 0)
    {
        cout << "No common elements in these 2 lists";
    }
    else
    {
        cout << "There are common elements in these 2 lists";
        cout << endl;
        cout << "This is the list of common elements: ";
        int count = 0;
        for (int x : commonNumbers)
        {
            if (++count < commonNumbers.size())
                cout << x << ", ";
            else
                cout << x << ".";
        }
    }
    return 0;
}