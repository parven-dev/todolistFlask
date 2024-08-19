import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def smtp_server():
    email_user = "ryanroy1400@gmail.com"
    password = ""
    sender = email_user

    subject = "OTP For Verification"
    body = f"""
        Thank you for using
        Please find below your OTP
        OTP: 
        """

    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = sender
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_user, password)

    text = msg.as_string()

    server.sendmail(email_user, sender, text)

    print("mail sent")
    server.quit()


smtp_server()
