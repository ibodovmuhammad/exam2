data = list(map(int, input().split()))

min_val = min(data)
max_val = max(data)

min_index = data.index(min_val)
max_index = data.index(max_val)

data[min_index], data[max_index] = data[max_index], data[min_index]

print(*data)