import smtplib
from cred import email, password

def amzn(message):
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(email, password)
    session.sendmail(email, email, message)
    session.quit()