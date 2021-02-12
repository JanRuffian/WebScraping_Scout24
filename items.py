import scrapy


class Scout24Item(scrapy.Item):

    model = scrapy.Field()
    data = scrapy.Field()
    price = scrapy.Field()
    km = scrapy.Field()
    # PS = scrapy.Field()
    # Benzin = scrapy.Field()
    # Schaltung = scrapy.Field()
