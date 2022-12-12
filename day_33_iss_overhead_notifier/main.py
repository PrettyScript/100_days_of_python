def reformatNumber(number: str) -> str:
    
    spaces_and_dashes = [" ", "-"]
    for char in spaces_and_dashes:
        number = number.replace(char, "")
    print(number)
    dash = "-"
    phone_number = number[:3] + '-' + number[3:]
    print(phone_number)



reformatNumber("1-23-45 6")
