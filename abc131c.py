from fractions import gcd

a, b, c, d = list(map(int, input().split() ))

lcm = c * d // gcd(c,d)
temp1 = b - b//c - b//d + b//lcm
temp2 = (a-1) - (a-1)//c - (a-1)//d + (a-1)//lcm

print(temp1 - temp2)
