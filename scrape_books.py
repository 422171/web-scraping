import scrapy
from scrapy.crawler import CrawlerProcess
from collections import defaultdict

books_list = []
# total_books = 0
# page2 = True

class Scraper2_1(scrapy.Spider):
    name = 'scraper_books_1'

    def start_requests(self):
        urls = ['http://books.toscrape.com/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_short(self, response):
        '''
        global books_list: list of dictionaries
        only deals with the catalogue pages.
        each resultant book is a dictionary with keys: title, link, rating, price
        '''
        books = response.css('article.product_pod')

        for book in books:
            title = book.css('h3 a::attr(title)').extract_first()
            link = 'http://books.toscrape.com/catalogue/'+book.css('h3 a::attr(href)').extract_first().replace('catalogue/', '')
            rating = book.css('p.star-rating::attr(class)').extract_first().replace('star-rating ', '')
            price = book.css('p.price_color::text').extract_first()
            books_list.append({'title': title, 'link': link, 'rating': rating, 'price': price})

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page:
            yield response.follow(next_page, self.parse_short)
    
class Scraper2_2(scrapy.Spider):
    name = 'scraper_books_2'
    
    def start_requests(self):
        urls = ['http://books.toscrape.com/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_long)
    def parse_long(self, response):
        '''
        global books_list: list of dictionaries
        deals with the catalogue pages, and then redirects to each book's main page.
        each resultant book is a dictionary with keys: title, link, rating, price, category, description, availability
        '''
        books = response.css('article.product_pod')

        for book in books:
            link = 'http://books.toscrape.com/catalogue/'+book.css('h3 a::attr(href)').extract_first().replace('catalogue/', '')
            yield response.follow(link, self.parse_book)
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page:
            yield response.follow(next_page, self.parse_long)
    
    def parse_book(self, response):
        title = response.css('h1::text').extract_first()
        price = response.css('p.price_color::text').extract_first()
        availability = response.css('td::text').extract()[-2].strip()
        rating = response.css('p.star-rating::attr(class)').extract_first().replace('star-rating ', '')
        description = response.css('article.product_page p::text').extract_first()
        category = response.css('ul.breadcrumb li:nth-of-type(3) a::text').extract_first()
        if(category == 'Default'):
            category = "Miscellaneous"
        books_list.append({'title': title, 'link': response.url, 'rating': rating, 'price': price,'category': category, 'description': description, 'availability': availability})



def get_books(start_index, end_index):
    for i in range(start_index, end_index+1):
        book = books_list[i]
        print(f"Book {i+1}:\nTitle: {book['title']}\nPrice: {book['price']}\nRating: {book['rating']}\nLink: {book['link']}")

def get_books_2(start_index, end_index):
    for i in range(start_index, end_index+1):
        book = books_list[i]
        print(f"Book {i+1}:\nTitle: {book['title']}\nPrice: {book['price']}\nRating: {book['rating']}\nLink: {book['link']}\nCategory: {book['category']}\nDescription: {book['description']}\nAvailability: {book['availability']}")

process = CrawlerProcess()
# process.crawl(Scraper2_1)
process.crawl(Scraper2_2)
process.start()
print(f"Total books: {len(books_list)}")
print("1st 30 books:")
# get_books(0, 29)
get_books_2(0, 29)