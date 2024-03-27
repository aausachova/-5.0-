n, k = map(int, input().split())
numbers = list(map(int, input().split()))
occurrences = {}

for i in range(n):
    if numbers[i] in occurrences and i - occurrences[numbers[i]] <= k:
        print("YES")
        exit()
    occurrences[numbers[i]] = i

print("NO")
