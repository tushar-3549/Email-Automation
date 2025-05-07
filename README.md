# 📧 Email Automation with Python

This project automates the process of sending personalized HTML emails to multiple recipients using Python. It reads recipient data from a CSV file, generates customized messages using an HTML template, and sends them via SMTP.

---

## ✅ Features

- 🔹 Sends customized emails using an HTML template powered by **Jinja2**  
- 🔹 Loads recipient details (name and email) from a **CSV** file  
- 🔹 Uses **environment variables** for secure email credentials  
- 🔹 Supports **Gmail SMTP** (or any other provider with simple config changes)

---

## 🛠 Tech Stack

- **Python**
- **Jinja2** – for HTML templating  
- **pandas** – to process CSV files  
- **smtplib** – to send emails via SMTP  
- **dotenv** – for secure configuration using `.env` files

---

## ⚙️ Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/your-username/email-automation.git
cd email-automation
```
2. Install Dependencies
- Use pip to install required packages:

`pip install -r requirements.txt`

3. Add Your Email Credentials
- Create a .env file in the root directory:
    ```
    EMAIL_ADDRESS=your_email@gmail.com
    EMAIL_PASSWORD=your_email_password
    ```
- ⚠️ If you're using Gmail with 2-Step Verification, use an App Password.

4. SMTP Configuration (Optional)
- By default, the script uses Gmail:
  ```
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
  ```
- To use another email provider, update these values in config.py.

5. Prepare the Recipients List
- Create an emails.csv file in the following format:
    ```
    email,name
    recipient1@example.com,Mr X
    recipient2@example.com,Mr Y
    ```
6. Run the Script
- Use the following command to send emails:

`python send_emails.py`

- Each recipient will receive a customized email rendered from the HTML template.


