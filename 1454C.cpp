#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 1000000
int main()
{
    int t, n;
    cin >> t;
    while (t--)
    {
        cin >> n;
        int arr[n];
        int hash[MAX] = {0};
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            hash[arr[i]]++;
        }
        }
}