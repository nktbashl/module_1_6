my_dict = {'a': 1234, 'b': 4321}
print(my_dict)
print (my_dict['a'])
my_dict['e']= 129
my_dict['c']= 1245
my_dict['d']= 81237
print(my_dict)
print(my_dict['d'])
del my_dict['d']
print(my_dict)

my_set = 1,2,1,2,'asdf'
my_set = set(my_set)
my_set.update([434,3,5,1])
my_set.remove(1)
print(my_set)