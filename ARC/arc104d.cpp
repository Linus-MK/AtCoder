#include<iostream>
using namespace std;


int main()
{
    // スペース区切りの整数の入力
    int n, k, m;
    cin >> n >> k >> m;

    int limit = k * (n * (n+1) / 2 / 4 + 1);
    int dp[n+1][limit] = {0};
    int mod = m;
  
    dp[0][0] = 1;
    for (int j = 1; j < limit; j++){
        dp[0][j] = 0;
    }
  
    // for (int i = 0; i < n; i++){
    //     for (int j = 0; j < limit; j++){
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << endl;
    // }

  
    for (int i = 1; i < n+1; i++){
        for (int j = 0; j < limit; j++){
            // dp[i][j] = dp[i-1][j] + dp[i-1][j-i] + ... + dp[i-1][j-ki]
            if (j - (k+1) * i >= 0){
                dp[i][j] = dp[i][j-i] + dp[i-1][j];
                dp[i][j] %= mod;
                dp[i][j] -= dp[i-1][j-(k+1)*i];
                dp[i][j] %= mod;
            }else{
                long long temp = 0;
                for(int p=0; j-p*i >=0; p++){
                    temp += dp[i-1][j-p*i];
                    temp %= mod;
                }
                dp[i][j] = temp;
            }
        }
    }

    int toori[n+1] = {0};

    for (int i = 1; i <= n; i++){
        for (int j = 0; j < limit; j++){
            toori[i] += ((dp[i-1][j] * dp[n-i][j] % mod) * (k+1)) % mod;
        }
        toori[i] -= 1;
        cout << toori[i] << endl;
    }


    return 0;

}
