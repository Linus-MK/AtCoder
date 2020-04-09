n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

sorted_arr = sorted(arr)
maximum = sorted_arr[-1]
for i in range(n):
    if arr[i] == maximum:
        print(sorted_arr[-2])
    else:
        print(sorted_arr[-1])
