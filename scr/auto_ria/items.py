# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class AutoRiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CarItem(Item):
    model = Field()
    year = Field()
    mileage = Field()
    usd_price = Field()
    uah_price = Field()
    vin_code = Field()
    link = Field()