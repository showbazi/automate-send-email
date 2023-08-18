import os
from datetime import date
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from send_email import send_email

if "__file__" in locals():
    current_dir = Path(__file__).resolve().parent
else:
    current_dir = Path.cwd()

envs = current_dir / ".env"
load_dotenv(envs)

sheet_id = os.getenv("SHEET_ID")
sheet_name = os.getenv("SHEET_NAME")
URL = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

def load_df(url):
    parse_dates = ["due_date", "reminder_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df

def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present >= row["reminder_date"].date()) and (row["has_paid"] == "no"):
            send_email(
                subject=f'[Invoice reminder] Invoice: {row["invoice_no"]}',
                receiver_email=row["email"],
                name=row["name"],
                due_date=row["due_date"].strftime("%d, %b %Y"),  # example: 11, Aug 2022
                invoice_number=row["invoice_no"],
                amount=row["amount"],
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"

# @app.lib.cron()
# def cron_job(event):
df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)