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
    output = np.zeros((n + 1, V + 1))
    for i in range(1, n + 1):
        for v in range(1, V + 1):
            #todo
            return 0


print(knapsack1([1, 2, 3], [10, 15, 40], 3, 6))