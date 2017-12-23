from .app import app
from .scrapers import ScraperTask
# import os


st = ScraperTask()

# abspath = os.path.abspath('app/download.xml')
# d = feedparser.parse(abspath)

for e in range(10):
    st.delay('url-{}'.format(e))
