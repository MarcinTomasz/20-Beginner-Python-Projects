from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'marcintm001@gmail.com'
email_password = '...' #generate password from Google Account


email_receiver = 'mtmalek@protonmail.com'
subject = 'sent from a script'
body = 'This is sent from a program'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    
