import smtplib
import json

from email.mime.text import MIMEText

def email(to, subject, body):
	with open('config.pvt') as config_file:
		config = json.load(config_file)

	sent_from = config['user']

	email_text = """From: %s  
	To: %s  
	Subject: %s

	%s
	""" % (sent_from, to, subject, body)

	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(sent_from, config['key'])
		server.sendmail(sent_from, to, email_text)
		server.close()
	except:
		pass