my_dict = {'Tom': 2020, 'Jerri' : 2010}
print(my_dict)
print(my_dict['Jerri'])
my_dict['Dog'] = 2030
my_dict.update({'Minni':2040,
                'Mikki':2050})
f=my_dict.pop('Mikki')
print(my_dict.get('Mikki'))
print(f)
print(my_dict)
my_set={'Tom',124,'Dog',421,'Tom',124}
print(my_set)
my_set.update({555,'toffifee',(1,1.2)})
print(my_set)
print(my_set.remove(124))
print(my_set)