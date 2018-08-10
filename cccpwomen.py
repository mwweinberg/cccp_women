#python3

from bs4 import BeautifulSoup
import requests

url = 'https://web.archive.org/web/20171221213907/http://ldzl.people.com.cn:80/dfzlk/front/personProvince1.htm'

#get the web page
page = requests.get(url)

#creates a new BS holder based on the URL
soup = BeautifulSoup(page.text, 'lxml')

# extracts the list of provinces from the block on the left side of the page
# like on this page https://web.archive.org/web/20171221213907/http://ldzl.people.com.cn:80/dfzlk/front/personProvince1.htm
for entry in soup.find_all("div", {"class": "fl nav_left_2j"}):
    #breaks out each province list item
    for item in entry.find_all("li"):
        link = item.find('a').get('href')
        #there is no link for the Taiwan entry so this pulls it out to avoid an error
        if link == None:
            pass
        #for the rest of the links, makes them a full URL
        else:
            full_link = 'https://web.archive.org' + link
        print(full_link)
        #extracts the name of the province
        province = item.get_text()
        print(province)
