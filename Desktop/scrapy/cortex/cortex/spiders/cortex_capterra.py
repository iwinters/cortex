#bugs:
#if comment field is blank, two commas from script in a row
#if identities field is blank, "none"

#realized that sites including G2 and Chrome store block scrapers, decided it's not worth pursuing if it only gathers from a couple sites


import json
import scrapy

class Capterra_Spider(scrapy.Spider):
    name = 'capterra'
    base_url = 'https://www.capterra.com/spotlight/rest/reviews?apiVersion=2&productId=125653&from=%s'
    page = 0
    start_urls = [base_url%page]
    download_delay = 1.5
 
    def parse(self, response):
        data = json.loads(response.body)
        page = 0
        for item in data.get('hits', []):
            yield {
                'Comments': str(item.get('title')) + ' ; ' + str(item.get('generalComments')) + ' ; ' + str(item.get('prosText')) + ' ; ' + str(item.get('consText')),
                'Identities': str(item.get('reviewer', {}).get('fullName')) + ', ' + str(item.get('reviewer', {}).get('jobTitle')) + ', ' + str(item.get('reviewer', {}).get('companyName')),
                'Dates': item.get('writtenOn'),
                'Source': "Capterra"
            }
        
        if data.get('totalHits') > (page + 50):
            next_page = page + 50
            yield scrapy.Request(self.base_url%next_page)
            # https://blog.scrapinghub.com/2016/06/22/scrapy-tips-from-the-pros-june-2016