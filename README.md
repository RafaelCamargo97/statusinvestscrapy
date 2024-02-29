# Status Invest Scrapy Spider
This is a simple Python project that retrieves stock indicators from a website using Scrapy.

# What does it do
This spider will utilize the website http:\\statusinvest.com.br to gather indicators for stocks of your choice listed on the Brazilian Stock Market (B3).
The information it retrieves includes: Stock Code, Price, Change(12m), D.Y (Dividend Yield), P/L (Price-to-Earnings Ratio), P/VP (Price-to-Book Ratio), ROE (Return on Equity), Stock Rental.

# How does it work
To use it, you need to input the codes of the stocks on the "lista_acoes.txt" file located at statusinvestscrapy/statusinvestscrapy/fIles. After that, you have to open a terminal on the root directory of the project and run the command "scrapy crawl buffetspider -o <FILE_NAME>", where the <FILE_NAME> is the path and name of the file you want use for the code output (json or csv).
If you want to follow the project's standardization, use the following example: `scrapy crawl buffetspider -o "statusinvestscrapy/files/indicadores.json"`

