import json
import pandas as pd


class StatsCalculator:
    def __init__(self, load_csv=True):
        self._get_data(load_csv)
        
    def _get_data(self, load_csv):
        if load_csv:
            self.data = pd.read_csv('data.csv', low_memory=False)
        else:
            with open('data.json', 'r') as f:
                data = json.load(f)
            
            to_df = []
            for city, district_data in data.items():
                for district, valuelist in district_data.items():
                    for value in valuelist:
                        to_df.append([
                            city, district, value['neighborhood'], value['school'], value['ballot_box_number'], value['record'], value['image_url'], \
                            value['oy_erdogan'], value['oy_kilicdaroglu']
                        ])

            self.data = pd.DataFrame(to_df, columns=['ilAdi', 'ilceAdi', 'mahalleAdi', 'okulAdi', 'sandikNo', 'tutanak', 'url', 'RECEP TAYYİP ERDOĞAN', 'KEMAL KILIÇDAROĞLU'])
            self.data.to_csv('data.csv', index=False)