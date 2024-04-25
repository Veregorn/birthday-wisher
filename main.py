##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import pandas

# Obtain the current day of the month and the current month
now = dt.datetime.now()
current_month = now.month
current_day = now.day

# Read the data from the CSV file and save it in a DataFrame
data = pandas.read_csv('birthdays.csv')

# We need to iterate our DataFrame in order to check if today is someone's birthday
for index, row in data.iterrows():
    if row.month == current_month and row.day == current_day:
        # Calculate that person age
        age = now.year - row.year
        with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as file:
            letter = file.read()
            letter = letter.replace('[NAME]', row.firstName)
            letter = letter.replace('[AGE]', str(age))
        my_email = 'veregorn88@gmail.com'
        password = 'adcf mbkq gced babz'
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls() # Secure the connection
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=row.email, msg=f'Subject:Happy Birthday!\n\n{letter}')