p,v = map(int, input().split())
q,m = map(int, input().split())

start_1, end_1 = p - v, p + v
start_2, end_2 = q - m, q + m
res = min(end_1, end_2) - max(start_1, start_2) + 1

if res > 0:
    res = (2*m + 1) + (2*v + 1) - res
else:
    res = (2*m + 1) + (2*v + 1)
    
print(res)
