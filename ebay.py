import requests
from bs4 import BeautifulSoup

EBAY_URL= 'https://www.ebay.co.uk/itm/295169494643?_trkparms=%26rpp_cid%3D5d8cce9aa937f33a775e44ce%26rpp_icid%3' \
          'D5d8cce9aa937f33a775e44cd&_trkparms=pageci%3Ac3bb752e-8f3e-11ed-9016-02ba3ee4476d%7Cparentrq%3A90e9e2f' \
          '91850aa7105ae58aafffc43ac%7Ciid%3A1'
page = requests.get(url=EBAY_URL)
print(page.text)