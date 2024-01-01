def list_swap(list, old_num, new_num):
    for i in range (len(list)):
        if list[i] == old_num:
           list[i] = new_num
    return list

print(list_swap([1, 10, 5, 6, 7, 5, 45], 5, 0))
