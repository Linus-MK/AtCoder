########関数部分##############
def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out
# https://iatlex.com/python/base_change
############################

n, length = list(map(int, input().split()))

ans_list = []
for i in range(n):
    temp_str = Base_10_to_n(i, 3)
    suppli = length - 1 - len(temp_str)
    base_0 = '0' * suppli + temp_str

    # 0→1→2→0
    base_1 = base_0.replace('0', 'x').replace('1', 'y').replace('2', 'z').replace('x', '1').replace('y', '2').replace('z', '0')
    base_2 = base_0.replace('0', 'x').replace('1', 'y').replace('2', 'z').replace('x', '2').replace('y', '0').replace('z', '1')

    ans_list.append('2' + base_0)
    ans_list.append('1' + base_1)
    ans_list.append('0' + base_2)

for ans in ans_list:
    print(ans)