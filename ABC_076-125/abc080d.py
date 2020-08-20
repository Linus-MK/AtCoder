n, c = list(map(int, input().split()))

s = [0] * n
t = [0] * n
chan = [0] * n
for i in range(n):
    s[i], t[i], chan[i] = list(map(int, input().split()))

length_double = 2 * (max(t)+1)

recording_num = [0] * length_double
# tt = [0] * length_double
for i in range(1, c+1):
    tt = [0] * length_double

    for j in range(n):
        if chan[j] == i:
            tt[s[j]*2-1] += 1
            tt[t[j]*2] -= 1
    
    for j in range(1, length_double):
        tt[j] += tt[j-1]
    for j in range(length_double):
        if tt[j] > 0:
            recording_num[j] += 1
    # print(tt)

ans = max(recording_num)
print(ans)
# print(recording_num)

## 解説PDFより解説Youtubeのほうがしっくりくる
## 解説PDFは-0.5を「2倍すればいいよね」という解決法をしてるので、それいろいろな場合に応用が利くの? と思ってしまう
## 区間に対して +1を書きたい場合→始点に+1, 終点に−1をし、最後に累積和を取る

