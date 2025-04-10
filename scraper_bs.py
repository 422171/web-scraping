from bs4 import BeautifulSoup
import requests

'''create a function that takes a url and returns the title of the page'''
def get_page_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.title.string if soup.title else 'No title found'

# print(get_page_title('https://www.google.com'))
# print(get_page_title('https://www.jcchouinard.com/web-scraping-with-beautifulsoup-in-python/'))
# print(get_page_title('https://stackabuse.com/guide-to-parsing-html-with-beautifulsoup-in-python/'))

def get_page_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_books(soup):
    books = soup.find_all('article', class_='product_pod')
    books_list = []
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        books_list.append({'title': title, 'price': price})
    return books_list

url = 'http://books.toscrape.com/'
soup = get_page_content(url)
books = extract_books(soup)

for book in books:
    print(f"Title: {book['title']}\nPrice: {book['price']}\n")