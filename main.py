from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()

quotes = Scraper()

@app.get("/quote")

def quote(cat):
    return quotes.scrapedata(cat)
