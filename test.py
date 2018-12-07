from secret import movie_db_api_key
import requests
import json
from bs4 import BeautifulSoup
import sqlite3
import csv
from datetime import datetime, timedelta

def create_db():
    create_csv()
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()

    statement = '''
        DROP TABLE IF EXISTS 'MovieInfo';
    '''
    cur.execute(statement)    
    conn.commit()


    statement = '''
        CREATE TABLE 'MovieInfo' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'poster' TEXT NOT NULL,
            'title' TEXT NOT NULL,
            'title_id' Integer NOT NULL,
            'runtime' Integer NOT NULL,
            'budget' Integer NOT NULL,
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

    with open('movie_info.csv') as csvFile:
        res = csv.reader(csvFile)

        for row in res:
            if row[0] != 'poster':
                insertion = (None, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                statement = 'INSERT INTO "MovieInfo" '
                statement += 'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
                cur.execute(statement, insertion)
                conn.commit()