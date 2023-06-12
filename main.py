from get_yahoo_financials import YahooFinanceScraper


def main():
    x = YahooFinanceScraper("AAPL")
    x.yahoo_income_statement()

if __name__ == '__main__':
    main()

