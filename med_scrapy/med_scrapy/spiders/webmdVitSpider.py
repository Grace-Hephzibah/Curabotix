import scrapy


class WebmdvitspiderSpider(scrapy.Spider):
    name = "webmdVitSpider"
    allowed_domains = ["www.webmd.com"]
    start_urls = ["https://www.webmd.com/vitamins/alpha/a"]

    def parse(self, response):
        working_url = str(response)[5:42]
        letter = ord(str(response)[-2])

        vits = response.css('div.vitamins-search-list-conditions ul li')

        for  vit in vits:
            yield {
                'name': vit.css('a::text').get(),
                'url' : 'https://www.webmd.com/' + vit.css('a').attrib['href']
            }
        if  letter < 122: 
            new_char = chr(letter + 1)
            new_url =  working_url + new_char 
            yield scrapy.Request(new_url, callback=self.parse)
