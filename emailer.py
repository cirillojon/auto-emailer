import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Fetch the content from url
url = "https://www.cs.ucf.edu/people/all-faculty/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find emails on the page
emails = []
for a in soup.find_all('a', href=True):
    if a['href'].startswith('mailto:'):
        emails.append(a['href'][7:])  

# Prepare the message
message = """
Hello Professor, I hope you are doing well.

I was wondering if you were available to sit for my groups Senior Design Committee next week. 

I am sorry for the short notice. Let me know if you can make it, and I will provide more info regarding the location as soon as possible.

Thanks.
"""

# Connect to the email server
server = smtplib.SMTP('smtp-mail.outlook.com', 587)
server.starttls()

# Login to your email
server.login('your-email', 'your-password')

for email in emails:
    msg = MIMEMultipart()
    msg['From'] = 'your-email'
    msg['To'] = f'{email}'
    msg['Subject'] = 'Senior Design Committee Request'
    msg.attach(MIMEText(message, 'plain'))

    server.send_message(msg)
server.quit()