from secret import movie_db_api_key
import requests
import json
from bs4 import BeautifulSoup
import sqlite3
import csv
from datetime import datetime, timedelta
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

    date_input = date
    date_criteria = '2018-11-28'

    date_input = datetime.strptime(date_input, "%Y-%m-%d")
    date_criteria = datetime.strptime(date_criteria, "%Y-%m-%d")

    ###### Title List #######
    site_div = page_soup.find_all("font")
    for i in range(len(site_div)):
        title = site_div[i].find('a')
        if (title != None):
            title = site_div[i].find('a').string
            res_title.append(title)

    for i in range(16, 36):
        if date_input < date_criteria:
            if i % 2 == 0:
                title_list.append(res_title[i])
        else:
            if i % 2 ==1:
                title_list.append(res_title[i])

    for k in title_list:
        if "Dr. Seuss'" in k:
            k = "The Grinch"

        if "The Girl in the Spider's Web: A New Dragon Tattoo Story" in k:
            k = "The Girl in the Spider's Web"

        if "TCM: Die Hard 30th Anniversary Event" in k:
            k = "TCM Presents: Die Hard 30th Anniversary"

        if "Disney's Christopher Robin" in k:
            k = "CHRISTOPHER ROBIN"

        if "PERFECT BLUE (2018 RE-RELEASE)" in k:
            k = "Perfect blue"

        if "Princess Mononoke - Studio Ghibli" in k:
            k = "Princess Mononoke"

        if "&AMP" in k:
            res_title = k.replace('&AMP', '&')
            k = res_title

        if "(" in k:
            res_title = k.find("(")
            cleaned = k[:res_title-1]
            k = cleaned
            query_list.append(k)
        else:
            query_list.append(k)

    # print(url_full)
    # print(query_list)


    site_div = page_soup.find_all("td")
    for i in range(len(site_div)):
        title = site_div[i].find('font', attrs={"size":"2"})
        if (title != None):
            title = site_div[i].find('font', attrs={"size":"2"})
            res.append(title)
    # print(res)

    ###### Daily Gross #######
    if date_input < date_criteria:
        index = 39
    else:
        index = 21

    for i in range(10):
        b = str(res[index])
        a = b.replace('<b>', "")
        a = a.replace("</b>", "")
        a = a.replace('<font size="2">', "")
        a = a.replace("</font>", "")
        daily_gross_list.append(a)
        index = index + 11
    # print(daily_gross_list)

    ###### Theater #######
    if date_input < date_criteria:
        index = 42
    else:
        index = 24    

    for i in range(10):
        b = str(res[index])
        a = b.replace('<b>', "")
        a = a.replace("</b>", "")
        a = a.replace('<font size="2">', "")
        a = a.replace("</font>", "")
        theater_list.append(a)
        index = index + 11
    # print(theater_list)

    ###### Whole Gross #######
    if date_input < date_criteria:
        index = 44
    else:
        index = 26    
    for i in range(10):
        b = str(res[index])
        a = b.replace('<b>', "")
        a = a.replace("</b>", "")
        a = a.replace('<font size="2">', "")
        a = a.replace("</font>", "")
        whole_gross_list.append(a)
        index = index + 11
    # print(whole_gross_list)

    ###### Date #######
    if date_input < date_criteria:
        index = 45
    else:
        index = 27    
    for i in range(10):
        b = str(res[index])
        a = b.replace('<b>', "")
        a = a.replace("</b>", "")
        a = a.replace('<font size="2">', "")
        a = a.replace("</font>", "")
        date_list.append(a)
        index = index + 11
    print(date_list)

    for i in range(10):
        result = BoxOfficeInfo(title=query_list[i], title_id = '',daily=daily_gross_list[i], theater=theater_list[i], whole=whole_gross_list[i], date=date_list[i])
        result_list.append(result)
        # print(query_list[i])

    return result_list

# get_box_office('2018-07-23')



######################### CACHE DATA #########################
CACHE_FNAME = "cache_moviedb.json"
try:
    cache_file = open(CACHE_FNAME, "r")
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def params_unique_combination(url, params):
    alphabetized_keys = sorted(params.keys())
    res = []
    for k in alphabetized_keys:
        res.append("{}-{}".format(k, params[k]))
    return url + "_".join(res)


def make_movie_request_using_cache(url, params):
    unique_ident = params_unique_combination(url,params)

    if unique_ident in CACHE_DICTION:
        # print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        # print("Making a request for new data...")
        resp = requests.get(url, params=params)
        CACHE_DICTION[unique_ident] = resp.text 
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]


######################## THE MOVIE DB #########################
def get_movie_id():
    url = 'https://api.themoviedb.org/3/search/movie'
    params = {}
    params['api_key'] = movie_db_api_key 
    params['language'] = 'en-US'
    params['page'] = 1

    res_list = []
    query_list = []

    res_list = (get_box_office(date))
    for i in res_list:
        i.title = str(i.title)
        i.title = i.title.replace('(', '')
        i.title = i.title.replace(')', '')
        i.title = i.title.replace('"', '')
        i.title = i.title.replace(',', '')
        i.title = i.title.replace("'", '')
        query_list.append(i.title)
    # print(query_list)

    movie_id_list = []

    for k in query_list:
        params['query'] = k
        text_search_movies = make_movie_request_using_cache(url, params)
       # print(text_search_movies)
        text_search_movies = json.loads(text_search_movies)['results'][0]
        movie_id_list.append(str(text_search_movies['id']))
    # print(movie_id_list)
    return movie_id_list



def get_movie_info():
    id_list = get_movie_id()

    full_result_list = []
    full_starring_list = []
    compact_result = []
    res_starring = []
    res_starring_pic = []
    compact_starring = []
    compact_starring_pic = []


################## Get the full information #################
    for k in id_list:
        url = 'https://api.themoviedb.org/3/movie/'
        params = {}
        params['api_key'] = movie_db_api_key 
        params['language'] = 'en-US'
        url += k    
        text_search_movies = make_movie_request_using_cache(url, params)
        text_search_movies = json.loads(text_search_movies)
        full_result_list.append(text_search_movies)


################## Get the starring information #################
    for k in id_list:
        url = 'https://api.themoviedb.org/3/movie/'
        params = {}
        params['api_key'] = movie_db_api_key 
        params['language'] = 'en-US'
        url += k 
        url += '/credits'
        text_search_movies = make_movie_request_using_cache(url, params)
        text_search_movies = json.loads(text_search_movies)['cast']
        full_starring_list.append(text_search_movies)

    for k in range(10):
        for v in range(5):
            try:
                res_starring.append(full_starring_list[k][v]['name'])
                res_starring_pic.append(full_starring_list[k][v]['profile_path'])
            except:
                pass

    for k in range(0, 50):
        if k % 5 == 0:
            compact_starring.append(res_starring[k:k+5])
            compact_starring_pic.append(res_starring_pic[k:k+5])

#    print(compact_starring_pic)


################## Compact Information for the future use #################

    for i in range(len(full_result_list)):
        try:
            poster = full_result_list[i]['poster_path']
            title = full_result_list[i]['title']
            title_id = id_list[i]
            runtime = full_result_list[i]['runtime']
            release = full_result_list[i]['release_date']
            genre = full_result_list[i]['genres'][0]['name']
            overview = full_result_list[i]['overview']
            overview = str(overview)
            starring = compact_starring[i]
            picture = compact_starring_pic[i]
        except:
            pass

        res = MovieInfo(poster = poster,
                        title = title,
                        title_id = title_id,
                        runtime = runtime,
                        release = release,
                        genre = genre,
                        overview = overview,
                        starring = starring,
                        picture = picture)
        compact_result.append(res)


    # for i in range(len(compact_result)):
    #     print(compact_result[i].overview)

    return compact_result

# get_movie_info()

def create_csv():
    res_list = []
    res_list = get_movie_info()
    title_id_list = []
    title_id_list = get_box_office(date)
    temp = []
    title_criteria = []
    title2_criteria = []
    date_criteria = []


    with open('movie_info.csv', 'a', newline = '') as csvfile:
        fieldnames = ['poster', 'title', 'title_id', 'runtime', 'release', 'genre', 'overview', 'starring', 'picture']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        with open('movie_info.csv', 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)

            for i in range(len(your_list)):
                title_criteria.append(your_list[i][1])

        for i in res_list:
            temp.append(i.title_id)            
            if not i.title in title_criteria:
                try:
                    writer.writerow({'poster': i.poster, 'title': i.title, 'title_id': i.title_id, 'runtime':i.runtime, 'release': i.release, 'genre': i.genre, 'overview': i.overview, 'starring': i.starring, 'picture': i.picture})
                except:
                    i.overview = ''
                    writer.writerow({'poster': i.poster, 'title': i.title, 'title_id': i.title_id, 'runtime':i.runtime, 'release': i.release, 'genre': i.genre, 'overview': i.overview, 'starring': i.starring, 'picture': i.picture})



    with open('boxoffice.csv', 'a', newline = '') as csvfile:
        fieldnames = ['ranking', 'title', 'title_id', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        with open('boxoffice.csv', 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)

            for i in range(len(your_list)):
                date_criteria.append(your_list[i][3])

        ranking_index = 1
        for i in res_list:
            if not date in date_criteria:
                writer.writerow({'ranking': ranking_index, 'title': i.title, 'title_id': i.title_id, 'date': date})
                ranking_index += 1


    for i in range(10):
        title_id_list[i].title_id = temp[i]

    with open('boxoffice_info.csv', 'a', newline = '') as csvfile:
        fieldnames = ['title', 'title_id', 'daily', 'theater', 'whole', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        with open('boxoffice_info.csv', 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)

            for i in range(len(your_list)):
                title2_criteria.append(your_list[i][0])

        ranking_index = 1
        for i in title_id_list:
            i.title = str(i.title)
            i.title = i.title.replace('(', '')
            i.title = i.title.replace(')', '')
            i.title = i.title.replace(',', '')
            i.title = i.title.replace('"', '')
            i.title = i.title.replace("'", '')

            i.daily = str(i.daily)
            i.daily = i.daily.replace('(', '')
            i.daily = i.daily.replace(')', '')
            i.daily = i.daily.replace(',', '')
            i.daily = i.daily.replace("'", '')

            i.theater = str(i.theater)
            i.theater = i.theater.replace('(', '')
            i.theater = i.theater.replace(')', '')
            i.theater = i.theater.replace(',', '')
            i.theater = i.theater.replace("'", '')

            i.whole = str(i.whole)
            i.whole = i.whole.replace('(', '')
            i.whole = i.whole.replace(')', '')
            i.whole = i.whole.replace(',', '')
            i.whole = i.whole.replace("'", '')
            if not i.title in title2_criteria:
                writer.writerow({'title': i.title, 'title_id': i.title_id, 'daily': i.daily, 'theater': i.theater, 'whole': i.whole, 'date': i.date})


def create_db():
    create_csv()
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()

    statement = '''
        DROP TABLE IF EXISTS 'BoxOffice';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'BoxOfficeInfo';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'MovieInfo';
    '''
    cur.execute(statement)    
    conn.commit()


    statement = '''
        CREATE TABLE 'BoxOffice' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'ranking' Integer NOT NULL,
            'title' TEXT NOT NULL,
            'title_id' Integer NOT NULL,
            'ranking_date' Integer NOT NULL
        );
    '''
    cur.execute(statement)


    statement = '''
        CREATE TABLE 'BoxOfficeInfo' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'title' TEXT NOT NULL,
            'title_id' Integer NOT NULL,
            'daily' Integer NOT NULL,
            'theater' Integer NOT NULL,
            'whole' Integer NOT NULL,
            'date' Integer NOT NULL
        );
    '''
    cur.execute(statement)


    statement = '''
        CREATE TABLE 'MovieInfo' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'poster' TEXT NOT NULL,
            'title' TEXT NOT NULL,
            'title_id' Integer NOT NULL,
            'runtime' Integer NOT NULL,
            'release' TEXT NOT NULL,
            'genre' TEXT NOT NULL,
            'overview' TEXT NOT NULL,
            'starring' TEXT NOT NULL,
            'picture' TEXT NOT NULL
        );
    '''
    cur.execute(statement)


    with open('boxoffice.csv') as csvFile:
        res = csv.reader(csvFile)

        for row in res:
            if row[0] != 'ranking':
                insertion = (None, row[0], row[1], row[2], row[3])
                statement = 'INSERT INTO "BoxOffice" '
                statement += 'VALUES (?, ?, ?, ?, ?)'
                cur.execute(statement, insertion)
                conn.commit()

    with open('boxoffice_info.csv') as csvFile:
        res = csv.reader(csvFile)

        for row in res:
            if row[0] != 'title':
                insertion = (None, row[0], row[1], row[2], row[3], row[4], row[5])
                statement = 'INSERT INTO "BoxOfficeInfo" '
                statement += 'VALUES (?, ?, ?, ?, ?, ?, ?)'
                cur.execute(statement, insertion)
                conn.commit()

    with open('movie_info.csv') as csvFile:
        res = csv.reader(csvFile)

        for row in res:
            if row[0] != 'poster':
                insertion = (None, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                statement = 'INSERT INTO "MovieInfo" '
                statement += 'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
                cur.execute(statement, insertion)
                conn.commit()



def interactive_prompt():
    response = ''
    while response != 'exit':
        response = input('Enter a command: ')
        command = response.split() 

        if response == 'help':
                print("""    
    +++++++++++++++++++ HELP +++++++++++++++++++ 
    The input should be 'type' and 'date'.
    [TYPE]
    You can choose one of type below.
        daily: Show the movie information based on the date's box-office ranking
        whole: Show the movie information based on the whole gross income
        theater: Show the movie information based on the number of theaters
        date: Show the movie information based on the number of dates after release
    [DATE]
    The date type should be 'YYYY-MM-DD'
    The input example is daily 2018-12-01
    If you want to finish this system, type exit
                    """)
                continue

        elif command[0] in ['daily', 'whole', 'theater', 'date']:
            date = command[1]
            get_box_office(date)
            print(date)

        elif response == 'exit':
            print('bye')
            exit()




########### TEST LINE ########### 

# create_csv()
# create_db()


date = '2018-12-03'
get_box_office(date)
# create_db()

# for a in range(20):
#     date = datetime.strptime(date, "%Y-%m-%d")
#     date = date + timedelta(days=1)
#     date = str(date)[:10]
#     create_db()



# if __name__=="__main__":
#     interactive_prompt()