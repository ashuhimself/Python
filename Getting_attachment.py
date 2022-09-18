import imaplib, email, os

user = 'bankfeedalt@gmail.com'
password = 'APP password' #App password
imap_url = 'imap.gmail.com'
 
attachment_dir = 'C:/Users/ASUS/Desktop/Maddy/DataFiles/'
def auth(user,password,imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    return con

def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))
def search(key,value,con):
    result, data  = con.search(None,key,'"{}"'.format(value))
    return data


con = auth(user,password,imap_url)
con.select('INBOX')
msg_id = search('SUBJECT',"Fi Account Statement (Federal Bank) 01 Aug 2022 - 31 Aug 2022",con)
msg_id=msg_id[0].split()
for i in range(0, len(msg_id)):
    result, data = con.fetch(msg_id[i],'(RFC822)')
    raw = email.message_from_bytes(data[0][1])
    get_attachments(raw)