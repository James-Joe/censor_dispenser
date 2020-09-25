# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
import re
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", " her ", "herself"]

def cato(lst, mail):
    for i in lst:
      #mail = mail.replace(i.casefold(), "[REDACTED]")
      mail = re.sub(i, '[REDACTED]', mail)
    return mail
#print(cato(proprietary_terms, email_two))

