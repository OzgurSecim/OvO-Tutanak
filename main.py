from utils.scrape import DataScraper


if __name__ == '__main__':
    scraper = DataScraper(
        apiurl='https://api-sonuc.oyveotesi.org/api/v1/submission/school',
        referer='https://tutanak.oyveotesi.org/',
    )

    scraper(city=None, checkpoint=False)
