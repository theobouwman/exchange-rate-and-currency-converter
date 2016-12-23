# Theo Bouwman
# Check currency stock exange rated by just one command

import sys
import optparse
import urllib.request
import json

# all available currencies
currencies = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP',
'KHD', 'HRK', 'HUF', 'IDR', 'IRL', 'INR', 'JPY', 'KRW', 'MXN', 'MYR',
'NOK', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY',
'ZAR', 'EUR', 'USD']


# class for colored strings
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


# currency class to talk to api
class Currency:
    url = 'http://api.fixer.io'
    currency = None

    def __init__(self, currency):
        self.currency = currency

    # fetch currencies by currency
    def getLatestByCurrency(self):
        url = self.url + '/latest?base=' + self.currency
        response = urllib.request.urlopen(url).read().decode('utf-8')
        data = json.loads(response)

        print(bcolors.OKGREEN + 'Base: ' + data['base'] + bcolors.ENDC + '\n')

        # loop through currencies
        for key in data['rates']:
            value = data['rates'][key]

            # USD and EUR are the most asked currencies
            if key == 'EUR' or key == 'USD':
                print(bcolors.OKBLUE)
                print('%s = %s'%(key, value))
                print(bcolors.ENDC)
            else:
                print('{} = {}'.format(key, value))

    # get rates by 2 currencies
    def getBySymbols(self, symbols):
        # split on comma
        splitted = symbols.split(',')

        # check 2 parameters
        if len(splitted) < 2 or len(splitted) > 2:
            sys.exit(bcolors.FAIL + '2 currencies required.' + bcolors.ENDC)

        # check is currency is valid
        for currency in splitted:
            if currency not in currencies:
                sys.exit(bcolors.FAIL + currency + ' is not a valid currency' + bcolors.ENDC)

        url = self.url + '/latest?symbols=' + splitted[0] + ',' + splitted[1]
        response = urllib.request.urlopen(url).read().decode('utf-8')
        data = json.loads(response)

        print(bcolors.OKGREEN + 'Base: ' + data['base'] + bcolors.ENDC + '\n')

        # loop throush results
        for key in data['rates']:
            value = data['rates'][key]
            print('{} = {}'.format(key, value))


def main():
    # add parameters
    p = optparse.OptionParser()
    p.add_option('--list', '-l', default=None)
    p.add_option('--currency', '-c', default="eu")
    p.add_option('--symbols', '-s', default=None)
    options, arguments = p.parse_args()

    # list of available currencies
    if options.list is not None:
        print(bcolors.OKGREEN + 'List of available currencies')
        print('--currency OR -s <CURRENCY>' + bcolors.ENDC)
        for c in currencies:
            print(c)

        sys.exit()

    api = Currency(options.currency)
    if options.symbols is None:
        if options.currency not in currencies:
            sys.exit('Not a valid currency')

        api.getLatestByCurrency()
    else:
        api.getBySymbols(options.symbols)


if __name__ == '__main__':
    main()
