# Your code here

# task 1
# Given url not open in browser (it is not valid URL) therefore got output as Failed to send GET request
# I tried another URL then http_request function work properly.

import requests # import library

def http_request(): # define function 
    url = 'https://eoa0qzkprh8wd6s.m.pipedream.net' 
    response = requests.get(url)
    
    if response.status_code == 200:      # give the condition
        print('GET request successful')
        print(response.text)
    else:
        print(f'Failed to send GET request: Status Code {response.status_code}')

# Call the function to send the GET request
http_request()


import requests

def http_request():
    url = 'https://www.google.com/search?q=moneycontrol'
    response = requests.get(url)
    
    if response.status_code == 200:
        print('GET request successful')
        print(response.text)
    else:
        print(f'Failed to send GET request: Status Code {response.status_code}')

# Call the function to send the GET request
http_request()








# task 2
#curl -v -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" https://eo6f3hp6twlkn24.m.pipedream.net/






#Task 3
# import neccesory libreries
from datetime import datetime, timedelta
import calendar

#Define function
def first_day_last_week_in_current_month():
    current_date = datetime.now()
    # Get last day of the current month
    last_day_current_month = current_date.replace(day = 1, month = current_date.month +1) - timedelta(days=1)
    # calculate the date for the first day of the last week in the current month
    first_day_last_week = last_day_current_month - timedelta(days=last_day_current_month.weekday())
    # return and convert date in given formate
    return first_day_last_week.strftime("%Y-%m/%d")
print(first_day_last_week_in_current_month())









# task 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap






# task 5

class LoginMetaClass(type):
    pass


class AccessWebsite(metaclass=LoginMetaClass):
    logged_in = False

    def login(self, username, password):
        if username == "admin" and password == "admin":
            self.logged_in = True

    def access_website(self):
        return "Success"
