import email
import imaplib
import os
import boto3
from datetime import datetime
import urllib2

## downloads all email attachments to a localdirectory. need to create a gmail dev key for that
now = datetime.now()
time=now.strftime("%d-%b-%Y")

imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
typ, accountDetails = imapSession.login("invoice.collector@someemail.com", "emaildevkey")
if typ != 'OK':
    print 'Not able to sign in!'

imapSession.select('[Gmail]/All Mail')
typ, data = imapSession.search(None, '(SINCE '+time+')')
if typ != 'OK':
    print 'Error searching Inbox.'

# Iterating over all emails
for msgId in data[0].split():
    typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
    if typ != 'OK':
        print 'Error fetching mail.'

    emailBody = messageParts[0][1]
    mail = email.message_from_string(emailBody)
    for part in mail.walk():
        if part.get_content_maintype() == 'multipart':
                # print part.as_string()
            continue
        if part.get('Content-Disposition') is None:
                # print part.as_string()
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join('.', 'attachments/new', fileName)
            if not os.path.isfile(filePath):
                print fileName
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
imapSession.close()
imapSession.logout()

s3 = boto3.client('s3' ,aws_access_key_id='accesskey',
    aws_secret_access_key='secretaccesskey')

dir='/Users/ankitkumar/PycharmProjects/processemail/attachments/new/'


for filename in os.listdir(dir):
    print filename
    s3.upload_file(dir+filename, 'plated-data-science', 'logistics/'+filename)


#responce=urllib2.urlopen("https://www.ec.fedex.com/fedexnet/Login.jsp")


