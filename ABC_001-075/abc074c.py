# 総当たり：
# A, Bは30以下。30より大きいと重量の制約を満たせないから。
# 砂糖が溶け残らずに入る最大量は、E = 100, F = 3000 のときで、1500g. なので
# Dを総当たり（1500/2 = 750以下）してCを最大値決め打ち
# 30 * 30 * 750 = 750000 でいけるだろ。

a, b, c, d, e, f = list(map(int, input().split()))
ans_water = 1
ans_sugar = 0

for i_a in range(30+1):
    for i_b in range(15+1):
        water = 100 * a * i_a + 100 * b * i_b
        if water == 0:
            continue
        if water > f:
            continue
        for i_d in range(750+1):
            sugar = d * i_d
            if water + sugar > f:
                continue
            if sugar > water // 100 * e:
                continue
            sugar_max = water // 100 * e
            sugar_max = min(sugar_max, f - water)
            i_c = (sugar_max - sugar) // c

            # print(water, sugar, i_a, i_b, i_d, sugar_max, i_c)
            # if sugar + c * i_c == sugar_max:
            #     sugar += c * i_c
            #     print("{} {}".format(water + sugar, sugar))
            #     print("###")
            #     exit()
            
            sugar += i_c * c

            if sugar / water >= ans_sugar / ans_water:
                ans_sugar = sugar
                ans_water = water
                # print("koushin: ")
                # print(water, sugar, i_a, i_b, i_d, sugar_max, i_c)

print("{} {}".format(ans_water + ans_sugar, ans_sugar))
