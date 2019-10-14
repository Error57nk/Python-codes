import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def sendit(msgid):
    email_user = 'niteshraspi007@gmail.com'
    email_password = '*************'
    email_send = 'niteshkrsit@gmail.com'

    subject = 'INCOMMING'
    if(msgid == 1):
        trig='Nitesh'
        
    elif(msgid == 2):
        trig ='Avisek'

    elif(msgid == 3):
        trig ='Joydip'

    elif(msgid == 4):
        trig ='Unknown Person'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    
    body = trig + 'has visited please check detail'
    msg.attach(MIMEText(body,'plain'))

    filename='a.jpg'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()
    print("mail sent")



if __name__ == "__main__":
    sendit()
