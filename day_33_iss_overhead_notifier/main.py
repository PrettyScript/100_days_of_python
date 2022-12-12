def reformatNumber(number: str) -> str:
    # print(number.split())
    # new_number = ''
    spaces_and_dashes = [" ", "-"]
    # number = [number.replace(char, '') for char in spaces_and_dashes]
    for char in spaces_and_dashes:
        number = number.replace(char, "")
    print(number)

    # for every third number add a dash, if no third number than dash every 2 number
    # number = list(number)
    number = list(number)
    # print("-".join(number[::2]))


reformatNumber("1-23-45 6")
