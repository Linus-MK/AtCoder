import string
lower = string.ascii_lowercase

n = int(input())

ans = ['']

for i in range(n):
    new_list = []
    for word in ans:
        for new_char in lower:
            if new_char in word:
                new_list.append(word + new_char)
            else:
                new_list.append(word + new_char)
                break
    ans = new_list
#    print(new_list)

for word in ans:
    print(word)
