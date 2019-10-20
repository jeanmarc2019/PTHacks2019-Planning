import bs4 as bs
import urllib.request
import csv
import re


sauce = urllib.request.urlopen('http://www.city-data.com/crime/')
soup = bs.BeautifulSoup(sauce, 'lxml')
table = soup.table

states = soup.find("div", {"class": "col-md-6", "id": "tabs_by_category"})
for a in states.find_all("a", href = True):
    placeholder = str(a).split('"')
    print(placeholder[1])


