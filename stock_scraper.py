import urllib.request
from bs4 import BeautifulSoup


def get_stock_tickers():
    req = urllib.request.Request(
        'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr'):
        col = row.findAll('td')
        if len(col) > 0:
            tickers.append(str(col[0].string.strip()))
    tickers.sort()
    return tickers


def get_stock_prices(ticker_list):
    for ticker in ticker_list:
        htmlfile = urllib.request.urlopen(
            "http://finance.yahoo.com/q?s={0}".format(ticker)
        )
        htmltext = htmlfile.read()
        soup = BeautifulSoup(htmltext, 'html.parser')
        htmlSelector = 'yfs_l84_{0}'.format(ticker.lower())
        for price in soup.find_all(id=htmlSelector):
            print('{0} is {1}'.format(ticker, price.text))

def print_stock_scraper_welcome_message():
    print('Welcome to my stock scraper.')
    print('--- We show stocks information here ---')

def main():
    all_tickers = get_stock_tickers()
    print_stock_scraper_welcome_message()
    get_stock_prices(all_tickers)


if __name__ == '__main__':
    main()
