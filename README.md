# Web Scraping

A collection of Python scripts for web scraping using BeautifulSoup and Scrapy. This project includes examples for scraping quotes and books, along with utilities for organizing and exporting data.

## Functionalities

- **Scrape Quotes**: Extract quotes, authors, and tags from [Quotes to Scrape](https://quotes.toscrape.com/) using Scrapy.
- **Scrape Books**: Extract book details such as title, price, rating, category, and availability from [Books to Scrape](http://books.toscrape.com/) using Scrapy and BeautifulSoup.
- **Data Organization**: Organize scraped data by author or tag and export it to text files.
- **Utilities**: Functions to fetch page titles and extract book details using BeautifulSoup.

## Requirements

- Python 3.x
- Required Python libraries:
  - `scrapy`
  - `beautifulsoup4`
  - `requests`

Install the required libraries using:
```bash
pip install scrapy beautifulsoup4 requests
```

## Usage

### Scraping Quotes
1. Run the `scrape_quotes.py` script to scrape quotes from [Quotes to Scrape](https://quotes.toscrape.com/).
2. The script organizes quotes by author and tag and exports them to `quotes_by_author.txt` and `quotes_by_tag.txt`.

```bash
python scrape_quotes.py
```

### Scraping Books
1. Use `scrape_books.py` to scrape book details from [Books to Scrape](http://books.toscrape.com/).
2. Choose between two modes:
   - **Basic Mode**: Scrape title, price, rating, and link.
   - **Detailed Mode**: Scrape additional details like category, description, and availability.

```bash
python scrape_books.py
```

### Using BeautifulSoup
1. Use `scraper_bs.py` for simple web scraping tasks like fetching page titles or extracting book details.

```bash
python scraper_bs.py
```

## Background

These projects were inspired by a DataCamp course on web scraping in Python, which focused on Scrapy. I expanded on this foundation by independently exploring BeautifulSoup for additional web scraping tasks.

## File Descriptions

- **`scrape_quotes.py`**: Scrapy spider for scraping quotes and organizing them by author and tag.
- **`scrape_books.py`**: Scrapy spider for scraping book details in basic or detailed mode.
- **`scraper_bs.py`**: Utility script using BeautifulSoup for simple scraping tasks.
- **`quotes_by_author.txt`**: Output file containing quotes organized by author.
- **`quotes_by_tag.txt`**: Output file containing quotes organized by tag.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project. I would love to collaborate!!

## License

This project is licensed under the MIT License.
