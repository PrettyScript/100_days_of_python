numbers = [1, 2, 3]
new_numbers = [num + 1 for num in numbers]
print(new_numbers)

name = "Jessica"
letters_list = [letter for letter in name]

double_num = [num * 2 for num in range(1, 5)]
# print(double_num)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)
