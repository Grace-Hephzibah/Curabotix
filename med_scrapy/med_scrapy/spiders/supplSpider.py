import scrapy


class SupplspiderSpider(scrapy.Spider):
    name = "supplSpider"
    allowed_domains = ["www.mayoclinic.org"]
    start_urls = ["https://www.mayoclinic.org/drugs-supplements"]

    def parse(self, response):
        base_url = 'https://www.mayoclinic.org/'
        meds = response.css('div.sub div.p-12 ul li')

        for med in meds:
            yield {
                'name': med.css('a span::text')[1].get(), 
                'link' : base_url + med.css('a').attrib['href']
            }