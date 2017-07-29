import imaplib
import unicornshield as unicorn
import time

mailServer = 'server'
mailUsername = 'name@email.com'
mailPassword = 'securePassword'

mail = None

def connect():
	global mail

	unicorn.setAll(155,155,155)
	unicorn.show()
	mail = imaplib.IMAP4_SSL(mailServer)
	mail.login(mailUsername, mailPassword)
	mail.list()
	mail.select("inbox")
	unicorn.clear()

connect()

def getUnreadmails():
	data = mail.search(None, 'UNSEEN')
	unreadmails = len(str(data[1]).split())
	if str(data[1]) == "['']":
		unreadmails = 0
	return int(unreadmails)

doNotDisturb = False
lastChecked = time.time()
waitTillNextCheck = 60*2
unreadmails = getUnreadmails()

while True:
	oldUnreadMails = unreadmails
	if time.time() > lastChecked+waitTillNextCheck:
		try:
			unreadmails = getUnreadmails()
		except:
			connect()
			unreadmails = getUnreadmails()
		lastChecked = time.time();

	if unicorn.buttonPressed() == True:
		if doNotDisturb == False:
			doNotDisturb = True
		else:
			doNotDisturb = False

	unicorn.clear()
	if doNotDisturb == True:
		unicorn.setPixel(0,0,0,155)
		unicorn.show()
	else:
		if oldUnreadMails == unreadmails:
			pass
		if unreadmails <= 9 and unreadmails >=1:
			for x in range(unreadmails):
				unicorn.setPixel(x, 0, 155, 0)
		elif unreadmails > 9:
			unicorn.setAll(155, 0, 0)
		else:
			unicorn.setPixel(0,150,150,0)
		unicorn.show()
