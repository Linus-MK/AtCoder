b, c = list(map(int, input().split()))

if b != 0 and c == 1:
    print(2)
    exit()

if b >= 0:
    span_posi_max = b + (c-2) //2
    span_posi_min = b - c //2
    span_nega_max = -b + (c-1) //2
    span_nega_min = -b - (c-1) //2
else:
    span_posi_max = -b + (c-1) //2
    span_posi_min = -b - (c-1) //2
    span_nega_max = b + (c-2) //2
    span_nega_min = b - c //2

ans = (span_posi_max - span_posi_min + 1) + (span_nega_max - span_nega_min + 1)
overlap = min(span_posi_max, span_nega_max) - max(span_posi_min, span_nega_min) + 1
overlap = max(overlap, 0)
print(ans - overlap)

# print(span_posi_max, span_posi_min, span_nega_max, span_nega_min)