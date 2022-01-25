# a dynamic change calculating system
def dyncoins(v, cs):
    # initialise solution set, costs and best coin for each value
    s = [0 for x in range(len(cs))]
    C = [float("inf") for x in range(0, v + 1)]
    P = [0 for x in range(0, v + 1)]
    C[0] = 0
    # find the best denomination and cost of each value up to v
    for w in range(1, v + 1):
        for i in range(0, len(cs)):
            if (cs[i] <= w) and (C[w - cs[i]] + 1 < C[w]):
                C[w] = C[w - cs[i]] + 1
                P[w] = i + 1
    solution = "The optimal solution is {} coins".format(C[v])
    # fill the solution set with the amount of each denomination
    while v > 0:
        i = P[v] - 1
        s[i] += 1
        v -= cs[i]
    return solution + " with the set {}".format(s)


# Test the machine
coins = [1, 5, 7]
result = dyncoins(18, coins)
print(result)
