n, a, b= list(map(int, input().split()))

kuri = n // (a+b)
amari = n % (a+b)
print(kuri * a + min(amari, a))