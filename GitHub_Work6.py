numbers = [1, 1, 5, 5, 12]

def list_Count(numbers):
    list = {}
    for i in numbers:
        if list.get(i) is None:
            list[i] = numbers.count(i)
    return list

print(list_Count(numbers))

