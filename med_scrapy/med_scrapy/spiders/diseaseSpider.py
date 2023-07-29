import scrapy


class DiseasespiderSpider(scrapy.Spider):
    name = "diseaseSpider"
    allowed_domains = ["www.mayoclinic.org"]
    start_urls = ["https://www.mayoclinic.org/diseases-conditions/index?letter=A"]

    def parse(self, response):
        working_url = str(response)[5:65]
        letter = ord(str(response)[65])

        diseases = response.css('div.cmp-result-name div.cmp-link')

        for  disease in diseases:
            yield {
                'name': disease.css('a::text').get(),
                'url' : disease.css('a').attrib['href']
            }
        if  letter < 90:
            new_char = chr(letter + 1)
            new_url =  working_url + new_char
            yield scrapy.Request(new_url, callback=self.parse)
        

