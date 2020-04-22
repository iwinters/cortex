import scrapy
import cortex.items

class TrustRadius_Spider(scrapy.Spider):
    name = 'tr'
    start_urls = ['https://www.trustradius.com/products/vidyard/reviews?o=recent']
    download_delay = 1.5
   
    def parse(self,response):
        reviews = response.css('.serp-review')
        items = []

        for review in reviews:
            item = cortex.items.CortexItem()
            identities = review.css('.name *::text').getall()
            comments = str(review.css('.review-title *::text').get())
            paragraphs = review.css('.response *::text').getall()
            for paragraph in paragraphs:
                comments = comments + ' ; ' + str(paragraph)
            dates = review.css('.review-date *::text').get()
            #dates_uncleaned = review.css('.ReviewSource__HalfUnitMarginDiv-lnjke6-1 ::text')
            #for date_uncleaned in dates_uncleaned:
            #    if "20" in str(date_uncleaned.get()):
            #        dates = str(date_uncleaned.get())
            #    else:
            #        pass

            item['identities'] = identities
            item['comments'] = comments
            item['dates'] = dates
            item['source'] = 'TrustRadius'

            items.append(item)

        return items