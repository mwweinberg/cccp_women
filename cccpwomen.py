#python3

from bs4 import BeautifulSoup
import requests
from pprint import pprint

#this is the top level url
#url = 'https://web.archive.org/web/20171221213907/http://ldzl.people.com.cn:80/dfzlk/front/personProvince1.htm'


#variables for db writing
title = ''



url = 'https://web.archive.org/web/20171212033200/http://ldzl.people.com.cn:80/dfzlk/front/personPage6129.htm'

#get the web page
page = requests.get(url)

#creates a new BS holder based on the URL
soup = BeautifulSoup(page.text, 'lxml')

# this gets the title and rank_indiv
# it just finds the first instance of this thing because it appears twice on the page
for entry in soup.find("span", {"class": "red2"}):

    #breaks up the titles if there are multiple titles for the one peson
    title = entry
    if '、' in title:
        title_split = title.split('、')
    elif '，' in title:
        title_split = title.split('、')
    else:
        title_split = title

    #adds the titles to a list of dictionaries for writing later
    #this may be something that can be done  more effidiently at the db writing stage
    #I just broke it out  here to make sure I could identify the position properly

    #this list of dics will  have title:rank_indiv
    title_list = {}

    for item in title_split:
        title_list[item] = (title_split.index(item)+1)

    print(title_list)

# this is the gender section
gender = soup.find('p').contents[1]
print(gender)

#this is the dob section
dob_unparsed = soup.find('p').contents[5]
print(dob_unparsed)
dob_year = dob_unparsed[0:4]
print(dob_year)
dob_month = dob_unparsed[5:7]
print(dob_month)

# this is the birth_province and birth_place section
birth_location_unparsed = soup.find('p').contents[9]
print(birth_location_unparsed)
birth_province = birth_location_unparsed[0:2]
print(birth_province)
birth_place = birth_location_unparsed[2:4]
print(birth_place)

# this is the education section
education = soup.find('p').contents[13]
print(education)

# this is the ethnicity section
ethnicity_unparsed = str(soup.find('div', {'class': 'p2j_text'}).contents[1])
eth_cut = ethnicity_unparsed.split('，')
ethnicity = eth_cut[2]
print(ethnicity)




#this stuff is all for the top level page
'''
#initializes the dictionary
province_dict = {}

# extracts the list of provinces from the block on the left side of the page
# like on this page https://web.archive.org/web/20171221213907/http://ldzl.people.com.cn:80/dfzlk/front/personProvince1.htm
for entry in soup.find_all("div", {"class": "fl nav_left_2j"}):
    #breaks out each province list item
    for item in entry.find_all("li"):
        link = item.find('a').get('href')
        #there is no link for the Taiwan entry so this pulls it out to avoid an error
        if link == None:
            full_link = 'Taiwan.tw'
        #for the rest of the links, makes them a full URL
        else:
            full_link = 'https://web.archive.org' + link
        #extracts the name of the province
        province = item.get_text()
        #adds entry to the dictionary
        province_dict[province] = full_link

#cleans up the dictionary by removing renegade provinces
del province_dict['台湾省']
del province_dict['澳门特别行政区']
del province_dict['香港特别行政区']

#pprint(province_dict)
'''
#this will be the loop structure once you get it right
'''for province in province_dict:
    url = province_dict[province]
    province_page = requests.get(url)
    province_soup = BeautifulSoup(province_page.txt)'''

'''

url = province_dict['安徽省']
province_page = requests.get(url)
province_soup = BeautifulSoup(province_page.text, 'lxml')

prov_titles = []

#the titles are in the b
for item in province_soup.find_all('b'):
    item_text = item.text
    cleaned_item_text = item_text.replace("：", "")
    print(cleaned_item_text)
    print('*****')
    #adds the titles in order to the prov_titles list
    prov_titles.append(cleaned_item_text)

prov_people = {}
#the names and links to the person page
for item in province_soup.find_all('p'):
    for element in item.find_all('a'):
        link = element.get('href')
        name = element.get_text()
        prov_people[name] = link

print(prov_titles)
pprint(prov_people)
print("888888888888")
page = province_soup.find('p').get_text()
print(page)
page_list = []
page_list.append(page)
for item in page_list:
    item.replace(" ", "")
print(page_list)

'''
