n = int(input())
lengths = list(map(int, input().split()))

max = max(lengths)
sum = sum(lengths) - max

if max > sum:
    result = abs(max - sum)
elif max == sum:
    result = 2 * max
else:
    result = max + sum
print(result)
