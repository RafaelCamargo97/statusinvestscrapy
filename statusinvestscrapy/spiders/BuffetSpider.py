import scrapy
from statusinvestscrapy.services import FileManager as fm


class BuffetSpiderSpider(scrapy.Spider):
    name = "buffetspider"
    allowed_domains = ["statusinvest.com.br"]
    start_urls = []

    def stocks_to_be_read(self):
        file = fm.FileManager().read_stock_list()

        for stock in file:
            url = "".join(["https://statusinvest.com.br/acoes/", stock])
            self.start_urls.append(url)

    def start_requests(self):
        self.stocks_to_be_read()
        for url in self.start_urls:
            yield scrapy.Request(url= url, callback=self.parse)

    def parse(self, response):
        stock_indicators = response.css(".value.d-block.lh-4.fs-4.fw-700::text").getall()
        stock_price = response.css("strong.value::text").getall()
        stock_rental = response.css("strong.m-md-0.mb-md-1.value.mt-0::text").get()
        stock_name = response.css("a.fw-900.active::text").get()
        yield {
            'Stock': stock_name,
            'Price': stock_price[0],
            'Change(12m)': stock_price[4],
            'D.Y': stock_indicators[0],
            'P/L': stock_indicators[1],
            'P/VP': stock_indicators[3],
            'ROE': stock_indicators[24],
            'Rental': stock_rental + "%"
        }
