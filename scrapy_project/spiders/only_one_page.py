from scrapy.crawler import CrawlerRunner
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy_project.check_seo import Check
from scrapy_project.items import Only_one_pages, QuestionItem
import scrapy
from scrapy_project.text_analyze import *
Ch = Check()


class Only_one_page_spider(scrapy.Spider):
    name = "only_one_page_spider"
    handle_httpstatus_list = [404, 500]
    start_urls = ["https://dulevo.ru"]
    allowed_domains = ["mail.ru"]
    url = ''



    def parse(self, response):
        item = QuestionItem()
        for quote in response.css('html'):
            counters_anal = quote.css('script').extract()
            if 'https://www.google-analytics.com/analytics.js' in str(counters_anal):
                yee = 'Есть'
            else:
                yee = 'Нет'
            if 'mc.yandex.ru/metrika' in str(counters_anal):
                res = 'Есть'
            else:
                res = 'Нет'
            social = quote.css('a').extract(),
            if 'www.vk.com' in social:
                vk_stat = 'Есть'
            else:
                vk_stat = 'Нет'
            if 'facebook.com' in social:
                fb_stat = 'Eсть'
            else:
                fb_stat = 'Нет'
            if 'instagram.com' in social:
                insta_stat = 'Есть'
            else:
                insta_stat = 'Нет'
            urls = response.url

            title = quote.css('title::text').extract_first(),

            item['base_url'] = self.allowed_domains[0]
            item['title'] = Ch.check('title', title)
            description = quote.css(
                'meta[name*=description]::attr(content), meta[name*=Description]::attr(content)').extract(),
            h1 = quote.css('h1::text').extract(),
            h2 = quote.css('h2::text, H2::text').extract(),
            item['description'] = Ch.check('description', description)
            item['h1'] = Ch.check('h1', h1)
            item['h2'] = Ch.check('h2', h2)
            keyword = quote.css(
                'meta[name*=Keywords]::attr(content), meta[name*=keywords]::attr(content)').extract(),
            item['keyword'] = Ch.check('keywords', keyword)
            item['description_unique'] = description
            item['title_unique'] = title
            item['link'] = response.url
            item['broken_link'] = response.status
            item['img'] = len(quote.css('img').extract())
            text = quote.css('body').extract()
            item['alt'] = most_common(text)
            item['vk'] = vk_stat,
            item['facebook'] = fb_stat,
            item['instagram'] = insta_stat,
            item['googl_anal'] = yee,
            item['text'] = round(len(response.body) / 1024, 1),
            item['yandex_metrick'] = res,
            return item


    def get_url(self, url, short_url):
        self.start_urls.clear()
        self.allowed_domains.clear()
        self.url=url
        self.allowed_domains.append(short_url)
        self.start_urls.append(url)