import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'yehor393@gmail.com'
EMAIL_HOST_PASSWORD = 'zbhw assr lyvt slix'


def send_email(subject, message, to_email):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()  # Enable security
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)  # Login to the server
        text = msg.as_string()
        print()
        print('///////////////////////////////////////////////')
        print(text)
        server.sendmail(EMAIL_HOST_USER, to_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")