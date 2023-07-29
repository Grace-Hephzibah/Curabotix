import scrapy


class WebmddrugspiderSpider(scrapy.Spider):
    name = "webmdDrugSpider"
    allowed_domains = ["www.webmd.com"]
    start_urls = ["https://www.webmd.com/drugs/2/alpha/a"]

    def parse(self, response):
        working_url = str(response)[5:41]
        letter = ord(str(response)[-2])

        drugs = response.css('div.drugs-search-list-conditions ul li')

        for  drug in drugs:
            yield {
                'name': drug.css('a::text').get(),
                'url' : 'https://www.webmd.com/' + drug.css('a').attrib['href']
            }
        if  letter < 122: 
            new_char = chr(letter + 1)
            new_url =  working_url + new_char 
            yield scrapy.Request(new_url, callback=self.parse)
