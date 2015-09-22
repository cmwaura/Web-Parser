__author__ = 'crispus'

from bs4 import BeautifulSoup

import urllib2
import us

contest = {}


class Parser:
    def __init__(self, Jobtitle, Description):
        self.Jobtitle = Jobtitle
        self.Description = Description
        # self.state_symbol=
    def cleaner(self):
        city_choice = raw_input(" Please choose the city you would like to search ")
        city_choice = city_choice.capitalize().split()
        locality = "+".join(city_choice)
        question = raw_input("Do you know the initial of the state you are looking for? [y/n] " )

        if question == "n" or question == "N":

            print "-"*200
            print "here is a list of all the states"
            states = us.states.mapping('abbr', 'name')
            print states
            state_symbol = raw_input("please choose your state [initials only] ")

        elif question  == "y"or question == "Y":

            state_symbol = raw_input("please choose your state [initials only] ")

            url = "http://www.indeed.com/jobs?q=python+analyst&l="+ locality +"%2C+"+ state_symbol + "&start=0"
    
            site = urllib2.urlopen(url).read()
    
            objects = BeautifulSoup(site, "html.parser")
            # print objects.prettify()
    
            try:
                for object in objects.find_all("div", class_="  row  result"):
                    try:
                        for position in object.findAll("a", class_="turnstileLink"):
                            print "-"*100
                            self.Jobtitle = position.get_text()
    
                        # for link in object.findAll("a", class_="jobtitle turnstileLink"):
                        #     self.Links = link.get('href')
    
                        for companyname in object.findAll("span", class_="company"):
                            self.companyname = companyname.get_text()
    
    
                        for location in object.findAll("span", itemprop = "addressLocality"):
                            self.location = location.get_text()
    
    
                        for summary in object.findAll("span", class_="summary"):
                            self.Description = summary.get_text()
    
                        context = {
                                "Jobtitle": self.Jobtitle,
    
                                "Location": self.location,
                                "CompanyName": self.companyname,
                                "Description":self.Description
                                   }
                        print context
    
                    except object.DoesNotExist:
                        print "please check the initial HTML"
    
            except object.DoesNotExist:
                pass

        else:
            print "you chose the wrong key"

parser = Parser("Jobtitle", "Description")
cleaner = parser.cleaner()
