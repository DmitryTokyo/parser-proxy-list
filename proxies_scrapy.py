import time
import logging
import os
import json
import requests
import re
from urllib.parse import urljoin

from environs import Env
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from tqdm import tqdm

logging.basicConfig(format="%(process)d %(levelname)s %(message)s", level=logging.INFO)

env = Env()
env.read_env()

HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }


def get_countries_url(response, proxies_urls):
    soup = bs(response, 'lxml')
    links_tag = soup.find_all(href=re.compile('proxys'))

    country_links = {}
    for link_tag in links_tag:
        country_code = link_tag['href'].strip('/proxys/')
        full_path = urljoin(proxies_urls, country_code)
        country = (link_tag.text).split(' ')[0]
        if country_code != '':
            country_links[country] = f'{full_path}/'
    
    return country_links


def get_proxies(countries_proxies_url, driver):
    proxies_countries = {}
    for country in tqdm(countries_proxies_url):
        driver.get(countries_proxies_url[country])
        
        try:
            select = Select(driver.find_element_by_name('xpp'))
            select.select_by_value('5')
            time.sleep(3)

            proxies = driver.find_elements_by_xpath('//tr[@onmouseover]/td[1]')
            proxies_countries[country] = [proxy.text for proxy in proxies]

        except Exception as err:
            logging.exception(err)

    driver.quit()
    return proxies_countries


def save_to_json(filename, proxies):

    with open(filename, 'w') as file:
        json.dump(proxies, file)
    
    print('Done...')


def main():
    countries = 'http://spys.one/proxys/'
    free_proxies_url = 'http://spys.one/free-proxy-list/'
    proxies_filename = env('PROXY_FILE')

    response = requests.get(countries, headers=HEADERS)
    response.raise_for_status()
    countries_urls = get_countries_url(response.text, free_proxies_urls)

    driver = webdriver.Chrome(executable_path = env('PATH_TO_DRIVER'))
    proxies = get_proxies(countries_urls, driver)
    
    save_to_json(proxies_filename, proxies)


if __name__ == "__main__":
    main()
