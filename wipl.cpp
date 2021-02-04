#include <iostream>
#include <vector>
#include <algorithm>
#define INF -99999
using namespace std;
int main() {
    int T,n,k;
    cin>>T;
    while(T--) {
        cin>>n>>k;
        vector<int> arr(n);
        for(int i = 0;i< n;i++) {
            cin>>arr[i];
        }
        sort(arr.begin(),arr.end(),greater<int>());
        int h1 = 0;
        int ans = 0;
        for(int i=0;i<n;i++) {
            if(h1 >= k) {
                break;
            }
            bool foundLower = false;
            int index;
            for(int j = n-1;j>i;j--) {
                if(k-h1 <= arr[j]) {
                    index = j;
                    foundLower = true;
                    break;
                }
            }
            if(foundLower) {
                h1 += arr[index];
                arr[index] = INF;
                ans++;
            } else {
                h1 += arr[i];
                arr[i] = INF;
                ans++;
            }
        }
        int h2 = 0;
        int i = 0;
        while(i < n && h2 < k) {
            if(arr[i] == INF) {
                i++;
                continue;
            } 
            h2 += arr[i];
            ans++;
            i++;
        }
        if(n==1 || h1 < k || h2 < k) {
            cout<<"-1\n";
        } else {
            cout<<"H1 - "<<h1<<" H2 - "<<h2<<" Solution - "<<ans<<endl;
        }
    }
}