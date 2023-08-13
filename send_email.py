import os;
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

PORT=587
EMAIL_SERVER="smtp-mail.outlook.com"

current_dir = Path(__file__).resolve().parent if *__file__* in locals else Path.cwd()

envs = current_dir / ".env"
load_dotenv(envs)


