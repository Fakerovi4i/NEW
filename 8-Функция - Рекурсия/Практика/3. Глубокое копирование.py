import copy

site = {
'html': {
'head': {
'title': 'Куплю/продам телефон недорого'
},
'body': {
'h2': 'У нас самая низкая цена на iPhone',
'div': 'Купить',
'p': 'Продать'
}
}
}

def find_key(dict_1, prod_name):
    for i_key, i_value in dict_1.items():
        if isinstance(i_value, str):
            if "телефон" in i_value or "iPhone" in i_value:
                new_list = [i if i not in ("телефон", "iPhone") else prod_name for i in i_value.split()]
                dict_1[i_key] = " ".join(new_list)
    for i_value in dict_1.values():
        if isinstance(i_value, dict):
            find_key(i_value, prod_name)

new_list_site = []
for _ in range(2):
    product_name = input("Введите название продукта: ")
    new_site = copy.deepcopy(site)
    find_key(new_site, product_name)
    new_list_site.append(new_site)
    for i_dict in new_list_site:
        print(i_dict)


