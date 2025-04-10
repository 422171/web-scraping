import scrapy
from scrapy.crawler import CrawlerProcess
from collections import defaultdict

class Scraper1 (scrapy.Spider):
    name = 'scrape_quotes'
    
    def start_requests(self):
        urls = ['https://quotes.toscrape.com/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('Scraper1 scrapes quotes from: ', response.url)
        quotes = response.css('div.row > div.col-md-8 > div.quote')
        for quote in quotes:
            text = quote.css('span.text::text').extract_first().strip()
            author = quote.css('span small.author::text').extract_first().strip()
            tags = quote.css('div.tags a.tag::text').extract()
            quotes_by_author[author].append(text)
            for tag in tags:
                quotes_by_tag[tag.strip()].append(text)
        next_page = response.css('li.next > a::attr(href)').extract_first()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
        
def get_quotes_by_author(author):
    for key in quotes_by_author:
        if author.lower() in key.lower():
            print(f"Quotes by {key}:")
            quotes = quotes_by_author[key]
            for i,quote in enumerate(quotes):
                print(f"{i+1}: {quote}")
            return
        
def get_quotes_by_tag(tag):
    for key in quotes_by_tag:
        if tag.lower() in key.lower():
            print(f"Quotes about {key}:")
            quotes = quotes_by_tag[key]
            for i,quote in enumerate(quotes):
                print(f"{i+1}: {quote}")
            return
        
def write_quotes_by_author(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for key in quotes_by_author:
            f.write(f"Quotes by {key}:\n")
            quotes = quotes_by_author[key]
            for i,quote in enumerate(quotes):
                f.write(f"{i+1}: {quote}\n")
            f.write('\n')

def write_quotes_by_tag(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for key in quotes_by_tag:
            f.write(f"Quotes about {key}:\n")
            quotes = quotes_by_tag[key]
            for i,quote in enumerate(quotes):
                f.write(f"{i+1}: {quote}\n")
            f.write('\n')

quotes_by_author = defaultdict(list)
quotes_by_tag = defaultdict(list)
process = CrawlerProcess()
process.crawl(Scraper1)
process.start()

# get_quotes_by_author('Einstein')
# get_quotes_by_tag('choices')
write_quotes_by_author('quotes_by_author.txt')
write_quotes_by_tag('quotes_by_tag.txt')