# Fractional Knapsack using Greedy Method

def fractional_knapsack(capacity, weights, profits):
    n = len(weights)

    # Calculate profit/weight ratio
    ratio = []
    for i in range(n):
        ratio.append((profits[i] / weights[i], weights[i], profits[i]))

    # Sort items in descending order of ratio
    ratio.sort(reverse=True)

    total_profit = 0

    for r, w, p in ratio:
        if capacity >= w:
            capacity -= w
            total_profit += p
        else:
            total_profit += r * capacity
            break

    return total_profit


# Main Program
weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

max_profit = fractional_knapsack(capacity, weights, profits)

print("Maximum Profit:", max_profit)