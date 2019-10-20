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
    state = str(placeholder[1])
    print("State: " + str(placeholder[1]))
    sauce1 = urllib.request.urlopen(state)
    soup1 = bs.BeautifulSoup(sauce1, 'lxml')
    cities = soup1.find("ul", {"class": "index"})
    for city in cities.find_all("a", href = True):
        cityName = str(city).split('"')
        print("city: " + cityName[1])
        sauce2 = urllib.request.urlopen("http://www.city-data.com/crime/" + str(cityName[1]))
        soup2 = bs.BeautifulSoup(sauce2, 'lxml')
        crimeData = soup2.find("div", {"class": "table-responsive"})
        years = [2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
        count = 0

        while count < 8:
            index = 0
            crime = crimeData.find("tr", {"class": "g"+str(count)})
            for crimes in crime.find_all("small"):
                index = index + 1
                print("Crime Set #" + str(count) + " Index #" + str(index)+ ": " + str(crimes))
            count = count + 1
        




