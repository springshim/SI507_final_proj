import sqlite3
import csv
import json
from datetime import datetime

DBNAME = 'movie.db'

def get_query_from_db(command):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    parameter = command.split()
    params = []
    result = []

    # statement = 'SELECT B.ranking, M.poster, M.title, M.runtime, M.release, M.genre, M.overview, M.starring '
    statement = 'SELECT M.title ' #이거 지우고 위에 것으로 해야됨
    statement += 'FROM BoxOffice as B '
    statement += 'JOIN MovieInfo as M '
    statement += 'ON B.title_id = M.title_id '
    statement += 'WHERE B.ranking_date = ? '

    if parameter[0] == 'runtime':    
        statement += 'ORDER BY M.runtime '

    elif parameter[0] == 'budget':
        statement += 'ORDER BY M.budget '

    elif parameter[0] == 'release':
        statement += 'ORDER BY M.release '

    elif parameter[0] == 'boxoffice':
        statement += 'ORDER BY B.ranking '

    if 'DESC' in command:
        statement += 'DESC '

    elif 'ASC' in command:
        statement += 'ASC '

    else:
        statement += 'ASC '

    params.append(parameter[1])
    cur.execute(statement, params)
    results = cur.fetchall()
    for row in results:
        result.append(row)
        # print(row)
    print(result)

    return result


def interactive_prompt():
    response = ''
    while response != 'exit':
        response = input('Enter a command: ')
        command = response.split() 

        if len(response) == 1:
            if response == 'help':
                    print("""    
        +++++++++++++++++++ HELP +++++++++++++++++++ 
        The input should be 'type' and 'date'.
        [TYPE]
        You can choose one of type below.
            boxoffice: Show the movie information based on the date's box-office ranking
            runtime: Show the movie information based on the whole gross income
            releasedate: Show the movie information based on the number of theaters
            budget: Show the movie information based on the number of dates after release
        [DATE]
        The date type should be 'YYYY-MM-DD'
        The input example is daily 2018-12-01
        If you want to finish this system, type exit
                        """)
                    continue

            elif response == 'exit':
                print('bye')
                exit()

            else:
                print('Wrong input, try again')
                
        else:
            if command[0] in ['boxoffice', 'runtime', 'release', 'budget']:
                get_query_from_db(response)

            else:
                print('wrong input')


if __name__=="__main__":
    interactive_prompt()