import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp-mail.outlook.com"

if "__file__" in locals():
    current_dir = Path(__file__).resolve().parent
else:
    current_dir = Path.cwd()

envs = current_dir / ".env"
load_dotenv(envs)

sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")

# function that will send the email
def send_email(receiver_email, subject, due_date, name, invoice_number, amount ):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Pawan Carriers", sender_email))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
            Hi {name},
            We hope this email finds you well.

            We would like to remind you about an upcoming payment that is due. The details are as follows:

            Invoice Number: Rs.{invoice_number}
            Due Amount: ${amount}
            Due Date: {due_date}

            Your prompt attention to this matter is greatly appreciated. If you have already made the payment, please disregard this reminder.

            If you have any questions or concerns regarding the invoice, feel free to reach out to us.

            Thank you for your business!

            Best regards,
            Pawan Carriers
        """
    )

    msg.add_alternative(
        f"""\
            <html>
                <body>
                    <p>Hi {name},</p>
                    <p>We hope this email finds you well.</p>
                    <p> We would like to remind you about an upcoming payment that is due. The details are as follows:</p>
                    <p>Invoice Number: <strong>Rs.{invoice_number}</strong></p>
                    <p>Due Amount: <strong>${amount}</strong></p>
                    <p>Due Date: <strong>{due_date}</strong></p>
                    <p>Your prompt attention to this matter is greatly appreciated. If you have already made the payment, please disregard this reminder.</p>
                    <p>If you have any questions or concerns regarding the invoice, feel free to reach out to us.</p>
                    <p>Thank you for your business!</p>
                    <p>Best regards</p>
                    <p>Pawan Carriers</p>
                </body>
            </html>
        """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    send_email(
        subject="Invoice Reminder",
        name="Baipalli Sagar",
        receiver_email="mail.bsagar@gmail.com",
        due_date="15, Aug 2023",
        invoice_number="ABC-123-456-789",
        amount="5000",
    )









