x = int(input())

for a in range(-200, 201):
    t = a ** 5
    for b in range(-200, 201):
        if t - (b ** 5) == x:
            print('{} {}'.format(a, b))
            exit()
