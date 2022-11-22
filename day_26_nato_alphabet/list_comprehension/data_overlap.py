with open("file1.txt") as file_1:
    file_one = file_1.readlines()
    file_one = [int(number[:1]) for number in file_one]
    # print(file_one)

with open("file2.txt") as file_2:
    file_two = file_2.readlines()
    file_two = [int(number[:1]) for number in file_two]
    # print(file_two)

data_overlap = [num for num in file_one if num in file_two]
print(data_overlap)

list_1 = [1, 2, 3]
list_2 = [2, 3, 4]

overlap = [num for num in list_1 if num in list_2]
print(overlap)
