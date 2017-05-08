#! /usr/bin/env python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from subprocess import check_output
import messaging_credentials

def buildMessage(subject, sender, recepient, textMessage):
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject 
	msg['From'] = sender
	msg['To'] = recepient
	part1 = MIMEText(textMessage, 'plain')
	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	return msg

def sendEmail(recepient, message):
	subject = "UPDATED TRANSCRIPT"

	sender = messaging_credentials.sender #your email here
	password = messaging_credentials.password #the email's password

	builtMessage = buildMessage(subject, sender, recepient, message)

	server = smtplib.SMTP(messaging_credentials.server, 587) #if you are using gmail, keep this as it is. Otherwise, you need to figure out what the email server is.
	server.starttls()
	server.login(sender, password)
	server.sendmail(sender, recepient, builtMessage.as_string())

def main():
	output = check_output(["/home/2015/yzhu399/minervaclient/extras/transcript_monitor.sh"])
	
	if output != "":
		sendEmail('<%s>' % messaging_credentials.sender, output)

main()

