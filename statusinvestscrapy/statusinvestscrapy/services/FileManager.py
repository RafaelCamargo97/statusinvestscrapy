import os


class FileManager:

    def read_stock_list(self):
        stock_list_dir = os.getcwd()

        stock_list_path = os.path.join(stock_list_dir, 'statusinvestscrapy\\files\\lista_acoes.txt')

        with open(stock_list_path, 'r') as file:
            stocks = file.readlines()
            stocks = [stock.strip() for stock in stocks]

        return stocks
