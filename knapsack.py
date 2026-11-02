def knapsack(w, p, c):
    items = sorted(zip(w, p), key=lambda x: x[1]/x[0], reverse=True)
    profit = 0

    for wt, pr in items:
        if c >= wt:
            c -= wt
            profit += pr
        else:
            profit += pr * c/wt
            break

    return profit

w = [10, 20, 30]
p = [60, 100, 120]
c = 50

print("Maximum profit:", knapsack(w, p, c))
