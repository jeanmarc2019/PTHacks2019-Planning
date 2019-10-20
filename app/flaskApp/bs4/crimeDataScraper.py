import bs4 as bs
import urllib.request
import csv
import re

f = open("StateCrimeData.csv", 'w')
 


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

        tempCityName = str(cityName[1])
        finalCityName = tempCityName.split("-")
        finalCityName.remove("crime")
        s = " "
        tempCityName = s.join(finalCityName)
        finalCityName = str(tempCityName).split(".")
        finalCityName.remove("html")
        s = " "
        tempCityName = s.join(finalCityName)
        finalCityName = tempCityName.split(" ")
        CityOfficalName = ""
        OfficialStateName = str(finalCityName[-1])
        print("state: " + str(finalCityName[-1]))
        if len(finalCityName) ==3:
            CityOfficalName = str(finalCityName[0]) + "-" + str(finalCityName[1])
        else:
            CityOfficalName = str(finalCityName[0])

        print("City Name: " + CityOfficalName)


        ##print("city: " + cityName[1])
        sauce2 = urllib.request.urlopen("http://www.city-data.com/crime/" + str(cityName[1]))
        soup2 = bs.BeautifulSoup(sauce2, 'lxml')
        crimeData = soup2.find("div", {"class": "table-responsive"})
        years = [0000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
        crimeAverages = []
        count = 0

        crime = crimeData.find("tfoot", {"class": "g8"})
        for crimes in crime.find_all("td"):
            tempCrime = str(crimes).split(">")
            finalCrimeChart = str(tempCrime[1])
            tempCrime = str(finalCrimeChart).split("<")
            finalCrimeChart = str(tempCrime[0])
            ##print("The Average crime rate is: 280.6 the cities crime rate for " + str(years[count]) + " is : " + str(finalCrimeChart)) 
            crimeAverages.append(str(finalCrimeChart))
        f.write("state:")
        f.write(OfficialStateName + "\n")
        f.write("city:")
        f.write(CityOfficalName + "\n")
        tempcount = 1
        while tempcount < len(crimeAverages):
            f.write("year:" + str(years[tempcount]) + ",crimerate:" + str(crimeAverages[tempcount])+"\n")
            tempcount = tempcount + 1

        """thewriter.writerow({"Types" : crimeAverages[0], "2003" : crimeAverages[1], "2004" : crimeAverages[2], "2005" : crimeAverages[3], "2006" : crimeAverages[4],
        "2007" : crimeAverages[5], "2008" : crimeAverages[6], "2009" : crimeAverages[7], "2010" : crimeAverages[8], "2011" : crimeAverages[9],
        "2012" : crimeAverages[10], "2013" : crimeAverages[11], "2014" : crimeAverages[12], "2015" : crimeAverages[13], "2016" : crimeAverages[14], 
        "2017" : crimeAverages[15]})"""



        
        """ while count < 8:
            index = 0
            crime = crimeData.find("tr", {"class": "g"+str(count)})
            for crimes in crime.find_all("small"):
                try:
                    index = index + 1
                    ##print("Crime Set #" + str(count) + " Index #" + str(index)+ ": " + str(crimes))
                    placeholderCrimeData = str(crimes).split("(")
                    s = ""
                    ##print(str(placeholderCrimeData))
                    crimeDataNum = str(placeholderCrimeData[1])
                    ##print(crimeDataNum)
                    placeholderCrimeData = crimeDataNum.split(")")
                    crimeDataNum = str(placeholderCrimeData[0])
                    print("Crime Set #" + str(count) + " Index #" + str(index)+ ": " + str(crimeDataNum))
                except:
                    print(0.0)
                    pass
            count = count + 1
        """
f.close()
    




