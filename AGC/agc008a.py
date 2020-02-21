n = int(input())
a_ = []
b_ = []
for i in range(n):
    a, b = list(map(int, input().split()))
    a_.append(a)
    b_.append(b)

to_added = 0
for i in reversed(range(n)):
    temp = a_[i] + to_added
    residue = temp % b_[i]
    if residue == 0:
        diff = 0
    else:
        diff = b_[i] - residue

    to_added += diff

print(to_added)
