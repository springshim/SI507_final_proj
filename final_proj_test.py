import unittest
from final_proj import *
from model import *

# get_input (2)
#     entry 값이 잘 받아져서 작동하는가
#     (entry.ranking / entry.poster 등 테스트)

# create_db (5)
#     WHERE 구문이 잘 작동하는가
#     ORDER가 잘 작동하는가 (4개 해야 함)

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
    def test_get_input(self):
        # conn = sqlite3.connect(DBNAME)
        # cur = conn.cursor()

        # sql = 'SELECT Company FROM Bars'
        # results = cur.execute(sql)
        # result_list = results.fetchall()
        # self.assertIn(('Sirene',), result_list)
        # self.assertEqual(len(result_list), 1795)

        # sql = '''
        #     SELECT Company, SpecificBeanBarName, CocoaPercent,
        #            Rating
        #     FROM Bars
        #     WHERE Company="Woodblock"
        #     ORDER BY Rating DESC
        # '''
        # results = cur.execute(sql)
        # result_list = results.fetchall()


if __name__ == '__main__':
    unittest.main()
