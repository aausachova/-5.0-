n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
prefix_sum = [0]*(max(a)+2)

for num in a:
    prefix_sum[num] += 1
for i in range(1, max(a)+2):
    prefix_sum[i] += prefix_sum[i-1]
for i in range(len(prefix_sum)-1):
    count = max(count, prefix_sum[i+1] - prefix_sum[max(0, i-1)])

print(n - count)
