# たまに出てくるABC-C問題のbit全探索。

n = int(input())

# 証言を何で管理するか……辞書からなる配列にしよう
testimonies = [{} for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        testimonies[i][x-1] = y

ans = 0
for idx in range(1<<n):
    honest_idx = [j for j in range(n) if (1<<j)& idx > 0]

    valid = True
    for i in range(n):
        # 正直者の場合だけ証言を考慮すればよい
        if i in honest_idx:
            curr_test = testimonies[i]
            for key, value in curr_test.items():
                # 正直者と言っているのに実際は不親切な人ならダメ
                if value == 1 and key not in honest_idx:
                    valid = False
                # 不親切な人と言っているのに実際は正直者ならダメ
                if value == 0 and key in honest_idx:
                    valid = False
    
    if valid:
        ans = max(ans, len(honest_idx))

print(ans)
