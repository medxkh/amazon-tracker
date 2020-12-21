import requests

URL="https://www.amazon.fr/Megaport-3-70-5-30GHz-GeForce-Centrale-Ordinateur/dp/B08FTHCRR5/"
title_id="productTitle"
price_id="priceblock_saleprice"
image_url_id="https://images-na.ssl-images-amazon.com/images/I/61u8hpl1AHL._AC_SX679_.jpg"

r = requests.get(URL)
html_str=r.text
print(html_str)