import smtplib

my_email = "jessicatestingwithpython@gmail.com"
yahoo_email = "jessicatestingwithpython@yahoo.com"
password = "iwuxecmvqpbgznas"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # connection = smtplib.SMTP("smtp.mail.yahoo.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=yahoo_email, msg="Subject:Hello\n\nThis is the body of my email.")
