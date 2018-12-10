# SI507 Final Project Demo by Bomi Shim
This project provides movie information of box-office top 10 ranks on a specific date. The movie information includes the movie title, poster image, runtime, release date, genre, overview, and starring with pictures. The information can be sorted by box-office ranking, runtime, release date, and budget.


## Data source
The movie information on a date input is collected from Box office Mojo using beautifulsoup.
https://www.boxofficemojo.com/daily/chart/?sortdate=2018-10-28&p=.htm

The movie information is collected from The Movie DB using API.
https://www.themoviedb.org/documentation/api?language=en-US


## Visualization Software
Flask
http://flask.pocoo.org/


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
