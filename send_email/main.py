import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_daily_email():
    sender_address = '2132272512@qq.com'
    sender_pass = 'fabatcjbmkandbac'
    receiver_address = '1985835442@qq.com'

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Daily Report'  # The subject line

    # The body and the attachments for the mail
    message.attach(MIMEText('This is the daily report email.', 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.qq.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    print('Mail Sent')


# Call the function
send_daily_email()
