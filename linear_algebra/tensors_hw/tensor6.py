#
tensor = dict()

c = 0
t=1
r = 1
for m in range(1, 4):
    for k in range(1, 4):
        for j in range(1, 4):
            n = 2 * j + 5 * k - 5 * m - 3 * r
            print(k, j, m, r, t, "value is ", n)
            tensor.update({"{}{}{}{}{}".format(k, j, m, r, t): n})
            c += 1
print(tensor)
tensor2 = dict()
for i in range(1,4):
    old_idx = "{}{}{}{}{}".format(i,k,i,r,t)
    new_idx = "{}{}{}".format(k, r, t)
    new_value = 0
    for k in range(1, 4):
        new_value += tensor[old_idx]
    tensor2.update({new_idx: new_value})
    print(new_idx, "value is ", n)

print(tensor2)