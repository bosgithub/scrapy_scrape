"""
Yelp web scraper: scrapes below information from yelp's
top 10 pho restauraunt:
1. restauraunt name
2. star rating: the the numerical value of the rating
3. date published: the date when the review was published
4. review: review text

"""

# load library
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
import time
import csv
import pdb


# site
my_url = 'https://www.yelp.ca/search?find_desc=pho&find_loc=Toronto%2C+ON&ns=1'


# connect to site, read url
Client = req(my_url)
page_html = Client.read()
Client.close()


# parse html with bs4
page_soup = soup(page_html, 'html.parser')


# for each restauraunt
rest = page_soup.findAll(
    "li", {"class": "lemon--li__373c0__1r9wz border-color--default__373c0__3-ifU"})


# go to individual restauraunt url
url = rest[4].find("span", {
                   "class": "lemon--span__373c0__3997G text__373c0__2Kxyz text-color--black-regular__373c0__2vGEn text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--inherit__373c0__2fB3p"})
rest_link = "https://www.yelp.ca" + url.a['href']


# store individual restauraunt link in a list
sub_link = []

rest_link = "https://www.yelp.ca" + rest[4].find("span", {
    "class": "lemon--span__373c0__3997G text__373c0__2Kxyz text-color--black-regular__373c0__2vGEn text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--inherit__373c0__2fB3p"}).a['href']

i = 3
while (i+1) < len(rest):
    i = i + 1
    for rest_link in rest:
        rest_link = "https://www.yelp.ca" + rest[i].find("span", {
            "class": "lemon--span__373c0__3997G text__373c0__2Kxyz text-color--black-regular__373c0__2vGEn text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--inherit__373c0__2fB3p"}).a['href']
    sub_link.append(rest_link)


###################################################################
# open csv file
# let csv writter start

f = open("anynomous_rest.csv", "w")
writer = csv.writer(f, delimiter=',')

# go into each restauraunt link
# parse with soup
for link in sub_link:
    # test with one link
    # link = sub_link[0]
    Client = req(link)
    page_html = Client.read()
    page_soups = soup(page_html, 'html.parser')
    main_class = page_soups.findAll("div", {"class": "hidden"})
    for i in main_class:

        # rating = soup.find('meta', itemprop = 'ratingValue').get('content')   # helped by mel <3

        rest_name = i.findAll("meta", {"itemprop": "name"})
        for i in rest_name[:10]:
            print(i.attrs['content'])
            #writer.writerow([i.attrs['content'], date_of_review, individual_review_star, review])

        rest_date = i.findAll('meta', itemprop='datePublished')
        for m in rest_date[:10]:
            print(m.attrs['content'])

        rest_star = i.findAll('meta', itemprop='ratingValue')
        for j in rest_star[:10]:
            print(j.attrs['content'])

        reviews = i.findAll("p", {"itemprop": "description"})
        for k in reviews[:10]:
            print(k.text)
            writer.writerow(
                [i.attrs['content'], m.attrs['content'], j.attrs['content'], k.text])

f.close()
Client.close()


print("***********************************************************************\
******************************************************************************\
******************************************************************************\
Hi sir! this is Bo. The last pho restauraunt only has 3 reviews, but \
I will try some other stores to make sure to get 100 rows of data \
for second part of this assignment.\
Professor Hyalmar, thank you for your help! You are the best! <3")
