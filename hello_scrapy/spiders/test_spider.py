import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["www.pornstargalore.com"]
    start_urls = [
    	"http://www.runoob.com/python3/python3-tutorial.html",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
