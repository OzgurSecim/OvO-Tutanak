import json
import pandas as pd
import numpy as np


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

    def __call__(self, simple=True):
        if simple:
            '''
            '''
            stats = []
            cities = list(self.data['ilAdi'].unique())
            for city in cities:
                temp = self.data.loc[self.data['ilAdi'] == city]
                
                total_count, total_record = len(temp), np.sum(temp['tutanak'])
                
                district_count = pd.DataFrame(temp.groupby('ilceAdi')['tutanak'].count()).to_dict()
                district_record = pd.DataFrame(temp.groupby('ilceAdi')['tutanak'].sum()).to_dict()

                for key, value in district_count['tutanak'].items():
                    stats.append([city, total_record, total_count, total_record / total_count, key, district_record['tutanak'][key], value, district_record['tutanak'][key] / value])



            df = pd.DataFrame(stats, columns=['ilAdi', 'toplamSandik', 'toplamTutanak', 'tutanakOrani', 'ilceAdi', 'ilceToplamSandik', 'ilceToplamTutanak', 'ilceTutanakOrani'])
            df.to_csv('stats_simple.csv', index=False)

        else:
            '''
            '''
            pass