#python3

from bs4 import BeautifulSoup
import requests

url = 'http://ldzl.people.com.cn/dfzlk/front/personPage5296.htm'

#get the web page
page = requests.get(url)

#creates a new BS holder based on the URL
soup = BeautifulSoup(page.text, 'html.parser')

#creates the sections
head1 = soup.find_all('h1')
head2 = soup.find_all('h2')
head3 = soup.find_all('h3')
head4 = soup.find_all('h4')
body = soup.find_all('p')

print(head1,body)
