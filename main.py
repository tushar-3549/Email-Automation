import pandas as pd
from send_email import send_email

csv_file = "emails.csv"
df = pd.read_csv(csv_file)

for index, row in df.iterrows():
    send_email(row["email"], row["name"])
