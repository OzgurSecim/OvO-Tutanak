# OvO-Tutanak

## Data on Cloud

### Election - 28 May 2023

[data.json (version 0)](https://drive.google.com/file/d/1Oz5A8R7ELbIl3rUtpLyGNsLNJhPWjb68/view?usp=sharing)

[data.csv (version 0)](https://drive.google.com/file/d/1Ze3uaQybedMyMbhWETedbmKCtGtIbqQD/view?usp=sharing)

[stats_simple.csv (version 0)](https://drive.google.com/file/d/1Ox5jBq6T2YXyYe5QQJHUylGUAccUcWue/view?usp=sharing)

### Election - 14 May 2023

[data_may14.csv (version 2)](https://drive.google.com/file/d/1J-xZT5Gy5wsT7G2yLUjDPZk0k1ESRWYW/view?usp=sharing)

## Environment Setup

You can install requirements with the following command:

    conda env create -n ovo --file environment.yml

You can activate the environment with the following command:

    conda activate ovo

## Data Scraping

You can obtain data from OvO API with the following command:

    python main.py

It is possible to obtain data of a specific city by changing `city` argument in `main.py`. Please see `meta/keypairs.json` before giving the name of the city as the argument.

## Statistical Analysis

You can convert the data to **.csv** format and infer statistics with the following command:

    python stats.py