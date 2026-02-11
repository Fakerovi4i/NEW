class My_dict(dict):
    def get(self, key, default=None):
        if default is None:
            default = 0
        return super().get(key, default)

my_dict = My_dict()

my_dict[1] = 100

my_dict[2] = 200
my_dict[3] = 0
my_dict[0] = 300

print(my_dict)
data_get = my_dict.get(25, 'n')
print(data_get)
