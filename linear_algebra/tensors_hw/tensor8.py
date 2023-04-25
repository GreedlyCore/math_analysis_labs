# 3 layers
# 243 elements
# a_jk_mrt
# R^3 dimension
value1 = 0
value1_arr = [idx + i[0] + idx + i[1] + i[2] for idx in ["1", "2", "3"] for i in ["111", "221", "331"]]
print(value1_arr)
value2 = 0
value2_arr = [idx + i[0] + idx + i[1] + i[2] for idx in ["1", "2", "3"] for i in ["112", "222", "332"]]
print(value2_arr)
value3 = 0
value3_arr = [idx + i[0] + idx + i[1] + i[2] for idx in ["1", "2", "3"] for i in ["113", "223", "333"]]
print(value3_arr)
print(len(value1_arr) + len(value2_arr) + len(value1_arr))
###################3
def calc(lst):
    j=lst[0]
    k = lst[1]
    m = lst[2]
    r = lst[3]
    return (2 * j) + (5 * k) - (5 * m) - (3 * r)
print([calc([int(j) for j in list(i)]) for i in value1_arr])
print(sum([calc([int(j) for j in list(i)]) for i in value1_arr]))
print(sum([calc([int(j) for j in list(i)]) for i in value2_arr]))
print([calc([int(j) for j in list(i)]) for i in value2_arr])
print(sum([calc([int(j) for j in list(i)]) for i in value3_arr]))
print([calc([int(j) for j in list(i)]) for i in value3_arr])
