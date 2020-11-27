import smtplib, ssl
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "krutheeka.dev@gmail.com"
receiver_email = "krutheeka.rajkumar@gmail.com"
password = input("Type your password and press enter:")
message = """\
Subject: Hi there

This message is sent from Python."""
s = smtplib.SMTP(host='localhost', port=port)
s.starttls()
s.login(sender_email, password)

msg = MIMEMultipart()

# setup the parameters of the message
msg['From']=sender_email
msg['To']=receiver_email
msg['Subject']="This is TEST"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# send the message via the server set up earlier.
s.send_message(msg)