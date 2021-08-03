from os import write
from unicodedata import name
import requests
from bs4 import BeautifulSoup
import csv

#scraping table from wikipedia and stoing in a csv file

website = requests.get('https://www.knowafest.com/college-fests/events/2021/05/2705-wheedle-2021-amet-deemed-to-be-university-technical-symposium-chennai')

print(website)
