import scrapy
from datetime import datetime


class IndiaTodaySpider(scrapy.Spider):

    name = "IndiaToday"

    def start_requests(self):
        urls = [
            'https://www.indiatoday.in/topic/{}'.format(self.topic)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        news_urls = response.css(".field-content a::attr(href)").getall()
        open('test.txt', 'w').close()

        for url in news_urls:
            yield scrapy.Request(url=url, callback=self.parse_news)

    def parse_news(self, response):
        data = {}
        data["title"] = response.css("title::text").get()
        data["author"] = response.css(".title::text").get().strip()
        data["publisher"] = "India Today"

        stories = response.css(".description p::text").getall()
        stories = [s.strip() for s in stories]
        data["body"] = "".join(stories)

        date = response.css(".pubdata::text").get().strip()
        data["publishedOn"] = datetime.strptime(date, '%B %d, %Y').timestamp()

        data["storyUrl"] = response.url

        yield data
