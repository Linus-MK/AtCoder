n = int(input())
x = input()

f = [-1] * (n+10)
f[0] = 0

for i in range(1, n+10):
    # python bitcount で見つけたこれを参考に https://ameblo.jp/316228/entry-10518720149.html
    f[i] = f[i % bin(i).count('1')] + 1

init_bitcount = x.count('1')
# Xを init_bitcount+1とinit_bitcount-1で割った余り

x_mod_01 = 0
for digit in x:
    x_mod_01 *= 2
    if digit == '1':
        x_mod_01 += 1
    x_mod_01 %= (init_bitcount+1)

if init_bitcount != 1:
    x_mod_10 = 0
    for digit in x:
        x_mod_10 *= 2
        if digit == '1':
            x_mod_10 += 1
        x_mod_10 %= (init_bitcount-1)

# print(x_mod_01, x_mod_10, init_bitcount)

power_mod_01 = [-1] * (n+10)
power_mod_01[0] = 1
for i in range(1, n+10):
    power_mod_01[i] = power_mod_01[i-1] * 2 % (init_bitcount + 1)

if init_bitcount != 1:
    power_mod_10 = [-1] * (n+10)
    power_mod_10[0] = 1
    for i in range(1, n+10):
        power_mod_10[i] = power_mod_10[i-1] * 2 % (init_bitcount - 1)


for i in range(n):
    if x[i] == '0':
        # 0→1
        first_residue = (x_mod_01 + power_mod_01[n - i - 1]) % (init_bitcount+1)
        print(f[first_residue] + 1)
    else:
        if init_bitcount == 1:
            # 立っているビットの数は0桁、つまりX_i = 0なのでf(X_i) = 0
            print(0)
            continue
        # 1→0
        first_residue = (x_mod_10 - power_mod_10[n - i - 1]) % (init_bitcount-1)
        print(f[first_residue] + 1)

# https://twitter.com/kyopro_friends/status/1281949470100353024
# https://atcoder.jp/contests/aising2020/editorial 公式
# 1回の操作で桁数以下に落ちることに注意すると、操作の繰り返しで急速に値が小さくなり、少ない回数で0に到着する。
# したがってfの表を作るのは今回不要。愚直にやってもできるので。初回の高速化だけが必要。
