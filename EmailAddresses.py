####################################################################
#EmailAddresses.py
#Gets all the email addresses from the web
###################################################################
import logging
import os
import pandas as pd
import re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from googlesearch import search

def main():
    logging.getLogger('scrapy').propagate=False

#return url (links) 
def get_urls(tag,n,language):
    urls=[url for url in search(tag,top=n,lang=language)]
    return urls

class MailSpider(scrapy.Spider):
    name='email'

    def parse(self,response):
        links=LsmlLinkExtractor(allow=()).extract_links(response)
        links=[str(link.url) for link in links]
        links.append(str(response.url))

        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_link)

    def parse_link(self,response):
        return 
