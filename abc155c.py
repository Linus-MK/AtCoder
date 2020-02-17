n = int(input())
max_num = 0
word_dict = {}
for i in range(n):
    w = input()
    temp = word_dict.get(w, 0) + 1
    word_dict[w] = temp
    if temp > max_num:
        max_num = temp

ans_list = []
for w in word_dict:
    if word_dict[w] == max_num:
        ans_list.append(w)

ans_list.sort()

for w in ans_list:
    print(w)
