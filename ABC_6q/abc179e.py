n, x, m =list(map(int, input().split()))

# 漸化式に従って値が変わるが、それは高々m通りの値しか取らない。
# 循環が先頭ではなく途中に戻るパターンもある
# (n -> n^2は1通りだが、n^2 -> nは正負で2通りあるため非可逆)
# したがって、先頭+周期部分に分割して、先頭 + 周期を何周したか + 余り で計算すれば良い

# ABC175 D Moving Pieceの細かい条件が簡潔なバージョンと言うか、179Eのほうが簡単じゃないか? 配点逆じゃない?
# https://atcoder.jp/contests/abc175/tasks/abc175_d

mod_list = [x]
mod_dict = {x: 0}
now = x
idx = 0

while True:
    now = now ** 2
    now %= m

    idx += 1
    if now in mod_dict:
        # 周期が見つかった
        period = idx - mod_dict[now]
        initial = mod_dict[now]
        break
    else:
        mod_list.append(now)
        mod_dict[now] = idx
    
# print(mod_list)
# print(mod_list[:initial])
# print(initial)

if n <= initial:
    print(sum(mod_list[:n]))
else:
    ans = 0
    ans += sum(mod_list[:initial])

    loop_num = (n - initial) // period
    rest = (n - initial) % period

    ans += sum(mod_list[initial:]) * loop_num
    ans += sum(mod_list[initial: initial+rest])
    print(ans)

