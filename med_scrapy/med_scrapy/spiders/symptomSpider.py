import scrapy


class SymptomspiderSpider(scrapy.Spider):
    name = "symptomSpider"
    allowed_domains = ["www.mayoclinic.org"]
    start_urls = ["https://www.mayoclinic.org/symptoms/index?letter=A"]

    def parse(self, response):
        working_url = str(response)[5:54]
        letter = ord(str(response)[-2])

        symptoms = response.css('div.index ol li')

        for  symptom in symptoms:
            yield {
                'name' : symptom.css('a::text').get(), 
                'url': 'https://www.mayoclinic.org/' + symptom.css('a').attrib['href'],
            }

        if  letter < 90:
            new_char = chr(letter + 1)
            new_url =  working_url + new_char
            yield scrapy.Request(new_url, callback=self.parse)

