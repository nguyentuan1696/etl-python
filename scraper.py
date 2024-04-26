import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quote-spdier'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        quote_selector = '.quote'
        text_selector = '.text::text'
        author_selector = '.author::text'
        about_selector = '.author + a::attr("href")'
        tags_selector = '.tags > .tag::text'
        next_selector = '.next a::attr("href")'

        for quote in response.css(quote_selector):
            yield {
                'text': quote.css(text_selector).extract_first(),
                'author': quote.css(author_selector).extract_first(),
                'about': 'https://quotes.toscrape.com' +
                         quote.css(about_selector).extract_first(),
                'tags': quote.css(tags_selector).extract(),
            }

        next_page = response.css(next_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
            )