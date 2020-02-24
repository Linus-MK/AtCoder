#include<iostream>
using namespace std;

long long mod = 1000000000 + 7;
long long modinv_table[200000+1];


long long power(int x, int a){
   	if (a == 0)
		return 1;
	else if (a == 1)
		return x;
	else if (a % 2 == 0){
        long long te = power(x, a/2);
        return te * te % mod;
    }
    else{
        long long te = power(x, a/2);
        return (te * te)% mod * x % mod;
    }
}

long long modinv(int x){
	return power(x, mod-2);
}


long long binomial(int n, int k){
    long long ans = 1;
    for (int i=0; i<k; i++){
        ans *= n-i;
        ans %= mod;
        ans *= modinv_table[i+1];
        ans %= mod;
    }
    return ans;
}

int main()
{
    // スペース区切りの整数の入力
    int n, a, b;
    cin >> n >> a >> b;

    for (int i=1; i<b+1; i++){
        modinv_table[i] = modinv(i);
    }

    long long ans;
    ans = power(2, n) - 1;
    ans -= binomial(n, a);
    ans -= binomial(n, b);
    ans += (mod) * 3;

    ans %= mod;

    cout << ans << endl;
    return 0;
}
