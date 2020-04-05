n = int(input())

max_i = 1
i = 1
while i*i <= n:
    if (n//i)*i == n:
        max_i = i
    i += 1

print(max_i + (n//max_i) - 1 - 1)
