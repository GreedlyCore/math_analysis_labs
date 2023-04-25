from math import factorial

import numpy as np
from itertools import *

# перевод из массивных индексов в тензорные
array_to_matrix = dict([("0", "11"), ("1", "21"), ("2", "12"), ("3", "22")])
matrix_to_array = dict([("11", "0"), ("21", "1"), ("12", "2"), ("22", "3")])

number_to_array = dict([("11", "0"), ("12", "1"), ("21", "2"), ("22", "3")])
array_to_number = dict([("0", "11"), ("1", "12"), ("2", "21"), ("3", "22")])

superarray_to_number = dict([("0", "1"), ("1", "2")])
number_to_superarray = dict([("1", "0"), ("2", "1")])
x = np.array([
    [[-2, -2, 1, 6], [-1, -1, -5, 4], [-1, -2, -3, -6], [-5, -4, 2, -1]],
    [[6, 0, -2, -1], [-3, 5, 4, 4], [1, -3, -5, -3], [-1, -5, 2, 6]
     ]
])
'''
TENSOR
j определяется номером строки
p определяется номером столбца 
m определяется номером слоя по горизонтали
k определяется номером слоя по вертикали
l определяется номером суперслоя по горизонтали
ARRAY
super_layer
matrix
number
'''


# 11222
def get_number_tensor(idx):
    arr = list(idx)
    superlayer = arr[4]
    matrix = arr[2] + arr[3]
    number = arr[0] + arr[1]
    # "1", matrix_to_array["12"], number_to_array["22"]
    return eval(
        "x[{}][{}][{}]".format(number_to_superarray[superlayer], matrix_to_array[matrix], number_to_array[number]))


print(get_number_tensor("22111"))
print(get_number_tensor("11122"))


def get_new_sym_element_tensor(idx):
    print(set([get_number_tensor(tensor_idx) for tensor_idx in get_special_permutatinons(idx)]))

    print([get_number_tensor(tensor_idx) for tensor_idx in get_special_permutatinons(idx)])
    return round(
    ((1 / factorial(4)) * sum([get_number_tensor(tensor_idx) for tensor_idx in get_special_permutatinons(idx)])), 2)


def get_special_permutatinons(idx):
    all_permutations = []
    x = list(idx)
    i = list(permutations(x[0] + x[1] + x[3] + x[4], 4))
    for elem_i in i:
        all_permutations.append(elem_i[0] + elem_i[1] + x[2] + elem_i[2] + elem_i[3])
    return all_permutations


print(get_new_sym_element_tensor("22211"))
print(get_special_permutatinons("22211"))
print(len(get_special_permutatinons("22211")))


def get_answer_permutations():
    cc = 0
    answer = []
    for c in ["1", "2"]:
        for d in ["11", "21"]:
            for e in ["11", "12"]:
                s = e + d + c
                answer.append(s)
                cc += 1
    print("--")
    for c in ["1", "2"]:
        for d in ["11", "21"]:
            for e in ["21", "22"]:
                s = e + d + c
                answer.append(s)
                cc += 1
    print("--")
    for c in ["1", "2"]:
        for d in ["12", "22"]:
            for e in ["11", "12"]:
                s = e + d + c
                answer.append(s)
                cc += 1
    print("--")
    for c in ["1", "2"]:
        for d in ["12", "22"]:
            for e in ["21", "22"]:
                s = e + d + c
                answer.append(s)
                cc += 1
    return answer
answer = []
cc = 0
for string in get_answer_permutations():
    ans = get_new_sym_element_tensor(string)
    print(string, "the element here is ", get_number_tensor(string), " ", ans)
    cc += 1
    answer.append(ans)
print("count, ", cc)
print(answer)
