from .app import app
from .scrapers import ScraperTask

scraper_task = ScraperTask()
app.tasks.register(scraper_task)
