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
    [[-5, 0, -3, 1], [1, -5, 2, -4], [-5, -4, -6, 2], [3, 0, 2, -5]],
    [[1, -5, 1, 4], [-3, 5, -1, -1], [-6, 2, 4, 2], [-4, -4, 5, 2]
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


def get_number_tensor(idx):
    arr = list(idx)
    superlayer = arr[4]
    matrix = arr[2] + arr[3]
    number = arr[0] + arr[1]
    return eval(
        "x[{}][{}][{}]".format(number_to_superarray[superlayer], matrix_to_array[matrix], number_to_array[number]))


def count_of_inverses(idx):
    count = 0
    x = [int(i) for i in list(idx)]
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[j] < x[i]:
                count += 1
    return count%2

#print(count_of_inverses("321"))

def get_new_sym_element_tensor(idx):
    return round(
        ((1 / factorial(2)) * sum([get_number_tensor(tensor_idx) for tensor_idx in
                                   get_special_permutatinons(idx)])), 2)
    # return round(
    #     ((1 / factorial(2)) * sum([(((-1) ** (count_of_inverses(tensor_idx))) * get_number_tensor(tensor_idx) )for tensor_idx in
    #                                get_special_permutatinons(idx)])), 2)


def get_special_permutatinons(idx):
    all_permutations = []
    x = list(idx)
    i = list(permutations(x[0] + x[1], 2))
    for elem_i in i:
        all_permutations.append(elem_i[0] + elem_i[1] + x[2] + x[3] + x[4])
    return all_permutations


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
