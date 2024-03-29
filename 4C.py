def binary_search(prefix_sum, l, s):
    left = 0
    right = len(prefix_sum) - 1
    num = 0
    while left <= right:
        mid = (left + right) // 2
        if mid >= l:
            num = prefix_sum[mid] - prefix_sum[mid - l]
        else:
            num = prefix_sum[mid]
        if num == s:
            left = mid
            break
        if num < s:
            left = mid + 1
        else:
            right = mid - 1
    return left


def find_index(prefix_sum, l, s):
    if prefix_sum[l] == s:
        return 1
    index = binary_search(prefix_sum, l, s)

    if index >= len(prefix_sum):
        index -= 1
    if prefix_sum[index] - prefix_sum[index - l] == s:
        return index - l + 1

    return -1


n, m = (int(i) for i in input().split())
orcs = [int(i) for i in input().split()]

prefix_sum = [0] * (len(orcs) + 1)
for i in range(1, len(orcs) + 1):
    prefix_sum[i] = prefix_sum[i - 1] + orcs[i - 1]

for _ in range(m):
    l, s = map(int, input().split())
    print(find_index(prefix_sum, l, s))
