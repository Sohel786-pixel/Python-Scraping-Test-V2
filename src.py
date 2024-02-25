
# task 1
import json
import gzip
with gzip.open(r"C:\Users\sohel\Downloads\categories.json.gz", mode="rt") as f:
    data = f.read()
print(data)


def parse_categories():
    categories = []

    def get_categories_recursive():
        pass

    get_categories_recursive()
    return categories






#task 2
#Start by setting up a Python project using the below commands to create a scrapy-project directory 
#and initialize a Python virtual environment.
#mkdir scrapy-project
#cd scrapy-project
#python -m venv env
#Activate the environment. 
#On Windows, run: env\Scripts\activate.ps1

# install scrapy using !pip install scrapy
# import scrapy

import scrapy

class WoolworthsSpider(scrapy.Spider):
    name = 'woolworths'
    allowed_domains = ['woolworths.com.au']
    start_urls = ['https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas']

    def parse(self, response):
        # Extract breadcrumb
        breadcrumb = response.css('div.breadcrumb-container ul.breadcrumb li a::text').getall()

        # Extract product names
        product_names = response.css('div.product-tile div.product-tile-inner span.product-name::text').getall()

        # Create items
        for product_name in product_names:
            item['product_name'] = product_name
            item['breadcrumb'] = breadcrumb
            yield item

