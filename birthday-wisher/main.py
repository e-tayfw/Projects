# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas as pd
import datetime as dt
import smtplib
import random

my_email = "ethantay321@gmail.com"
pwd = "pskn iiqd lovq nexd"
birthday_data = pd.read_csv("birthday-wisher/birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (idx, row) in birthday_data.iterrows()}
print(birthdays_dict)

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today_year = now.year

if (today_month, today_day) in birthdays_dict:
    random_template_num = str(random.randint(1, 3))
    template_file = f"birthday-wisher/letter_templates/letter_{random_template_num}.txt"

    with open(template_file) as file:
        template_content = file.read()
    recipient_name = birthdays_dict[(today_month, today_day)]["name"]
    modified_template = template_content.replace("[NAME]", recipient_name)

    recipient_email = birthdays_dict[(today_month, today_day)]["email"]
    recipient_age = today_year - int(birthdays_dict[(today_month, today_day)]["year"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{recipient_email}",
            msg=f"Subject:Happy {recipient_age} Birthday!! 🎉\n\n{modified_template}",
        )
