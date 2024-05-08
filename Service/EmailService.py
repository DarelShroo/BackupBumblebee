
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Create a multipart message and set headers
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = receiver_email
    email_message['Subject'] = subject

    # Add body to the email
    email_message.attach(MIMEText(message, 'plain'))

    # Create SMTP session for sending the email
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()

    try:
        # Login to the SMTP server
        smtp_server.login(sender_email, sender_password)

        # Convert the multipart message to a string
        email_text = email_message.as_string()

        # Send the email
        smtp_server.sendmail(sender_email, receiver_email, email_text)
        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError as e:
        print("Failed to authenticate. Please check your credentials.")
        print(e)

    except Exception as e:
        print("An error occurred while sending the email.")
        print(e)

    finally:
        # Quit the SMTP server
        smtp_server.quit()

    # Example usage
    sender_email = ''
    sender_password = ''  # Enter your Gmail password here
    receiver_email = ''
    subject = 'Hello from Python!'
    message = 'This is the content of the email.'

    send_email(sender_email, sender_password, receiver_email, subject, message)


