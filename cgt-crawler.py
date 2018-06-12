import urllib3
from bs4 import BeautifulSoup
import csv
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
        a = self.sriuba().findAll("ul", {"class": "details-box__list"})[1].findAll('span')[9].string
        print ("=>", a)
        if a == None:
            return str(0)
        else:
            return a

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

    def strip(self, title):
        regex = re.compile(r'(?:^)(.*)((?:(?: 3D asset )|(?: 3D model )|( ))(?:\| CGTrader))')
        return self.__regexSearch(title,regex)


links = ()
number = int(80)

for l in links:
    
    crl = Crawl(l)
    #print(crl.id() + crl.strip(crl.title()) + "\t\t\t\t\t\t")
    #crl.write_csv(crl.strip(crl.title()) + "\n")
    crl.write_csv(str(number) + "\t" + l + "\t" + crl.id() + "\t" + crl.strip(crl.title()) + "\t\t\t\t\t\t"+ crl.polys() + "\n")
    number += int(1)
