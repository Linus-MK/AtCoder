n = input()
int_n = int(n)
# len(n)桁のうち、オール9、もしくは1つを除いて9、が答え候補。候補を全探索

le = len(n)
nines = 10 ** le - 1
if nines == int_n:
    print(le*9)
    exit()

ans = 0

for i in range(le):
    for dif in range(1, 10):
        candi = nines - dif * 10 ** i
        if 9 * le - dif >= ans and candi <= int_n:
            ans = 9 * le - dif

print(ans)
