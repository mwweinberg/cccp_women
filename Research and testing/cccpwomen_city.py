#python3

from bs4 import BeautifulSoup
import requests
from pprint import pprint


city_url = 'https://web.archive.org/web/20171004155730/http://ldzl.people.com.cn/dfzlk/front/chengqu1029.htm'

city_page = requests.get(city_url)
city_soup = BeautifulSoup(city_page.text, 'lxml')

#for entry in city_soup.find_all('ul', {'class':'clearfix ld'}):
count = 1
for entry in city_soup.find_all('em', {'class' : ''}):
    print(entry)

city_unparsed = city_soup.find_all('em', {'class' : ''})
#turns the first url into a string and then extracts it
city_url_nub_1 = str(city_unparsed[1]).split('"')[3]
#city_url1a = str(city_url1).split('"')[3]
city_url_full_1 = 'https://web.archive.org/web/20171004155730/http://ldzl.people.com.cn/dfzlk/front/' + city_url_nub_1

print(city_url_full_1)
