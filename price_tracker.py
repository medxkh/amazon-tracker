from selenium import webdriver
from selenium.webdriver.chrome import Options
from email.message import EmailMessage
from config import Email_Adress, Email_Password




def get_product_info(driver):
    title_id="productTitle"
    price_id="priceblock_saleprice"
    image_url_id="imgTagWrapperId"
    product_title=driver.find_element_by_id(tilte_id).text
    product_price=driver.find_element_by_id(price_id).text[1:]
    product_image_url=driver.find_element_by_id(image_url_id).get_attribute('src')
    return {
        "title": product_title,
        "price": product_price,
        "image": image_url_id
    }

def send_email(product):
    break
    
URL="https://www.amazon.fr/Megaport-3-70-5-30GHz-GeForce-Centrale-Ordinateur/dp/B08FTHCRR5/"

options = Options()
options.add_argument("--headless")

CHROMEDRIVER= "/User/Applications/chromedriver"
driver = webdriver.Chrome(CHROMEDRIVER , options=options)

driver.get(URL)



print(product_title)
print(product_price)
print(product_image_url)

MAX_PRICE= 1500
if float(product_price) <= float(MAX_PRICE):
    msg=EmailMessage()
    msg['Subeject']= "amazon price tracker notification"
    msg['From']= Email_Adress
    msg['To']= Email_Adress
    msg.add_alternative("""
    <!DOCTYPE html>
    <html>
        <body>
            this is notification!
        </body>
    </html>
    """, subtype='html')
    with smtplib.SMTP_SSL('smtp.gmpail.com',465) as smtp:
        smtp.login(Email_Adress,Email_Password)
        smtp.send_message(msg)