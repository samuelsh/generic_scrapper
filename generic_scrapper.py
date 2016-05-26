from urllib2 import urlopen, URLError, HTTPError
from bs4 import BeautifulSoup


class Scrapper(Exception):
    def __init__(self, url):
        self.url = url
        self.bs = None
        try:
            self.page = urlopen(self.url).read()
        except (URLError, HTTPError) as urlerr:
            raise RuntimeError(urlerr.message)
        self.bs = BeautifulSoup(self.page, 'html.parser')

    def print_html(self):
        print(self.bs.prettify())

    def print_text(self):
        print(self.bs.get_text())

    def find_all(self, node):
        self.bs.find_all(node)
