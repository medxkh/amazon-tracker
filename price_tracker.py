from selenium import webdriver

URL="https://www.amazon.fr/Megaport-3-70-5-30GHz-GeForce-Centrale-Ordinateur/dp/B08FTHCRR5/"
title_id="productTitle"
price_id="priceblock_saleprice"
image_url_id="imgTagWrapperId"

CHROMEDRIVER= "/User/Applications/chromedriver"
driver = webdriver.Chrome(CHROMEDRIVER)

driver.get(URL)

product_title=driver.find_element_by_id(tilte_id).text
product_price=driver.find_element_by_id(price_id).text
product_image_url=driver.find_element_by_id(image_url_id).get_attribute('src')
