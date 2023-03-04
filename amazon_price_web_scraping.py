from bs4 import BeautifulSoup
import requests
from smtplib import SMTP

product = "https://www.amazon.com/dp/B0B18VW7VS/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B0B18VW7VS&pd_rd_w=1i4m7&content-id=amzn1.sym.fc40fdbf-2388-405b-a964-03cdb84a009a&pf_rd_p=fc40fdbf-2388-405b-a964-03cdb84a009a&pf_rd_r=S8AHHDMSAV5A71Q0Y8M7&pd_rd_wg=D7VIx&pd_rd_r=f525d058-6c20-4a8e-b214-218a544d0457&s=kitchen&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTDJNWk1BMjJWSUtRJmVuY3J5cHRlZElkPUEwMjEzOTE4MkZRSjhTRVNBRTBPUCZlbmNyeXB0ZWRBZElkPUEwMzI2ODUwMkpFTFFUM0ROUVUwOCZ3aWRnZXROYW1lPXNwX2RldGFpbF90aGVtYXRpYyZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

head = {
    "User-Agent": user_agent,
    "Accept-Language": accept_language,
}

# will use requests module to get the html code of the website
response = requests.get(product, headers=head)
# print(response.text)

# will use this html code response to create beautifulsoup

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

price = soup.find(name="span", class_="a-offscreen")
product_price_str = price.getText()
product_price = float(product_price_str.split("$")[1])
print(product_price)


# let's start sending mail
send_msg = f"Subject: Price alert\n\nCurrent price of product from your wishlist is ${product_price}.This is the best time to make your purchase\n" \
           f" {product}"
print(send_msg)
if product_price <= 300:
    smtp = SMTP("smtp.gmail.com", port=587)
    smtp.starttls()
    smtp.login(user=from_mail_id, password=password)
    smtp.sendmail(from_addr=from_mail_id, to_addrs=to_mail_id, msg=send_msg)
