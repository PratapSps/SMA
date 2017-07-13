'''
Created on Jul 12, 2017

@author: Survya Pratap Singh
Wright State University
UID: U00803205
email: singh.survya@gmail.com
website: https://survya.com
'''
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.


# me == the sender's email address
# you == the recipient's email address
Subject= 'The contents of file'
From= "singh.survya@gmail.com"
To= "singh.survya@gmail.com"

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.sendmail(From, To, "email")
s.quit()