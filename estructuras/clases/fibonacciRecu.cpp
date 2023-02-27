#include <bits/stdc++.h>
#define endl '\n'
#define all(a) (a).begin(), (a).end()
#define punteria(a) cout<<setprecision(a)<<endl
#define print(a) cout<<a<<endl;
#define input(a) cin.ignore();getline(cin,a);
#define int long long int

using namespace std;

int fibonacci(int x){
    if(x == 1) return 0; 
    else if(x == 2) return 1; 
    else return fibonacci(x-1) + fibonacci(x-2); 
}

int32_t main(){

    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cout<<fibonacci(5)<<endl;

    return 0;
}