# 貪欲法。座標の差のうち小さいものを (m-n)個選んで、その区域を移動すればよい。

n, m = list(map(int, input().split()))
coords = list(map(int, input().split()))
coords.sort()

if n >= m:
    print(0)
else:
    coords_diff = [0] * (m-1)
    for i in range(m-1):
        coords_diff[i] = coords[i+1] - coords[i]
    
    coords_diff.sort()
    print(sum(coords_diff[:(m-n)]))
