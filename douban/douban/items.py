# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movieName = scrapy.Field()
    rate = scrapy.Field()
    director=scrapy.Field()
    actors=scrapy.Field()
    genres = scrapy.Field()
    country=scrapy.Field()
    language=scrapy.Field()
    initialReleaseDate=scrapy.Field()
    runtime=scrapy.Field()
    imdbLink=scrapy.Field()
