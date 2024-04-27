from itertools import combinations
lst = [(2, 7), (2, 6), (1, 8), (4, 9)]
pairs = list(combinations(lst, 2))
products = [tuple1[0] * tuple2[0] for tuple1, tuple2 in pairs]
max_product = max(products)
min_product = min(products)
print((max_product, min_product))