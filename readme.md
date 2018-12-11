# SI507 Final Project Demo by Bomi Shim
This project provides movie information of top 10 box-office rankings on a specific date. The movie information includes the movie title, poster image, runtime, release date, genre, overview, and starring with pictures. The information can be sorted by box-office ranking, runtime, release date, and budget.


## Data source
The movie information on a date input is collected from Box office Mojo using beautifulsoup.
https://www.boxofficemojo.com/daily/chart/?sortdate=2018-10-28&p=.htm

The movie information is collected from The Movie DB using API.
https://www.themoviedb.org/documentation/api?language=en-US


## Visualization Software
Flask
http://flask.pocoo.org/


## Code Structure
Function:
[final_proj.py]
- get_box_office(date): collects top 10 box office movie title on a date from Box Office Mojo website. It returns a list 'result_list', which has ranking, title, title id, and date. Among them, title is used as a search query in get_movie_id(date) function.
- get_movie_id(date): by using the title value from get_box_office(date) function as a search query, finds the movie_id of the search query. The movie id will be used to get more extensive movie data in get_movie_info(date) function. It returns a list 'movie_id_list', which has movie ids.
- get_movie_info(date): with movie id, it searches movie information including the movie title, poster image, runtime, release date, genre, overview, and starring with pictures. It returns a list 'compact_result' with the movie information above.
- create_csv(date): With a list result_list and compact_list, it creates two csv files.
- create_db(date): With the two csv files, it creates database with two tables, BoxOffice and MovieInfo.

[model.py]
- get_input(year, month, date, type, order): based on the user input, finds the movie data from movie.db

Class: It contains two class, BoxOffice and MovieInfo. BoxOffice class has top 10 box office movie title from Box Office Mojo website. MovieInfo class has movie information which is collected from The Movie DB API.


## Files
[python files]
final_proj.py : collects movie information, and create csv and db files.
final_proj_test.py : test the ‘final_proj.py’ and ‘model.py’ whether it works well.

[csv files]
boxoffice.csv : contains the collected data from box-office mojo. It saves top 10 box office movie title on each date.
movie_info.csv : contains the collected data from The Movie DB. The data includes the movie title, poster image, runtime, release date, genre, overview, and starring with pictures.

[database files]
movie.db: The two csv files are stored in this db file.

[flask related files]
static > style.css : cotrols the style of home page
templates > input.html, result.html : sets the frame of home page
app.py : generates flask html homepage.
model.py : reads data from the database.


## How to use
1. Run ‘final_proj.py’ to collect the movie data on a specific date.
2. In the terminal, type the date in ‘YYYY-MM-DD’ format (ex: 2018-11-21).
3. Run a virtualenv.
4. Run ‘app.py’ to generate the homepage.
5. In the hompage, select the date you want to search, and click ‘submit’ button.
6. Get the search result.
