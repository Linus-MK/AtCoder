time = [int(input()) for _ in range(5)] 

extra = [0]*5

for i in range(5):
	extra[i] = (0 if time[i] % 10 == 0 else 10 - (time[i] % 10) )

ex = sum(extra) - max(extra) # 商品が届いてからの余剰時間を最小化したいので、最大の余剰時間を引く
print(sum(time) + ex)
