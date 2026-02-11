data = {1: "Z", 2: "X", 3: "V", 4: "g"}

if isinstance(data, dict):
    new_list = [i_data for i_index, i_data in enumerate(data.values()) if i_index % 2 == 0]
    print(new_list)
else:
        new_list = [i_data for i_index, i_data in enumerate(data) if i_index % 2 == 0]
        print(new_list)
