import scrapy

class InfoSpider(scrapy.Spider):
    name = 'tesla_spider'
    #allowed_domains = ['auto.ria.com']
    start_urls = ['https://auto.ria.com/uk/legkovie/tesla/']



    def parse(self, response):
        for car in response.css('section.ticket-item'):
            model = car.css('div.hide::attr(data-model-name)').get()
            year = car.css('div.hide::attr(data-year)').get()
            mileage = car.css('li.item-char.js-race::text').get()
            #mileage.replace('тис','').replace('км','').strip()
            uah_price = car.css('span.i-block > span::text').get()
            usd_price = car.css('span.bold.green.size22::text').get()
            vin = car.css('span.label-vin > span::text').get()
            if vin == None:
                vin = 'Not mentioned'

            link = car.css('a.m-link-ticket::attr(href)').get()
           # model = car.css('span.blue-bold :: text').get()


            yield {
                'link' : link,
                'model' : model,
                'mileage' : mileage,
                'uah:price' : uah_price,
                'usd_price' : usd_price,
                'vin' : vin,
                'year' : year
            }

        next_page = response.css('a.page-link.js-next::attr(href)').get()
        if next_page != None:
            yield response.follow(next_page,callback=self.parse)

