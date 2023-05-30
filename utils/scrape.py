import json
import requests
import time
import random
from tqdm.auto import tqdm


class DataScraper:
    def __init__(
            self,
            apiurl: str,
            referer: str,
            ):
        # OvO API URL
        self.url = apiurl
        # Headers for requests
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Referer': referer,
            'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

        with open('meta/meta.json', 'r') as f1, open('meta/keypairs.json', 'r') as f2:
            self.meta, keys = json.load(f1), json.load(f2)

        self.key2city, self.city2key = {}, {}
        for key, name in keys:
            self.key2city[key], self.city2key[name] = name, key

    def __call__(
            self,
            city: str = None,
            checkpoint: bool = True,
            ):
        if city is not None:
            targets = [self.city2key[city]]
            filename = f"data_{city.lower()}.json"
        else:
            targets = [str(x) for x in range(1, 83)]
            filename = 'data.json'

        if checkpoint:
            with open(filename, 'r') as f:
                data = json.load(f)
        else:
            data = {}
        
        # Iterate cities
        count = 0
        pbar = tqdm(targets, desc=f"Scraping OvO data - Status Code = {None} - Counter = 0")
        for target in pbar:
            meta = self.meta[target]
            
            if self.key2city[target] in data:
                temp = data[self.key2city[target]]
            else:
                temp = {}

            # Iterate districts
            for dist, dmeta in meta.items():
                if dist in temp:
                    continue
                temp[dist] = []

                # Iterate neighborhoods
                for neigh, nmeta in dmeta.items():
                    # Iterate schools
                    for sch, value in nmeta.items():
                        url = f"{self.url}/{value}"

                        status_code = 0
                        response = requests.get(url, headers=self.headers)
                        status_code = response.status_code
                        pbar.set_description(f"Scraping OvO data - Status Code = {status_code} - Counter = {count}")
                        while status_code != 200:
                            time.sleep(random.uniform(0.2, 1))
                            response = requests.get(url, headers=self.headers)
                            status_code = response.status_code
                            pbar.set_description(f"Scraping OvO data - Status Code = {status_code} - Counter = {count}")
                        response = response.json()
                        count += 1
                        pbar.set_description(f"Scraping OvO data - Status Code = {status_code} - Counter = {count}")

                        temp[dist] += [
                            {
                                'neighborhood': neigh,
                                'school': sch,
                                'ballot_box_number': ballot['ballot_box_number'],
                                'record': ballot['cm_result'] is not None,
                                'image_url': ballot['cm_result']['image_url'] if ballot['cm_result'] is not None else None,
                                'oy_erdogan': ballot['cm_result']['votes']['1'] if ballot['cm_result'] is not None else None,
                                'oy_kilicdaroglu': ballot['cm_result']['votes']['2'] if ballot['cm_result'] is not None else None,
                            } for ballot in response
                        ]

                        time.sleep(random.uniform(0, 1))

                # Checkpoint
                data[self.key2city[target]] = temp
                with open(filename, 'w') as f:
                    f.write(json.dumps(data, indent=4, ensure_ascii=False))
 