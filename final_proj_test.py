import unittest
from final_proj import *
from model import *

class TestBoxOffice(unittest.TestCase):
    def setUp(self):
        self.nov_11th_box_office = get_box_office('2018-11-11')
        self.june_19th_box_office = get_box_office('2018-06-19')

    def test_length(self):
        self.assertEqual(len(self.nov_11th_box_office), 10)
        self.assertEqual(len(self.june_19th_box_office), 10)

    def test_boxoffice_result(self):
        self.assertEqual(self.nov_11th_box_office[3].title, ('Overlord',))
        self.assertEqual(self.june_19th_box_office[6].title, ('Superfly',))

        self.assertEqual(self.nov_11th_box_office[3].date, ('2018-11-11'))
        self.assertEqual(self.june_19th_box_office[6].date, ('2018-06-19'))

        self.assertEqual(self.nov_11th_box_office[3].ranking, (4,))
        self.assertEqual(self.june_19th_box_office[6].ranking, (7,))        


class TestMovieID(unittest.TestCase):
    def test_movie_id(self):
        self.movie_id_1 = get_movie_id('2018-10-30')
        self.movie_id_2 = get_movie_id('2018-07-13')

        self.assertEqual(self.movie_id_1[2], '335983')
        self.assertEqual(self.movie_id_2[9], '402900')


class TestMovieInfo(unittest.TestCase):
    def test_movie_info(self):
        self.movie_info_1 = get_movie_info('2018-09-24')
        self.movie_info_2 = get_movie_info('2018-08-08')

        self.assertEqual(len(self.movie_info_1), 10)
        self.assertEqual(len(self.movie_info_2), 10)

        self.assertEqual(self.movie_info_1[0].poster, ('/qM66Hv4ByAxnilr0jaqCA9uOD4Y.jpg',))
        self.assertEqual(self.movie_info_2[5].poster, ('/cQvc9N6JiMVKqol3wcYrGshsIdZ.jpg',))

        self.assertEqual(self.movie_info_1[0].title, ('The House with a Clock in Its Walls',))
        self.assertEqual(self.movie_info_2[5].title, ('The Equalizer 2',))

        self.assertEqual(self.movie_info_1[0].runtime, (106,))
        self.assertEqual(self.movie_info_2[5].runtime, (122,))

        self.assertEqual(self.movie_info_1[0].budget, (42000000,))
        self.assertEqual(self.movie_info_2[5].budget, (62000000,))

        self.assertEqual(self.movie_info_1[0].release, ('2018-09-15',))
        self.assertEqual(self.movie_info_2[5].release, ('2018-07-19',))

        self.assertEqual(self.movie_info_1[0].genre, ('Horror',))
        self.assertEqual(self.movie_info_2[5].genre, ('Thriller',))

        self.assertEqual(self.movie_info_1[0].starring, ((['Jack Black', 'Cate Blanchett', 'Owen Vaccaro', 'Kyle MacLachlan', 'Renée Elise Goldsberry'],)))
        self.assertEqual(self.movie_info_2[5].starring, (['Denzel Washington', 'Pedro Pascal', 'Ashton Sanders', 'Orson Bean', 'Bill Pullman'],))

        self.assertEqual(self.movie_info_1[0].picture, ['/vMXgtzMdt2jSAjOECFQ5F53blbr.jpg', '/5HikVWKfkkUa8aLdCMHtREBECIn.jpg', '/pNTtj9L4eVQQIb6o79D0dJC87HS.jpg', '/7DnMuDlSdpycAQQxOIDmV66qerc.jpg', '/bNHksD4bZxWhNUIW5mwLgPWc30G.jpg'])
        self.assertEqual(self.movie_info_2[5].picture, ['/semwsON3dN3np6cyzlCw7F2YDGe.jpg', '/wAkkWX9J4n1MsLGxJxXSPvjWuzY.jpg', '/eONLhaBvc3IyhWsfwdIdbRnbK9M.jpg', '/mFClcHz7Tn9iaT0qkuGYXxcszeV.jpg', '/pIpTEQVbDif8m8OdjAxQKNCj0D6.jpg'])


class TestInput(unittest.TestCase):
    def test_boxoffice(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = 'SELECT title, title_id, ranking FROM BoxOffice WHERE ranking_date = "2018-09-22"'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual((result_list[6][0]), 'Peppermint')
        self.assertEqual((result_list[7][1]), 1777)
        self.assertEqual((result_list[1][2]), 2)


    def test_movieinfo(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''SELECT M.title, M.genre, M.budget
                FROM BoxOffice as B
                JOIN MovieInfo as M
                ON B.title_id = M.title_id
                WHERE ranking_date = "2018-10-09"
    '''
        results = cur.execute(sql)
        result_list = results.fetchall()

        self.assertEqual(len(result_list), 10)    
        self.assertEqual((result_list[2][0]), 'Night School')
        self.assertEqual((result_list[2][1]), 'Comedy')
        self.assertEqual((result_list[2][2]), 29000000)

        self.assertEqual((result_list[0][0]), 'Venom')
        self.assertEqual((result_list[0][1]), 'Science Fiction')
        self.assertEqual((result_list[0][2]), 116000000)


    def test_movieinfo_order_by_budget(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''SELECT M.title, M.budget
                FROM BoxOffice as B
                JOIN MovieInfo as M
                ON B.title_id = M.title_id
                WHERE ranking_date = "2018-09-12"
                ORDER BY M.budget DESC
    '''

        results = cur.execute(sql)
        result_list = results.fetchall()

        self.assertEqual((result_list[0][0]), 'Mission: Impossible - Fallout')
        self.assertEqual((result_list[0][1]), 178000000)

        self.assertEqual((result_list[1][0]), 'The Meg')
        self.assertEqual((result_list[1][1]), 150000000)



        sql = '''SELECT M.title, M.runtime
                FROM BoxOffice as B
                JOIN MovieInfo as M
                ON B.title_id = M.title_id
                WHERE ranking_date = "2018-09-12"
                ORDER BY M.runtime DESC
    '''

        results = cur.execute(sql)
        result_list = results.fetchall()

        self.assertEqual((result_list[0][0]), 'Mission: Impossible - Fallout')
        self.assertEqual((result_list[0][1]), 148)

        self.assertEqual((result_list[1][0]), 'BlacKkKlansman')
        self.assertEqual((result_list[1][1]), 135)


        sql = '''SELECT M.title, M.release
                FROM BoxOffice as B
                JOIN MovieInfo as M
                ON B.title_id = M.title_id
                WHERE ranking_date = "2018-09-12"
                ORDER BY M.release DESC
    '''

        results = cur.execute(sql)
        result_list = results.fetchall()

        self.assertEqual((result_list[0][0]), 'Peppermint')
        self.assertEqual((result_list[0][1]), '2018-09-06')

        self.assertEqual((result_list[1][0]), 'The Nun')
        self.assertEqual((result_list[1][1]), '2018-09-05')



if __name__ == '__main__':
    unittest.main()
