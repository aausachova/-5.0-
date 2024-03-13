n = int(input())
a = (int(input()) for _ in range(n))
print(sum(k // 4 + min(k % 4, 2) for k in a))
