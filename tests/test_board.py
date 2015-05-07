# encoding: utf-8

import pinterest
import unittest
import json


class BoardTest(unittest.TestCase):
    """
    Board model unit tests
    """

    SAMPLE_JSON = '''{
      "category": null,
      "is_collaborative": false,
      "layout": "default",
      "name": "Test board 1",
      "url": "/testuser/board1/",
      "created_at": "Mon, 26 Sep 2011 00:26:19 +0000",
      "collaborated_by_me": false,
      "followed_by_me": true,
      "type": "board",
      "id": "178314535185157810",
      "image_thumbnail_url": "http://media-cache-ak0.pinimg.com/upload/178314535185157810_board_thumbnail_2015-03-07-16-50-40_9153_60.jpg"
    }'''

    def _get_sample_board(self):
        """
        Builds a sample board
        :return: Returns an instance of pinterest.Board
        """
        return pinterest.Board(id='178314535185157810',
                               name='Test board 1',
                               url='/testuser/board1/',
                               layout='default',
                               category='travel',
                               type='board',
                               image_thumbnail_url='http://media-cache-ak0.pinimg.com/upload/178314535185157810_board_thumbnail_2015-03-07-16-50-40_9153_60.jpg',
                               is_collaborative=False,
                               collaborated_by_me=False,
                               followed_by_me=True,
                               created_at='Mon, 26 Sep 2011 00:26:19 +0000')

    def testInit(self):
        """
        Tests the pinterest.Board constructor
        :return:
        """
        board = pinterest.Board(id='178314535185157810',
                                name='Test board 1',
                                url='/testuser/board1/',
                                layout='default',
                                category='travel',
                                type='board',
                                image_thumbnail_url='http://media-cache-ak0.pinimg.com/upload/178314535185157810_board_thumbnail_2015-03-07-16-50-40_9153_60.jpg',
                                is_collaborative=False,
                                collaborated_by_me=False,
                                followed_by_me=True,
                                created_at='Mon, 26 Sep 2011 00:26:19 +0000')
        self.assertIsInstance(board, pinterest.Board)

    def testProperties(self):
        """
        Tests all of the pinterest.Board properties
        """
        board = pinterest.Board()
        board.id = '178314535185157810'
        self.assertEqual('178314535185157810', board.id)

        board.name = 'Test board 1'
        self.assertEqual('Test board 1', board.name)

        board.url = '/testuser/board1/'
        self.assertEqual('/testuser/board1/', board.url)

        board.layout = 'default'
        self.assertEqual('default', board.layout)

        board.category = 'travel'
        self.assertEqual('travel', board.category)

        board.type = 'board'
        self.assertEqual('board', board.type)

        board.image_thumbnail_url = 'http://media-cache-ak0.pinimg.com/upload/178314535185157810_board_thumbnail_2015-03-07-16-50-40_9153_60.jpg'
        self.assertEqual('http://media-cache-ak0.pinimg.com/upload/178314535185157810_board_thumbnail_2015-03-07-16-50-40_9153_60.jpg', board.image_thumbnail_url)

        board.is_collaborative = False
        self.assertEqual(False, board.is_collaborative)

        board.collaborated_by_me = False
        self.assertEqual(False, board.collaborated_by_me)

        board.followed_by_me = True
        self.assertEqual(True, board.followed_by_me)

        board.created_at = 'Mon, 26 Sep 2011 00:26:19 +0000'
        self.assertEqual('Mon, 26 Sep 2011 00:26:19 +0000', board.created_at)

    def testAsDict(self):
        """
        Tests the pinterest.Board asDict method
        """
        board = self._get_sample_board()
        data = board.asDict()
        self.assertEqual('178314535185157810', data['id'])
        self.assertEqual('Test board 1', data['name'])
        self.assertEqual('/testuser/board1/', data['url'])
        self.assertEqual('default', data['layout'])
        self.assertEqual('travel', data['category'])
        self.assertEqual('board', data['type'])
        self.assertEqual('http://media-cache-ak0.pinimg.com/upload/178314535185157810_board_thumbnail_2015-03-07-16-50-40_9153_60.jpg', data['image_thumbnail_url'])
        self.assertEqual(False, data['is_collaborative'])
        self.assertEqual(False, data['collaborated_by_me'])
        self.assertEqual(True, data['followed_by_me'])
        self.assertEqual('Mon, 26 Sep 2011 00:26:19 +0000', data['created_at'])

    def testEq(self):
        """
        Tests the pinterest.Board __eq__ method
        """
        board = pinterest.Board()
        board.id = '178314535185157810'
        board.name = 'Test board 1'
        board.url = '/testuser/board1/'
        board.layout = 'default'
        board.category = 'travel'
        board.type = 'board'
        board.image_thumbnail_url = 'http://media-cache-ak0.pinimg.com/upload/178314535185157810_board_thumbnail_2015-03-07-16-50-40_9153_60.jpg'
        board.is_collaborative = False
        board.collaborated_by_me = False
        board.followed_by_me = True
        board.created_at = 'Mon, 26 Sep 2011 00:26:19 +0000'
        self.assertEqual(board, self._get_sample_board())

    def testNewFromJsonDict(self):
        """
        Tests the pinterest.Board newFromJsonDict
        """
        data = json.loads(BoardTest.SAMPLE_JSON)
        status = pinterest.Board.newFromJsonDict(data)
        self.assertEqual(self._get_sample_board(), status)