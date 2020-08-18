import math
a, b, hour, minute = list(map(int, input().split()))

x_hour = a * math.cos((hour + minute/ 60)*30/180 * math.pi)
x_min = b * math.cos(minute*6 / 180 * math.pi)
y_hour = a * math.sin((hour + minute/ 60)*30/180 * math.pi)
y_min = b * math.sin(minute*6 / 180 * math.pi)

print(math.sqrt((x_hour - x_min) ** 2 + (y_hour - y_min) ** 2))
