##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
# name,email,year,month,day
# YourName,your_own@email.com,today_year,today_month,today_day
from datetime import datetime
import pandas
from random import randint
import smtplib

MY_EMAIL = "jessicatestingwithpython@gmail.com"
MY_PASSWORD = "ljshdhjnad()@"

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
# print(birthdays_dict)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"./letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday\n\n{contents}"
        )
