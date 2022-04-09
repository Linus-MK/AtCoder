# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471

N = int(input())
for i_test in range(N):

    s = input()
    # 最後の文字は無条件に1個
    # それ以外は、直後より前ならば2個
    # 直後の文字と同じならば? そのさらに後まで行く

    ans = ""

    length = len(s)
    for i, let in enumerate(s):
        if i == length - 1:
            ans += let
        else:
            for j in range(i+1, length):
                if s[i] < s[j]:
                    ans += let * 2
                    break
                elif s[i] > s[j]:
                    ans += let
                    break
                elif j == length - 1:
                    ans += let
                    break
                else:
                    continue
    print(f"Case #{i_test+1}: {ans}")
