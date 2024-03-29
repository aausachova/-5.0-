def result(k):
    temp = 0
    for i in range(k, 0, -1):
        temp = temp + (i * (k - i + 1)) + (k - i + 1)
    return temp - 1


def binary_search_l(value):
    left = 0
    right = 1900000
    while right - left > 1:
        middle = (left + right) // 2
        if result(middle) <= value:
            left = middle
        else:
            right = middle
    return right


n = int(input())
result_value = binary_search_l(n)
print(result_value - 1)
