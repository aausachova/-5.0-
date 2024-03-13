n = int(input())
shicla =  list(map(int, input().split()))
res = chr(43) * (n - 1)
if not sum(shicla)%2:
    for a, b in enumerate(shicla):
        if b % 2 == 1:
            break
    a = max(0, a-1)
    res = res[:a] + chr(120) + res[a+1:]
print(res)
