#python3

from bs4 import BeautifulSoup
import requests
from pprint import pprint

#this is the top level url
#top_url = 'https://web.archive.org/web/20171221213907/http://ldzl.people.com.cn:80/dfzlk/front/personProvince1.htm'


#variables for db writing
title = ''

##############################################################
#############THIS IS THE CITY PAGE STUFF####################
##############################################################
'''
#meta TODO (11/11): As I am writing these todos, I do not know how much of them have already been done in the code below

#TODO 1 (11/11): There are two people at the top of the page. You need 4 pieces of information about them: 1. name, 2. url, 3. where they are in the order (rank_peer), 4. how many people total.  Most of this is probably in the <em> tags. For example: <em class=""><a href="personPage4314.htm">宋国权</a></em>

#TODO 2 (11/11): There is a chart at the bottom of the page with three columns. The first column is county, the second is official #1, and the third is official #2.  You need 1. name of county, 2. URL of county, 3. name of dude (each), 4. url of dude, 5. rank_peer of dude, 6. how many people total.  Most of this is probably in: this is the only <ol class="fl"> on the page. within this <ol>, find each <li> (or <span>, if that's somehow easier).

city_url = 'https://web.archive.org/web/20171004155730/http://ldzl.people.com.cn/dfzlk/front/chengqu1029.htm'

city_page = requests.get(city_url)
city_soup = BeautifulSoup(city_page.text, 'lxml')

#for entry in city_soup.find_all('ul', {'class':'clearfix ld'}):
count = 1
for entry in city_soup.find_all('em', {'class' : ''}):
    print("entry: " + str(entry))

city_unparsed = city_soup.find_all('em', {'class' : ''})
#turns the first url into a string and then extracts it
city_url_nub_1 = str(city_unparsed[1]).split('"')[3]
#city_url1a = str(city_url1).split('"')[3]
city_url_full_1 = 'https://web.archive.org/web/20171004155730/http://ldzl.people.com.cn/dfzlk/front/' + city_url_nub_1

print("city_url_full_1:" + city_url_full_1)

'''
##############################################################
#############THIS IS THE PERSON PAGE STUFF####################
##############################################################
def person():

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

    # this is the picture section
    img_url_unparsed = str(soup.find('img', {'id': 'userimg'}))
    img_url_end = img_url_unparsed.split('"')[7]
    img_url = 'https://web.archive.org' + img_url_end
    print(img_url)
    #I assume this will be a dynamically created variable
    url_save_file_name = 'guy.jpg'
    #uses requests to download the picture
    image_r = requests.get(img_url, allow_redirects=True)
    #writes the downloaded picture to the file
    open(url_save_file_name, 'wb').write(image_r.content)

    #this is the data dump
    data_dump = soup.find('div', {'class', 'p2j_text'})
    print(data_dump)

person()
##############################################################
#############THIS IS THE PROVINCE PAGE STUFF####################
##############################################################
#this stuff is all for the top level page

# TODO 1 (11/11) Get the province name (it is the only H1 on the page)

# TODO 2 (11/11) For the people listed with pictures AND the people listed in the next two sections (no pictures - these are the p tags), you need 1. name, 2. URL, 3. rank_peer, 4. peer total.  After doing that, dedupe via url (becuase 2 people may have the same name) and re-rank (if the same guy was #1 and #2, he becomes just #1 and the original #3 dude becomes #2.

# TODO 3 (11/11) There is a chart at the bottom of the page with city + official 1 + official 2 (sometimes the chart wraps around itself so it looks like 6 things, but it is really just 3).  From this chart you only need 1. city name, and 2. city URL. Here's how jessica said to do it: this is the only <ol class="fl"> on the page. within this <ol>, find each <li> (or <span>, if that's somehow easier), and use the first href after that tag.  There are 2 other hrefs in each <li>, but we don't need them for our purposes in this loop.

'''
#initializes the dictionary
province_dict = {}

# extracts the list of provinces from the block on the left side of the page
# like on this page https://web.archive.org/web/20171224064640/http://ldzl.people.com.cn:80/dfzlk/front/personProvince1028.htm
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
