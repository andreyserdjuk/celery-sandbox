from celery import Celery
from .settings import BACKEND, BROKER
from kombu import Exchange, Queue

app = Celery('scraper',
             broker=BROKER,
             backend=BACKEND)

exchange = Exchange('scrap-ex', type='direct')

app.conf.update(
    task_routes={
        'scraper_task': {'queue': 'scraping', 'routing_key': 'get_page_content'},
    },
    task_queues=(
        Queue('scraping', exchange, routing_key='get_page_content'),
    )
)

