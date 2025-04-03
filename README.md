### Email Automation with Python

This project automates the process of sending customized HTML emails to multiple recipients using Python. It loads email addresses and names from a CSV file, generates a personalized email for each recipient, and sends them via SMTP.

### Features

- Sends customized emails using an HTML template.
- Loads recipient information from a CSV file.
- Uses environment variables for email configuration.
- Supports sending via Gmail's SMTP server.

### Tech Stack

    - Python
    - Jinja2 (for HTML template rendering)
    - SMTP (via Gmail)
    - pandas (for reading CSV files)
    - dotenv (for environment variables)

**Setup**
- Add your email credentials:
```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
```
- SMTP Server Configuration

The default SMTP server is set to Gmail's SMTP server (smtp.gmail.com) with port 587. If you're using a different email provider, you can modify the SMTP_SERVER and SMTP_PORT values in the config.py file.
- Prepare the CSV File

***Create a CSV file (emails.csv) with the following structure:***
```
email,name
recipient1@example.com,Mr X
recipient2@example.com,Mr Y
```
- Run the Email Sending Script

***Once everything is set up, run the Python script to send the emails:***

- This will send a customized email to each recipient listed in the CSV file using the HTML template.

