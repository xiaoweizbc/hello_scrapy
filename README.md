# 说明
###创建项目
```
scrapy startproject hello_scrapy
```
###定义Item
#####编辑hello_scrapy目录中的 items.py 文件:
```
import scrapy

class HelloScrapyItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
```
###编写第一个爬虫(Spider)
#####以下为我们的第一个Spider代码，保存在 hello_scrapy/spiders 目录下的 test_spider.py 文件中:
```
import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
```
###爬取
#####1.进入项目的根目录，执行下列命令启动spider:
```
scrapy crawl test
```
#####2.用python运行文件start.py
```
python start.py
```