import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def check_price():
    url = #amazon product url wrapped in single quotes
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    product_name = soup.find('span', id='productTitle').get_text(strip=True)
    
    product_price_span = soup.find('span', class_='a-price-whole').text
    product_price_cleanup = product_price_span.replace(".", "")
    final_price = int(product_price_cleanup)
    
    def send_email():
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = #your email 
        smtp_password = #specific app password - see read me notes
        sender_email = #your email
        recipient_email = #email 
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f'DROP IN PRICE For {product_name}!'
        
        body = f'''
        <html>
            <body>
                <p>The price has dropped for <b><a href="{url}">{product_name}</a></b>.</p>
                <p>Current value is <h2><b>${final_price}</b></h2>.</p>
            </body>
        </html>
        '''
        
        msg.attach(MIMEText(body, 'html'))
        
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.quit()
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")
    
    if final_price < {final_price}:
        send_email()
    else:
        print("Price is not below (insert price here).")

schedule.every().hour.do(check_price)

while True:
    schedule.run_pending()
    time.sleep(1)
#For every 15 mintues update function here - schedule.every(15).minutes.do(check_price)
