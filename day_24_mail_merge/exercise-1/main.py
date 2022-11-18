# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", mode="r") as file:
    # file.write("\nNew Text.")
    print(type(file))

with open("new_file.txt", mode="w") as file:
    contents = file.write("New Text.")
    print(type(contents))