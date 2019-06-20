w, h, x, y = list(map(int, input().split()))

if x*2 == w and y*2 == h:
	#center
	print("{} {}".format(w*h/2, 1))
else:
	print("{} {}".format(w*h/2, 0))
