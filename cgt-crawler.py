import urllib3
from bs4 import BeautifulSoup
import csv
import os
import re

class Crawl():
    def __init__(self, url):
        self.url = url

    def sriuba(self):
        http = urllib3.PoolManager()
        response = http.request('GET', self.url)
        return BeautifulSoup(response.data.decode('utf-8'))

    def title(self):
        return self.sriuba().title.string

    def price(self):
        return self.sriuba().find('span', class_='price').string

    def id(self):
        return self.sriuba().find('span', class_='product_id').string

    def polys(self):
        a = self.sriuba().findAll("ul", {"class": "details-box__list"})[1].findAll('span')[-7].string
        print ("=>", a)
        if a == None:
            return str(0)
        else:
            return a

    def name(self):
        return self.sriuba().find('span', class_='name').string

    def write_csv(self, items):
        fileName = "sarasas.csv"
        with open(fileName, "a") as f:
            f.write(items)

    def enumerate(self, number):
        pass

    def __regexSearch(self, title, regex):
        print("__regexSearch", title)
        print(re.search(regex, title))
        return re.search(regex, title).group(1)

    def add_commas(self, link):
        link = "{}".format(link)
        print(link)


links = ("""
put your links in here
""")
links = links.split("\n")
links = list(filter(bool, links))

number = int(165)
for l in links:
    crl = Crawl(l)
    crl.write_csv(str(number) + "\t" + l + "\t" + crl.id() + "\t" + crl.name() + "\t\t\t\t\t\t"+ crl.polys() + "\n")
    number += int(1)
