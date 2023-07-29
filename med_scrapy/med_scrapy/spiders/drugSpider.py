import scrapy


class DrugspiderSpider(scrapy.Spider):
    name = "drugSpider"
    allowed_domains = ["www.mayoclinic.org"]
    start_urls = ["https://www.mayoclinic.org/drugs-supplements/drug-list?letter=A"]

    def parse(self, response):
        working_url = str(response)[5:67]
        letter = ord(str(response)[-2])

        drugs = response.css('div.index ol li')

        for  drug in drugs:
            yield {
                'name' : drug.css('a::text').get(), 
                'url': 'https://www.mayoclinic.org/' + drug.css('a').attrib['href'],
            }

        if  letter < 90:
            new_char = chr(letter + 1)
            new_url =  working_url + new_char
            yield scrapy.Request(new_url, callback=self.parse)
