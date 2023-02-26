# Lab 10c

# Use the Scrapy library
import scrapy


class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.80/index.html']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {'Image Link': x.xpath(newsel).extract_first(), }

        # To recurse next page
        page_selector = '.next a ::attr(href)'
        next_page = response.css(page_selector).extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

# Test scrapytest.py
#   Terminal: scrapy runspider scrapytest.py
# Save the output to a file results.json
#   Terminal: scrapy runspider scrapytest.py -o results.json -t json