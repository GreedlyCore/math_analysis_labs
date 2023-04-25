for m in range(1, 3):
    r = 1
    for t in range(1, 3):
        for j in range(1, 4):
            for k in range(1, 4):
                n = 2 * j + 5 * k - 5 * m - 3 * r
                print(j, k, m, r, t, "value is ", n)