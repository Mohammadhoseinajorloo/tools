#!/usr/bin/env python3

from bs4 import BeautifulSoup
from exception import (ArgvException , 
                       ResponseExeption, 
                       UrlException,
                       EmptySeasonException,
                       EmptyEpisodeException,
                      )
from parser import Parser
from tqdm import tqdm
import os, re, requests, sys 

FILE = "/home/mohammad/links.txt"

def checkURL(str):
    regex= 'http[s]?:\/\/.*'
    checkURL= re.findall(regex,str)
    if checkURL:
       return True 
    return False 

def request_to_page(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.findAll("a")[1:]
    raise ResponseExeption(f'Response invalid.response={r.status_code}')

def save_links(links):
    with open(FILE, 'w+') as f:
         for link in links:
            f.write(f'{link}\n')
    print(f'ok.done')
           
def main():
    if len(sys.argv) < 2:
        raise ArgvException("Please enter serial name")
    baseurl = 'https://sjdcbjhdbscjbhsdjcbjsd.sjdcbjddbcsjhbsbjhcjbsdjshcdcjbsdsj.buzz/xG3m/Serial/'
    if checkURL(baseurl):
        parser = Parser()
        name_serial = parser.return_download_link_arg()
        URL = baseurl + name_serial
        episods = []
        seasons_links = request_to_page(URL)
        if len(seasons_links) == 0:
            raise EmptySeasonException(f"in this file season not exist.seasons={seasons_links}") 
        for season in seasons_links:
            episode_links = request_to_page(os.path.join(URL, season['href']))
            if len(episode_links) == 0:
                raise EmptyEpisodeException(f"in this file episode not exist.episodes={episode_links}") 
            for episode in episode_links:
                season_and_episode = os.path.join(season['href'], episode['href'])
                complate_url = os.path.join(URL, season_and_episode)                     
                episods.append(complate_url)
        save_links(episods)
    else:
        raise UrlException(f'URL is not present.url = {baseurl}')
           

if __name__ == "__main__":
    main()
