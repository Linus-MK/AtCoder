x, k, d = list(map(int, input().split()))

minimum = x - d * k
maximum = x + d * k

if minimum >= 0:
    print(minimum)
elif maximum <= 0:
    print(-maximum)
else:
    c1 = maximum % (2*d)
    c2 = c1 - 2*d
    print(min(abs(c1), abs(c2)))
