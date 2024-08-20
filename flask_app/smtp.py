import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()


class SMTP:
    def __init__(self, otp):
        self.sender = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.otp = otp

    def smtp_server(self):
        subject = "OTP For Verification"
        body = f"""
            Thank you for using
            Please find below your OTP
            OTP: {self.otp}
            """

        msg = MIMEMultipart()
        msg["From"] = self.sender
        msg["To"] = self.sender
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("PORT")))
        server.starttls()
        server.login(self.sender, self.password)

        text = msg.as_string()

        server.sendmail(self.sender, self.sender, text)

        print("mail sent")
        server.quit()
