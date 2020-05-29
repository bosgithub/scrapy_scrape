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

#####################################################################
# individual_rest_name
individual_rest_name = rest[4].div.div.div.div.div.div.div.div.div.div.div.a.img["alt"]
print(individual_rest_name)


# individual_rest_star
star = rest[4].findAll("span", {
                       "class": "lemon--span__373c0__3997G display--inline__373c0__3JqBP border-color--default__373c0__3-ifU"})
overall_star_rating = star[0].div.get('aria-label')
overall_star_rating


# retrieve name of restauraunt
i = 3
while (i+1) < len(rest):
    i = i + 1
    for rest_name in rest:
        rest_name = rest[i].div.div.div.div.div.div.div.div.div.div.div.a.img["alt"]
    print("top ten pho restauraunt name are : ", rest_name)
    for rest_star in rest:
        rest_star = rest[i].findAll("span", {
            "class": "lemon--span__373c0__3997G display--inline__373c0__3JqBP border-color--default__373c0__3-ifU"})[0].div.get('aria-label')
    print("top ten pho restauraunt rating starts are : ", rest_star)


####################################################################
# go into sub links for individual restauraunt

# rest[4] retrieves the first restauraunt's branch link.
# concate with yelp main page to get restauraunt url for this branch

url = rest[4].find("span", {
                   "class": "lemon--span__373c0__3997G text__373c0__2Kxyz text-color--black-regular__373c0__2vGEn text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--inherit__373c0__2fB3p"})
rest_link = "https://www.yelp.ca" + url.a['href']

# loop to make a sub link list which contain all individual rest_link

sub_link = []
rest_link = "https://www.yelp.ca" + rest[i].find("span", {
    "class": "lemon--span__373c0__3997G text__373c0__2Kxyz text-color--black-regular__373c0__2vGEn text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--inherit__373c0__2fB3p"}).a['href']
i = 3
while (i+1) < len(rest):
    i = i + 1
    for rest_link in rest:
        rest_link = "https://www.yelp.ca" + rest[i].find("span", {
            "class": "lemon--span__373c0__3997G text__373c0__2Kxyz text-color--black-regular__373c0__2vGEn text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--inherit__373c0__2fB3p"}).a['href']
    sub_link.append(rest_link)
print(sub_link)


# connect to individual restauraunt site, read url
Clients = []
pages = []
for link in sub_link:
    Clients = req(link)
    pages = Clients.read()
    Clients.close()

# parse html with bs4
page_soup = soup(pages, 'html.parser')

print(len(page_soup))

##################################################################
# review date
date_of_review = page_soup.find("span", {
                                "class": "lemon--span__373c0__3997G text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa-"})
date_of_review = date_of_review.text

####################################################################
# reivew text

review = page_soup.find(
    "p", {"class": "lemon--p__373c0__3Qnnj text__373c0__2Kxyz comment__373c0__3EKjH text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-"})
review = review.text

####################################################################
# reivew star
individual_review_star = page_soup.find("div", {
    "class": "lemon--div__373c0__1mboc i-stars__373c0__1T6rz i-stars--regular-4__373c0__2YrSK border-color--default__373c0__3-ifU overflow--hidden__373c0__2y4YK"})
individual_review_star = individual_review_star['aria-label']

###################################################################
# run loop to get all info
# for contain in container:
#coin = contain.a['title']
#title_contain = contain.findAll('a', {'class': 'cmc-link'})
#price = title_contain[1].text
# daily_change_contain = contain.findAll(
#    'div', {'class': 'cmc--change-positive'})
#daily_change = daily_change_contain[0].text
#
#
#print('coin: ' + coin)
#print('price: ' + price)
#print('daily_change: ' + daily_change)
