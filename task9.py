data = list(map(int, input().split()))

shifted_data = [data[-1]] + data[:-1]

print(*shifted_data)
