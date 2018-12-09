import sqlite3
import csv

DBNAME = 'movie.db'
entries = []
ENTRIES_FILE = "entries.json"

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

    for row in results:
        entries.append(row)
    print(entries)

    for row, i in results:
        ranking = row[0]
        poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2' + row[1]
        title = row[2]
        runtime = row[3]
        release = row[4]
        genre = row[5]
        overview = row[6]

        a = row[7].split()
        b= str(a[0:2])
        b = b.replace(",", "")
        b = b.replace("'", '')
        b = b.replace('[', '')
        b = b.replace(']', '')
        b = b.replace('(', '')
        b = b.replace(')', '')
        b = b.replace('"', '')

        starring = row[7]
        picture = row[8]

        entry = {"ranking": name, "text": text, "timestamp": time_string, "id": str(next_id)}



    # try:
    #     f = open(ENTRIES_FILE, "w")
    #     dump_string = json.dumps(entries)
    #     f.delete()
    #     f.write(dump_string)
    #     f.close()
    # except:
    #     print("ERROR! Could not write entries to file.")

    return entries


def get_result():
    global entries
    return entries    


get_input(2018, 11, 11, 'runtime', 'asc')

# def interactive_prompt():
#     response = ''
#     while response != 'exit':
#         response = input('Enter a command: ')
#         command = response.split() 

#         if len(response) == 1:
#             if response == 'help':
#                     print("""    
#         +++++++++++++++++++ HELP +++++++++++++++++++ 
#         The input should be 'type' and 'date'.
#         [TYPE]
#         You can choose one of type below.
#             boxoffice: Show the movie information based on the date's box-office ranking
#             runtime: Show the movie information based on the whole gross income
#             releasedate: Show the movie information based on the number of theaters
#             budget: Show the movie information based on the number of dates after release
#         [DATE]
#         The date type should be 'YYYY-MM-DD'
#         The input example is daily 2018-12-01
#         If you want to finish this system, type exit
#                         """)
#                     continue

#             elif response == 'exit':
#                 print('bye')
#                 exit()

#             else:
#                 print('Wrong input, try again')
                
#         else:
#             if command[0] in ['boxoffice', 'runtime', 'release', 'budget']:
#                 get_query_from_db(response)

#             else:
#                 print('wrong input')


# if __name__=="__main__":
#     interactive_prompt()