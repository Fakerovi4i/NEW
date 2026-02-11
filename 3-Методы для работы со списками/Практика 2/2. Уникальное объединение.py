def cleaner(list):
    for i in list:
        if list.count(i) > 1:
            list.remove(i)

def merge_sorted_lists(list1, list2):
    list1.extend(list2)
    cleaner(list1)
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
    return list1

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)

print(merged)