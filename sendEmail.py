import smtplib
from email.message import EmailMessage

def email_alert(to,subject,body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to

    user = "abko27700@gmail.com"
    msg['from'] = user
    password = "ihpgrckozrtjpwjg"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


