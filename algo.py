import numpy as np

def knapsack1(weights, values, n, W):
    output = np.zeros((n + 1, W + 1))
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                output[i, w] = max(output[i - 1, w], output[i - 1, w - weights[i - 1]] + values[i - 1])
            else:
                output[i, w] = output[i - 1, w]
    return output[n, W]

def knapsack2(weights, values, n, V):
    output = np.full((n+1, V+1), 0.0)
    output[0][1:] = np.infty
    for i in range(1, n + 1):
        for v in range(1, V + 1):
            if values[i - 1] <= v:
                output[i, v] = min(output[i - 1, v], output[i - 1, v - values[i - 1]] + weights[i - 1])
            else:
                output[i, v] = output[i - 1, v]
    return output[n, V]

capacity = 8
solution1 = knapsack1([1, 3, 5, 7], [2, 4, 7, 10], 4, capacity)
solution2 = knapsack2([1, 3, 5, 7], [2, 4, 7, 10], 4, int(solution1))

print(solution1, solution2)