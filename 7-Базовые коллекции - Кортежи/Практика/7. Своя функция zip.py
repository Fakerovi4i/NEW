string_1 = [1, 2, 3, 4]
tuple_1 = (1, 2, 3, 4, 5)

if isinstance(string_1, dict):
    new_list = ((tuple_1[i_index], i_key) for i_index, i_key in enumerate(string_1))
elif isinstance(tuple_1, dict):
    new_list = ((string_1[i_index], i_key) for i_index, i_key in enumerate(tuple_1))
else:
    new_list = (
        (tuple_1[i_index], string_1[i_index])
        for i_index in range(min(len(string_1), len(tuple_1)))
    )

for i in new_list:
    print(i)
