n, a, b, c, d = list(map(int, input().split()))
s = input()

ans = "Yes"

count_empty_max = count_empty = 0
count_rock_max = count_rock = 0
for i in range(a-1, c):
    if s[i] == '#':
        count_rock += 1
        count_empty = 0
        count_rock_max = max(count_rock_max, count_rock)
    else:
        count_empty += 1
        count_rock = 0
        count_empty_max = max(count_empty_max, count_empty)

count_empty = 0
count_rock = 0
for i in range(b-1, d):
    if s[i] == '#':
        count_rock += 1
        count_empty = 0
        count_rock_max = max(count_rock_max, count_rock)
    else:
        count_empty += 1
        count_rock = 0
        count_empty_max = max(count_empty_max, count_empty)


if count_rock_max >= 2:
    ans = 'No'
if c > d and count_empty_max <= 2:
    ans = 'No'
print(ans)

'''
15 1 3 15 7
...#.#...#.#...
で、Noが真の答えなのにYesを出してしまう。

実は、実際に移動をシミュレーションしたほうが良かったのかもしれない？？？
'''