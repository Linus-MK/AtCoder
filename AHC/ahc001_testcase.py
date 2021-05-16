import random

n = round(50 * 4 ** random.random())
print(f'n={n}')

# x, y
coords_list = []
xs = []
ys = []
for i in range(n):
    x = random.randrange(10000)
    y = random.randrange(10000)
    assert (x, y) not in coords_list
    coords_list.append((x, y))
    xs.append(x)
    ys.append(y)

# r
limit = 10**8
r = random.sample(range(1, limit), n-1)
r = [0] + sorted(r) + [limit]

# print(r)


import matplotlib
import matplotlib.pyplot as plt
import math

plt.style.use('ggplot')

fig = plt.figure()

ax = fig.add_subplot(1,1,1)

ax.scatter(xs,ys)

ax.set_xlabel('x')
ax.set_ylabel('y')

for i in range(n):
    xi = xs[i]
    yi = ys[i]
    area = r[i+1] - r[i]
    x_width = math.sqrt(area) * random.uniform(0.8, 1.25)
    y_width = area / x_width
    x_width = 200
    y_width = 200

    rect1 = matplotlib.patches.Rectangle((xi-x_width//2, yi-y_width//2), 
                                        x_width, y_width, 
                                        edgecolor='black', fill=False) 
    ax.add_patch(rect1) 

ax.set_aspect('equal')
fig.show()
plt.savefig('hoge.png')

import numpy as np
print(np.min(np.diff(r)))