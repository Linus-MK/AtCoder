h, w = list(map(int, input().split() ))

s = []
s.append("." * (w+2)) 
for _ in range(h):
	s.append("." + input() + ".")
s.append("." * (w+2)) 

ans = "Yes"
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]

for i in range(1, h+1):
	for j in range(1, w+1):
		if s[i][j] == "#":
			CanPaint = False
			for k in range(4):
				if s[i+dx[k]][j+dy[k]] == "#":
					CanPaint = True
			if not CanPaint:
				ans = "No"

print(ans)
