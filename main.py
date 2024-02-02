import sys
import requests
from bs4 import BeautifulSoup
import time

# Telegram Bot details
telegram_bot_token = '6730949806:AAHa_YusY4lCTk0a-RBKNDQ-s4S3tzOVmMs'
telegram_channel_username = '@Amanuelfantahun_af'

# Function to send messages to Telegram
def send_message_to_telegram(message):
    send_message_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    data = {
        "chat_id": telegram_channel_username,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(send_message_url, data=data)
    if response.status_code != 200:
        print("Failed to send message to Telegram channel.")

# Assign default character encoder for Python 2 (optional for Python 3)
if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')

base_url = 'https://www.jaferbooks.com/'
url = 'https://www.jaferbooks.com/shop-grid.php'

html_text = requests.get(url).content
soup = BeautifulSoup(html_text, 'lxml')
books = soup.find_all('div', class_='product product__style--3 col-lg-3 col-md-4 col-sm-6 col-12')

for book in books:
    img_src = book.find('img').get('src')
    book_image = img_src if 'http' in img_src else f"{base_url}{img_src}"

    book_title = book.find('h6').text.strip()
    book_author = book.find('small').text.strip().replace('በ ', '')
    book_price = book.find('li').text.strip()

    # Creating message for Telegram
    message = f"Title: {book_title}\nAuthor: {book_author}\nPrice: {book_price}\nImage URL: {book_image}"
    send_message_to_telegram(message)

    # Sleep for 60 seconds to avoid hitting rate limits
    time.sleep(15)
