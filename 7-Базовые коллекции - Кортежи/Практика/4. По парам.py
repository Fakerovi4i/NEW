original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# new_list = [(original_list[i_index], original_list[i_index+1]) for i_index in range(0, (len(original_list)), 2)]

# new_list = [i_value for i_value in zip(original_list[::2], original_list[1::2])]

new_list = list(zip(original_list[::2], original_list[1::2]))

print(new_list)

# Тут 3 решения