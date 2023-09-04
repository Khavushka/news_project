# automatiing repetitive tasks is a common use case for python. in this project, you will build an automated email sender that can send personalized emails to a list of recipients. you will use python's built-in email library to compose and send emails programmatically. this project will provide insights into email protocols, handling attachments, and sending emails in bulk. 

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add the message body
    msg.attach(MIMEText(message, 'plain'))

    # Setup the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    try:
        # Start the SMTP server connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to the email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        print('Email sent successfully!')
    except Exception as e:
        print('An error occurred while sending the email:', str(e))
    finally:
        # Terminate the SMTP server connection
        server.quit()

# Example usage
sender_email = 'your-email@gmail.com'  # Your Gmail email address
sender_password = 'your-password'  # Your Gmail password
recipient_email = 'recipient-email@example.com'  # Email address of the recipient
subject = 'Automated Email'  # Email subject
message = 'Hello, this is an automated email.'  # Email message

send_email(sender_email, sender_password, recipient_email, subject, message)