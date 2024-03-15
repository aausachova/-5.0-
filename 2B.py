n, k = map(int, input().split())
prices = list(map(int, input().split()))[:n]

def max_profit(n, k, prices):
    max_profit = 0

    for i in range(n):
        for j in range(i+1, min(i+k+1, n)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max(max_profit, 0)

print(max_profit(n, k, prices))
