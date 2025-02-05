# SMTP configaration
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER =  "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
