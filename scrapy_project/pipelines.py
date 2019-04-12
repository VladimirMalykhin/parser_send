# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from questions.models import (Questions, Results)
from scrapy_project.check_seo import Check
import datetime


class ScrapyProjectPipeline(object):
    def process_item(self, item, spider):
        #if item['title']:
         #   self.result[item['link']] = item['title']
          #  self.resultkey[item['link']] = item['keyword']
       # if item['description']:
        #    self.resultdesc[item['link']] = item['description']
       # resultlink.append(item["link"])
       # self.resulth1[item['link']] = item['h1']
       # self.resulttext[item['link']] = item['text']
       # self.resultgoogl[item['link']] = item['googl_anal']
        date_add = datetime.date.today()

        title=item['title']

        if item['keyword'] is not None:
            keywords = item['keyword']

        else:
            keywords = 'Ошибок нет'

        if item['description'] is not None:
            descriptions = item['description']

        else:
            descriptions = 'Ошибок нет'

        if item['h1'] is not None:
            h1 = item['h1']

        else:
            h1 = 'Ошибок нет'

        if item['googl_anal'] is not None:
            google = item['googl_anal']

        else:
            google = 'Ошибок нет'

        if item['h2'] is not None:
            h2 = item['h2']

        else:
            h2 = 'Ошибок нет'

        if item['yandex_metrick'] is not None:
            yandex = item['yandex_metrick']

        else:
            yandex = 'Ошибок нет'

        vk = item['vk']
        facebook = item['facebook']
        instagram = item['instagram']
        broken_link = item['broken_link']
        base_url = item['base_url']
        title_unique = item['title_unique']

        desc_unique = item['description_unique']


        #results = Results(base_url=base_url, title=title, url=item['link'], keywords=keywords,
         #                    description=descriptions,
         #                    h1=h1, h2=h2,google=google,yandex=yandex,date_add=date_add)
        results = Results(base_url=base_url, title=title, url=item['link'], keywords=keywords,
                          description=descriptions, title_unique=title_unique,description_unique=desc_unique,
                          h1=h1, h2=h2, vk=vk, facebook=facebook, instagram=instagram, google=google,
                          yandex=yandex, broken_link=broken_link, date_add=date_add)
        results.save()
        return item



