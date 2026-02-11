students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interests_lenght_surname(dict_student):
    list_interests = []
    len_sur = 0
    for i_value in dict_student.values():
        list_interests.extend(i_value['interests'])
        len_sur += len(i_value['surname'])

    return list_interests, len_sur


for i_id, i_value in students.items():
    print(f"id:{i_id} - {i_value["age"]} года")

interests_list, len_surname = interests_lenght_surname(students)

print(interests_list)
print(len_surname)