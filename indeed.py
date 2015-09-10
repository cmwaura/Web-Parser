__author__ = 'crispus'

from bs4 import BeautifulSoup
import urllib2, json

dict = {}

def cleaner():
    url = "http://www.indeed.com/jobs?q=python+analyst&l=San+Francisco%2C+CA"

    site = urllib2.urlopen(url).read()

    objects = BeautifulSoup(site, "html.parser")
    # print objects.prettify()

    try:
        for object in objects.find_all("div", class_="  row  result"):
            try:
                for position in object.findAll("a", class_="turnstileLink"):
                    print "-"*100
                    Jobtitle = position.get_text()
                    dict["Jobtitle"] = Jobtitle
                    # print dict
                for companyname in object.findAll("span", class_="company"):
                    companyname = companyname.get_text()
                    dict["companyname"] = companyname
                    # print companyname

                for location in object.findAll("span", itemprop = "addressLocality"):
                    location = location.get_text()
                    dict["location"] = location
                    # print location

                for summary in object.findAll("span", class_="summary"):
                    Description = summary.get_text()
                    dict["Description"] = Description
                    # print Description

                # print dict
                go_to_file()

            except object.DoesNotExist:
                print "please check the initial HTML"

    except object.DoesNotExist:
        pass
        
def go_to_file():
    final_data = json.dumps(dict, ensure_ascii=False, sort_keys=True, indent=2)
    print "Json Data:", final_data

cleaner()
