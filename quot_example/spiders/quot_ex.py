# -*- coding: utf-8 -*-
import scrapy

from quot_example.items import QuotExampleItem

class QuotExSpider(scrapy.Spider):
    name = 'quot_ex'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
	quote=response.xpath("//div[@class='quote']")
	for qut in quote:
	    text=qut.xpath(".//span[@class='text']/text()").extract_first()
	    author =qut.xpath(".//small//text()").extract_first()
	    link=qut.xpath(".//a[@class='tag']/text()").extract_first()

	    item=QuotExampleItem()
	    item['quote']=text
	    item["author"]=author
	    item["link_tag"]=link
	    print len(item)
	    
	    yield item
        next_page_url=response.xpath("//li[@class='next']//a/@href").extract_first()
        if next_page_url:
	   absolute_next_page_url=response.urljoin(next_page_url)
	   yield scrapy.Request(absolute_next_page_url)
 
	  
        
