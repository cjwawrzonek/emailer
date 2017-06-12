import smtplib
import json

from email.mime.text import MIMEText

""" Quick email function
parameters:
	user:	 a gmail username
	passw: 	 a password to authenticate gmail
	to: 	 recipient address
	subject: email subject
	body: 	 email body text """
def send_gmail(user, passw, to, subject, body):
	sent_from = user + '@gmail.com'

	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = sent_from
	msg['To'] = to

	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(sent_from, passw)
		server.sendmail(sent_from, to, msg.as_string())
	except:
		pass

	server.close()