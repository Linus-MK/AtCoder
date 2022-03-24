n = int(input())
str_n = str(n)

def leading(string):
    string = str(string)
    ans = 0
    for ch in string:
        if ch == '1':
            ans += 1
        else:
            return ans
    return ans

ones = 1

if n <= 9:
    print(1)
    exit()

i = 1
ans = 0
while True:
    substr = int(str_n[:i])
    ans *= 10
    ans += i - 1

    if substr//10*10+9 >= ones:
        ans += 1
    ones *= 10
    ones += 1
    
    substr = substr
    for num in range(substr+1, substr//10*10+10):
        ans -= leading(num)

    if substr == n:
        break
    i += 1

print(ans)
