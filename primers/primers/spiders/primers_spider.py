import scrapy


class Primers_Spider(scrapy.Spider):
    name = "primers"

    def start_requests(self):
        urls = [
            'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for item in response.css("div#Div1.product"):

            status=True
            if item.css('span.out-of-stock::text').get()=="Out of Stock":
                status=False

           
    
            
            yield{
                #To remove '$' from the Price, slice the string
                'price':float(item.css('span.price').css('span::text').get()[1:]),
                'title':item.css('a.catalog-item-name::text').get(),
                'status':status,
                'manufacturer':(item.css('a.catalog-item-brand::text').get()).strip()
                }
