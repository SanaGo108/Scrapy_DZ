import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class LightsnewSpider(scrapy.Spider):
    name = "lightsnew"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/podvesnye-svetilniki"]

    def parse(self, response):
        lights = response.css('_Ud0k U4KZV')
        for light in lights:
            yield {
                'name' : light.css('div.lsooF span::name').get(),
                'price' : light.css('div.pY3d2 span::text').get(),
                'url' : light.css('a').attrib['href']
            }