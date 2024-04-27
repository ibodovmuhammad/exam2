def remove_duplicates(strings):
    unique_strings = []
    for string in strings:
        if string not in unique_strings:
            unique_strings.append(string)
    return unique_strings

strings = ["apple", "banana", "cherry", "apple", "banana", "date"]
print(remove_duplicates(strings))
