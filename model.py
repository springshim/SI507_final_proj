import sqlite3
import csv

DBNAME = 'movie.db'
entries = []
c = []

def get_input(year, month, date, type, order):
    global entries
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    command = str(year) + '-' + str(month) + '-' + str(date) + ' ' + str(type) + ' ' + str(order)
    parameter = command.split()
    params = []
    result = []

    statement = 'SELECT B.ranking, M.poster, M.title, M.runtime, M.release, M.genre, M.overview, M.starring, M.picture '
    statement += 'FROM BoxOffice as B '
    statement += 'JOIN MovieInfo as M '
    statement += 'ON B.title_id = M.title_id '
    statement += 'WHERE B.ranking_date = ? '

    if parameter[1] == 'runtime':
        statement += 'ORDER BY M.runtime '

    elif parameter[1] == 'budget':
        statement += 'ORDER BY M.budget '

    elif parameter[1] == 'release':
        statement += 'ORDER BY M.release '

    elif parameter[1] == 'boxoffice':
        statement += 'ORDER BY B.ranking '

    if 'desc' in command:
        statement += 'DESC '

    elif 'asc' in command:
        statement += 'ASC '

    params.append(parameter[0])
    cur.execute(statement, params)
    results = cur.fetchall()

    entries = []
    for row in results:
        ranking = row[0]
        poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2' + row[1]
        title = row[2]
        runtime = row[3]
        release = row[4]
        genre = row[5]
        overview = row[6]

        res = row[7]
        a = res.split()
        starring = []
        index = 0
        for i in range(5):
            b = str(a[index:index+2])
            b = b.replace(",", "")
            b = b.replace("'", '')
            b = b.replace('[', '')
            b = b.replace(']', '')
            b = b.replace('(', '')
            b = b.replace(')', '')
            b = b.replace('"', '')
            starring.append(b)
            index += 2

        res = row[8]
        a = res.split()
        picture = []

        for i in range(5):
            a[i] = a[i].replace(',', '')
            a[i] = a[i].replace("'", '')
            a[i] = a[i].replace("[", '')
            a[i] = a[i].replace("]", '')
            url = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2' + a[i]
            picture.append(url)

        entry = {"ranking": ranking, "poster": poster, "title": title, "runtime": runtime, "release": release, "genre": genre, "overview": overview,
                "starring0": starring[0], "starring1": starring[1], "starring2": starring[2], "starring3": starring[3], "starring4": starring[4],
                "picture0": picture[0], "picture1": picture[1], "picture2": picture[2], "picture3": picture[3], "picture4": picture[4]}
        entries.append(entry)

    return entries
