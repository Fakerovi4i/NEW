
def create_dict(data, template=None):
    if isinstance(data, (dict, list, set)):
        return data
    if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        template = {data: data}
        return template

def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_list.append(create_dict(i_element))
    return new_list

data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)
print(data)
