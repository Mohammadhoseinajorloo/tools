import argparse

class Parser:
    def __init__(self):
       self.__parser = argparse.ArgumentParser(description='serial tools')
       self.__parser.add_argument("-l", type=str, default=2, help="fide download links")

    def return_download_link_arg(self):
        args = self.__parser.parse_args() 
        return args.l
