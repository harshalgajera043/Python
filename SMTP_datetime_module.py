# import smtplib
#
# my_email = "hgajera307@gmail.com"
# my_password = "ciofdsdtaowghtco"
#
# with smtplib.SMTP(host="smtp.gmail.com") as connection:
#     connection.starttls()  # To make our message encrypted
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="hgajera307@yahoo.com",
#         msg="Subject:Hello\n\nMy email body"
#     )
#
# Datetime module
import datetime as dt
date = dt.datetime.now()
# min_year = dt.MINYEAR
# max_year = dt.MAXYEAR
# print(min_year)
# print(max_year)
time = date.time()
# print(time)
# print(time.timezone())
# print(type(date.tzinfo))
# print(date.tzinfo)

My_birth_date = dt.datetime(year=2002, month=4, day=22, hour=00, minute=10)
print(My_birth_date.time())

