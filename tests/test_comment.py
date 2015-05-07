# encoding: utf-8

import pinterest
import unittest
import json


class CommentTest(unittest.TestCase):
    """
    Comment model unit tests
    """

    SAMPLE_JSON = '''{
      "text": "Travel Germany",
      "created_at": "Thu, 19 Feb 2015 21:55:08 +0000",
      "type": "comment",
      "id": "424605277246025455"
    }'''

    def _get_sample_comment(self):
        """
        Builds a sample comment
        :return: Returns an instance of pinterest.Comment
        """
        return pinterest.Comment(id='424605277246025455',
                                 type='comment',
                                 text='Travel Germany',
                                 created_at='Thu, 19 Feb 2015 21:55:08 +0000')

    def testInit(self):
        """
        Tests the pinterest.Comment constructor
        :return:
        """
        comment = pinterest.Comment(id='424605277246025455',
                                    type='comment',
                                    text='Travel Germany',
                                    created_at='Thu, 19 Feb 2015 21:55:08 +0000')
        self.assertIsInstance(comment, pinterest.Comment)

    def testProperties(self):
        """
        Tests all of the pinterest.Comment properties
        """
        comment = pinterest.Comment()
        comment.id = '424605277246025455'
        self.assertEqual('424605277246025455', comment.id)

        comment.type = 'comment'
        self.assertEqual('comment', comment.type)

        comment.text = 'Travel Germany'
        self.assertEqual('Travel Germany', comment.text)

        comment.created_at = 'Thu, 19 Feb 2015 21:55:08 +0000'
        self.assertEqual('Thu, 19 Feb 2015 21:55:08 +0000', comment.created_at)

    def testAsDict(self):
        """
        Tests the pinterest.Comment asDict method
        """
        comment = self._get_sample_comment()
        data = comment.asDict()
        self.assertEqual('424605277246025455', data['id'])
        self.assertEqual('comment', data['type'])
        self.assertEqual('Travel Germany', data['text'])
        self.assertEqual('Thu, 19 Feb 2015 21:55:08 +0000', data['created_at'])

    def testEq(self):
        """
        Tests the pinterest.Comment __eq__ method
        """
        comment = pinterest.Comment()
        comment.id = '424605277246025455'
        comment.type = 'comment'
        comment.text = 'Travel Germany'
        comment.created_at = 'Thu, 19 Feb 2015 21:55:08 +0000'
        self.assertEqual(comment, self._get_sample_comment())

    def testNewFromJsonDict(self):
        """
        Tests the pinterest.Comment newFromJsonDict
        """
        data = json.loads(CommentTest.SAMPLE_JSON)
        status = pinterest.Comment.newFromJsonDict(data)
        self.assertEqual(self._get_sample_comment(), status)