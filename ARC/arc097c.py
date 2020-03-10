s = input()
k = int(input())

substring_list = []
for i in range(1, 5+1):
    for start in range(len(s) - i + 1):
        substring_list.append(s[start:start+i])

# print(substring_list)
substring_list = sorted(set(substring_list))
print(substring_list[k-1])

# https://stackoverflow.com/questions/2931672/what-is-the-cleanest-way-to-do-a-sort-plus-uniq-on-a-python-list
# sortしてuniqueする場合は一回setを使うとよい
