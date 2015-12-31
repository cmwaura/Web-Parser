import re
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

class SalaryEstimates:

    def salary_parser(self, soup):

        rx = re.compile('([+(),])')
        print "---------------------------------------------------------------------------------"
        print "---------------------------------------------------------------------------------"
        print " ----------------------T-A-B-L-E-S-----------------------------------------------"
        print "---------------------------------------------------------------------------------"


        for post in soup.find_all("ul", {"class":"rbList"}):
            # return post
            figures = post.get_text(' ', strip=True)
            figures = list(rx.sub(r'', figures).replace(' ', ', ').split())

            quantity = [(elem).replace(',','') for elem in figures if '$' not in elem]

            salary = [(elem).replace('$', '').replace(',','') for elem in figures if '$' in elem]

            d = {'Salary from jobs': pd.Series(salary, index=['a', 'b', 'c','d','e']),
                 'Quantity': pd.Series(quantity, index=['a', 'b', 'c', 'd', 'e'])}
            self.df5 = pd.DataFrame(d)
            self.df5 = self.df5.apply(pd.to_numeric, errors='coerce')
            print self.df5
            df5_median =self.df5['Salary from jobs'].median()
            df5_mean = self.df5['Salary from jobs'].mean()

            print "The median for this job is:", df5_median
            print "The mean for this job is:", df5_mean
            return self.df5

    def graphing_salary(self, username, api_key):

            # username= "cmwaura"
            # api_key ="543mnm6vz9"

            tls.set_credentials_file(username=username, api_key=api_key)
            # for table in self.df5:
            data = [
                go.Scatter(
                    x=self.df5['Quantity'],
                    y=self.df5['Salary from jobs']

                )
            ]
            final_graph = py.plot(data, filename='pandas/basic-bar')
            # salary_graph = py.plot(data, filename='pandas/basic-bar', auto_open=False )
            return final_graph



