from bs4 import BeautifulSoup
from fields import Talabat
from utils import get_next_data
from parser import * 

import requests

r = requests.get('https://www.talabat.com/uae/restaurant/621133/ginos-deli-jlt?aid=1308')
soup = BeautifulSoup(r.text, 'lxml')

print (parse(soup))

# print (parse_menu(soup))
# print (parse(soup))
