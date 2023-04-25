from itertools import  *
def count_of_inverses(idx):
    count = 0
    x = [int(i) for i in list(idx)]
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[j] < x[i]:
                count += 1
    return count%2

# for i in range[]:


print([i for i in permutations("12", 2)])
print(count_of_inverses("111"))
print(count_of_inverses("211"))
print(count_of_inverses("221"))