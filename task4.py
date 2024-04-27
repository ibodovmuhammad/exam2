def sum_of_tuples(tuples_list):
    result = []
    for tup in tuples_list:
        total = sum(tup)
        result.append(total)
    return result

input1 = [(1, 2), (2, 3), (3, 4)]
output1 = sum_of_tuples(input1)
print(output1)

input2 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
output2 = sum_of_tuples(input2)
print(output2)