#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 1000000
using namespace std;
int main()
{
    int T, n;
    cin >> T;
    while (T--)
    {
        cin >> n;
        int arr[n];
        vector<int> v;
        int hash[MAX] = {0};
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            hash[arr[i]]++;
        }
        for (int i = 0; i < n; i++)
        {
            if (hash[arr[i]] == 1)
            {
                v.push_back(arr[i]);
            }
        }
        int l = v.size();
        if (l == 0)
        {
            cout << -1 << endl;
        }
        else
        {
            sort(v.begin(), v.end());
            for (int i = 0; i < n; i++)
            {
                if (arr[i] == v[0])
                {
                    cout << i + 1 << endl;
                }
            }
        }
    }
}