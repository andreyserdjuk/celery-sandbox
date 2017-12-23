from celery import Task
# import requests
from typing import AnyStr
import time


class ScraperTask(Task):
    name = 'scraper_task'

    def run(self, url):
        return self.get_content(url)

    def get_content(self, url: AnyStr):
        # return requests.get(url).text
        print('scraping {}'.format(url))
        return 'content from {}'.format(url)
