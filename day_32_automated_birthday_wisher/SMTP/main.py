import smtplib

my_email = "jessicatestingwithpython@gmail.com"
yahoo_email = "jessicatestingwithpython@yahoo.com"
password = "iwuxecmvqpbgznas"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     # connection = smtplib.SMTP("smtp.mail.yahoo.com")
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=yahoo_email, msg="Subject:Hello\n\nThis is the body of my email.")

import datetime as dt
from random import choice

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

# print(day_of_week)
# print(day)

date_of_birth = dt.datetime(year=1995, month=10, day=28)
# print(date_of_birth)

with open("quotes.txt") as file:
    quotes = file.readlines()
    
quote = choice(quotes)
print(quote)

days = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # connection = smtplib.SMTP("smtp.mail.yahoo.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=yahoo_email, msg=f"Subject:Random Quote\n\n{quote}").encoding('utf8')
