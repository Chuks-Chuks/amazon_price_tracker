import requests
import lxml.html
import smtplib
import os
import dotenv

project_folder = os.path.expanduser('../amazon_price_tracker')
dotenv.load_dotenv(os.path.join(project_folder, '.env'))


def send_price_alert(message):
    senders_mail = os.getenv('SENDERS_EMAIL')
    password = os.getenv('SENDERS_PASSWORD')
    smtp_address = os.getenv('SMTP_ADDRESS')

    with smtplib.SMTP(smtp_address) as connection:
        connection.starttls()
        connection.login(senders_mail, password)
        connection.sendmail(
            senders_mail,
            "philipchuk@gmail.com",
            f"Subject: PRICE DROP!\n\n{message}",
        )


AMAZON_URL = 'https://www.amazon.co.uk/Oral-B-Toothbrush-Rechargeable-Revolutionary-Technology/dp/B08TMSQ2R7?ref_=' \
             'Oct_DLandingS_D_09bf8231_60&th=1'

AMAZON_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                  'Safari/537.36',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7,bn;q=0.6',
}
page = requests.get(url=AMAZON_URL, headers=AMAZON_HEADERS)
doc = lxml.html.fromstring(page.content)
price_whole = float(doc.xpath('//span[@class="a-price-whole"]/text()')[0])
product_title = doc.xpath('//span[@id="productTitle"]/text()')[0].split()
p_title = ""
for words in product_title:
    p_title += f"{words} "
print(p_title)
print(price_whole)
message = f"The product: {p_title} has dropped in price.\n\nHere is the link: {AMAZON_URL}"
if price_whole == price_whole:
    send_price_alert(message=message)