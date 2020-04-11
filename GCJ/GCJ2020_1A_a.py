# URL

N = int(input())
for ix in range(N):
    n_pat = int(input())
    patterns = [input() for ip in range(n_pat)]

    # 各条件を、init/mid/finの3つに分割する

    inits = []
    fins = []
    mids = []

    for pattern in patterns:
        first_index = pattern.find('*')
        last_index = pattern.rfind('*')
        init = pattern[:first_index]
        # print(init)
        inits.append(init)
        fin = pattern[last_index+1:]
        fins.append(fin)
        # print(fin)
        mids.append(pattern[first_index+1:last_index].replace('*', ''))

    # print(inits)
    # print(fins)
    # print(mids)
    flag = True

    # initsの整合性チェック
    ans_init = ''

    for init in inits:
        temp = min(len(ans_init), len(init))
        if init[:temp] != ans_init[:temp]:
            flag = False
            break
        if len(ans_init) < len(init):
            ans_init = init

    # finsの整合性チェック
    ans_fin = ''
    for fin in fins:
        temp = min(len(ans_fin), len(fin))
        if temp > 0 and fin[-temp:] != ans_fin[-temp:]:
            flag = False
            break
        if len(ans_fin) < len(fin):
            ans_fin = fin

    # 
    ans_mid = ''.join(mids)

    # print(ans_init, ans_mid, ans_fin)
    ans = 'hoge'
    if flag:
        ans = ans_init + ans_mid + ans_fin
    else:
        ans = '*'
    print("Case #{0}: {1}".format(ix+1, ans))
