x = input()
y = input()

ans = 'Yes'
for i in range(len(x)):
    if x[i] != y[i]:
        ans = 'No'
print(ans)
