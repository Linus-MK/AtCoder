import sys

n = int(input())
# setで管理とlistで管理するのとどっちが良いんだろう……
# setでやる
num_set = set(range(1, 2*n+1+1))
for i in range(n+1):
    say = list(num_set)[0]
    print(say)
    num_set.remove(say)
    sys.stdout.flush()
    num = int(input())
    if num == 0:
        exit()
    else:
        num_set.remove(num)
