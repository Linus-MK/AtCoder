x = input()
ll = len(x)

now = 0
mod_dict = {}
mod_dict[0] = 1
for i in reversed(range(len(x))):
    now = now + int(x[i]) * pow(10, (ll - i - 1), 2019)

    now %= 2019
    if now not in mod_dict:
        mod_dict[now] = 1
    else:
        mod_dict[now] = mod_dict[now] + 1

ans = 0
for v in mod_dict.values():
    ans += v * (v-1) // 2
print(ans)

