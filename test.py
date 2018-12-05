from secret import movie_db_api_key
import requests
import json
from bs4 import BeautifulSoup
import sqlite3
import csv
from datetime import datetime, timedelta

######################### CLASS DEFINITION #########################
class BoxOffice():
    def __init__ (self, ranking, title, title_id, date):
        self.ranking = ranking,
        self.title = title,
        self.title_id = title_id,
        self.date = date


class BoxOfficeInfo():
    def __init__ (self, title, title_id, daily, theater, whole, date):
        self.title = title,
        self.title_id = title_id
        self.daily = daily,
        self.theater = theater,
        self.whole = whole,
        self.date = date


class MovieInfo():
    def __init__ (self, poster, title, title_id, runtime, release, genre, overview, starring = [], picture = []):
        self.poster = poster
        self.title = title
        self.title_id = title_id
        self.runtime = runtime
        self.release = release
        self.genre = genre
        self.overview = overview
        self.starring = starring
        self.picture = picture

######################### CACHE DATA #########################
CACHE_FNAME = "cache.json"
try:
    cache_file = open(CACHE_FNAME, "r")
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def get_unique_key(url):
    return url

def make_request_using_cache(url):
    unique_ident = get_unique_key(url)

    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making a request for new data...")
        resp = requests.get(url)
        CACHE_DICTION[unique_ident] = resp.text 
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]


######################## GET BOX OFFICE DATA #########################
def get_box_office(date):
    url = 'https://www.boxofficemojo.com/daily/chart/?view=1day&sortdate='
    url_full = url + date

    page_text = make_request_using_cache(url_full)
    page_soup = BeautifulSoup(page_text, "html.parser")  

    title_list = []
    query_list = []
    res_title = []
    res = []
    daily_gross_list = []
    whole_gross_list = []
    date_list = []
    theater_list = []

    result_list = []


    ###### Title List #######
    site_div = page_soup.find_all("font")
    for i in range(len(site_div)):
        title = site_div[i].find('a')
        if (title != None):
            title = site_div[i].find('a').string
            res_title.append(title)


    for i in range(16, 36):
        if i % 2 == 1:
            title_list.append(res_title[i])
    print(title_list)
    title = []

    # site_div = page_soup.find_all("td")
    # for i in range(len(site_div)):
    #     title = site_div[i].find('font', attrs={"size":"2"})
    #     if (title != None):
    #         title = site_div[i].find('font', attrs={"size":"2"})
    #         res.append(title)


    # index = 19
    # # for k in range(len(res)):
    # #     test_title = res[i].find('a').string()
    # #     print(test_title)

    # for i in range(10):
    #     b = str(res[index])
    #     a = b.replace('<b>', "")
    #     a = a.replace("</b>", "")
    #     a = a.replace('<font size="2">', "")
    #     a = a.replace("</font>", "")
    #     query_list.append(a)
    #     index = index + 11
    # # print(query_list)

    # for i in range(len(query_list)):
    #     print(query_list[i].find('a')['href'])
    #     # print(test)

    # ###### Daily Gross #######
    # index = 21
    # for i in range(10):
    #     b = str(res[index])
    #     a = b.replace('<b>', "")
    #     a = a.replace("</b>", "")
    #     a = a.replace('<font size="2">', "")
    #     a = a.replace("</font>", "")
    #     daily_gross_list.append(a)
    #     index = index + 11
    # # print(daily_gross_list)

    # ###### Theater #######
    # index = 24
    # for i in range(10):
    #     b = str(res[index])
    #     a = b.replace('<b>', "")
    #     a = a.replace("</b>", "")
    #     a = a.replace('<font size="2">', "")
    #     a = a.replace("</font>", "")
    #     theater_list.append(a)
    #     index = index + 11
    # # print(theater_list)


    # ###### Whole Gross #######
    # index = 26
    # for i in range(10):
    #     b = str(res[index])
    #     a = b.replace('<b>', "")
    #     a = a.replace("</b>", "")
    #     a = a.replace('<font size="2">', "")
    #     a = a.replace("</font>", "")
    #     whole_gross_list.append(a)
    #     index = index + 11
    # # print(whole_gross_list)

    # ###### Date #######
    # index = 27
    # for i in range(10):
    #     b = str(res[index])
    #     a = b.replace('<b>', "")
    #     a = a.replace("</b>", "")
    #     a = a.replace('<font size="2">', "")
    #     a = a.replace("</font>", "")
    #     date_list.append(a)
    #     index = index + 11
    # print(date_list)



    # for i in range(10):
    #     result = BoxOfficeInfo(title=query_list[i], title_id = '',daily=daily_gross_list[i], theater=theater_list[i], whole=whole_gross_list[i], date=date_list[i])
    #     result_list.append(result)
    #     # print(query_list[i])

    # return result_list

get_box_office('2018-11-28')
