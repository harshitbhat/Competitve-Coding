//  while True:
//      n = int(input())
//      if n == 0:
//          break
//      print(int((n*(n+1)*(2*n + 1))/6))

#include <iostream>
using namespace std;
int main(){
    int n;
    while(1) {
        cin>>n;
        if(n==0) {
            break;
        }
        cout<< (n*(n+1)*(2*n+1))/6<<endl;
    }
}