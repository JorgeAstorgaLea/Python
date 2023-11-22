my_set = {}
print(type(my_set))
my_set = {'Python','JavaScript','C#','C++'}
print(type(my_set))
print(my_set)
my_set_0 = {'Python','JavaScript','C++'}
my_set.difference_update(my_set_0)
print(my_set)