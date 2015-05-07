# encoding: utf-8

import pinterest
import unittest
import json


class PinTest(unittest.TestCase):
    """
    Pin model unit tests
    """

    SAMPLE_JSON = '''{
      "domain": "pinterest.com",
      "image_square_size_pixels": {
        "width": 45,
        "height": 45
      },
      "image_medium_url": "http://media-cache-ec0.pinimg.com/200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg",
      "like_count": 0,
      "image_medium_size_points": {
        "width": 200,
        "height": 302
      },
      "id": "414753446908885020",
      "image_large_size_points": {
        "width": 600,
        "height": 906
      },
      "price_currency": "USD",
      "title": "",
      "image_square_size_points": {
        "width": 45,
        "height": 45
      },
      "comment_count": 0,
      "cacheable_id": "414753446908885020",
      "type": "pin",
      "image_large_url": "http://media-cache-ec0.pinimg.com/1200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg",
      "image_large_size_pixels": {
        "width": 700,
        "height": 1058
      },
      "attribution": null,
      "description": "How to Avocado Face Mask: www.balibody.com.au",
      "price_value": 0,
      "is_playable": false,
      "link": "https://www.pinterest.com/pin/283163895292465591/",
      "is_repin": false,
      "liked_by_me": false,
      "is_uploaded": false,
      "image_square_url": "http://media-cache-ec0.pinimg.com/45x45/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg",
      "repin_count": 0,
      "tracked_link": "https://www.pinterest.com/pin/283163895292465591/",
      "created_at": "Tue, 10 Mar 2015 07:08:42 +0000",
      "image_medium_size_pixels": {
        "width": 200,
        "height": 302
      },
      "promoter": null,
      "debug": null,
      "is_video": false
    }
    '''
    
    def _get_sample_pin(self):
        """
        Builds a sample pin
        :return: Returns an instance of pinterest.Pin
        """
        return pinterest.Pin(id='414753446908885020',
                             cacheable_id='414753446908885020',
                             title='',
                             description='How to Avocado Face Mask: www.balibody.com.au',
                             type='pin',
                             domain='pinterest.com',
                             link='https://www.pinterest.com/pin/283163895292465591/',
                             like_count=0,
                             comment_count=0,
                             repin_count=0,
                             image_square_url='http://media-cache-ec0.pinimg.com/45x45/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg',
                             image_square_size_pixels={
                                'width': 45,
                                'height': 45
                             },
                             image_square_size_points={
                                'width': 45,
                                'height': 45
                             },
                             image_medium_url='http://media-cache-ec0.pinimg.com/200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg',
                             image_medium_size_pixels={
                                'width': 200,
                                'height': 302
                             },
                             image_medium_size_points={
                                'width': 200,
                                'height': 302
                             },
                             image_large_url='http://media-cache-ec0.pinimg.com/1200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg',
                             image_large_size_pixels={
                                'width': 700,
                                'height': 1058
                             },
                             image_large_size_points={
                                'width': 600,
                                'height': 906
                             },
                             price_value=0,
                             price_currency='USD',
                             attribution=None,
                             tracked_link='https://www.pinterest.com/pin/283163895292465591/',
                             promoter=None,
                             debug=None,
                             liked_by_me=False,
                             is_repin=False,
                             is_uploaded=False,
                             is_playable=False,
                             is_video=False,
                             created_at='Tue, 10 Mar 2015 07:08:42 +0000')

    def testInit(self):
        """
        Tests the pinterest.Pin constructor
        :return:
        """
        pin = pinterest.Pin(id='414753446908885020',
                            cacheable_id='414753446908885020',
                            title='',
                            description='How to Avocado Face Mask: www.balibody.com.au',
                            type='pin',
                            domain='pinterest.com',
                            link='https://www.pinterest.com/pin/283163895292465591/',
                            like_count=0,
                            comment_count=0,
                            repin_count=0,
                            image_square_url='http://media-cache-ec0.pinimg.com/45x45/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg',
                            image_square_size_pixels={
                                'width': 45,
                                'height': 45
                            },
                            image_square_size_points={
                                'width': 45,
                                'height': 45
                            },
                            image_medium_url='http://media-cache-ec0.pinimg.com/200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg',
                            image_medium_size_pixels={
                                'width': 200,
                                'height': 302
                            },
                            image_medium_size_points={
                                'width': 200,
                                'height': 302
                            },
                            image_large_url='http://media-cache-ec0.pinimg.com/1200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg',
                            image_large_size_pixels={
                                'width': 700,
                                'height': 1058
                            },
                            image_large_size_points={
                                'width': 600,
                                'height': 906
                            },
                            price_value=0,
                            price_currency='USD',
                            attribution=None,
                            tracked_link='https://www.pinterest.com/pin/283163895292465591/',
                            promoter=None,
                            debug=None,
                            liked_by_me=False,
                            is_repin=False,
                            is_uploaded=False,
                            is_playable=False,
                            is_video=False,
                            created_at='Tue, 10 Mar 2015 07:08:42 +0000')
        self.assertIsInstance(pin, pinterest.Pin)

    def testProperties(self):
        """
        Tests all of the pinterest.Pin properties
        """
        pin = pinterest.Pin()
        pin.id = '414753446908885020'
        self.assertEqual('414753446908885020', pin.id)

        pin.cacheable_id = '414753446908885020'
        self.assertEqual('414753446908885020', pin.cacheable_id)

        pin.title = ''
        self.assertEqual('', pin.title)

        pin.description = 'How to Avocado Face Mask: www.balibody.com.au'
        self.assertEqual('How to Avocado Face Mask: www.balibody.com.au', pin.description)

        pin.type = 'pin'
        self.assertEqual('pin', pin.type)

        pin.domain = 'pinterest.com'
        self.assertEqual('pinterest.com', pin.domain)

        pin.link = 'https://www.pinterest.com/pin/283163895292465591/'
        self.assertEqual('https://www.pinterest.com/pin/283163895292465591/', pin.link)

        pin.like_count = 0
        self.assertEqual(0, pin.like_count)

        pin.comment_count = 0
        self.assertEqual(0, pin.comment_count)

        pin.repin_count = 0
        self.assertEqual(0, pin.repin_count)

        pin.image_square_url = 'http://media-cache-ec0.pinimg.com/45x45/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg'
        self.assertEqual('http://media-cache-ec0.pinimg.com/45x45/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg',
                         pin.image_square_url)

        pin.image_square_size_pixels = {
            'width': 45,
            'height': 45
        }
        self.assertEqual({'width': 45, 'height': 45}, pin.image_square_size_pixels)

        pin.image_square_size_points = {
            'width': 45,
            'height': 45
        }
        self.assertEqual({'width': 45, 'height': 45}, pin.image_square_size_points)

        pin.image_medium_url = 'http://media-cache-ec0.pinimg.com/200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg'
        self.assertEqual('http://media-cache-ec0.pinimg.com/200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg',
                         pin.image_medium_url)

        pin.image_medium_size_pixels = {
            'width': 200,
            'height': 302
        }
        self.assertEqual({'width': 200, 'height': 302}, pin.image_medium_size_pixels)

        pin.image_medium_size_points = {
            'width': 200,
            'height': 302
        }
        self.assertEqual({'width': 200, 'height': 302}, pin.image_medium_size_points)

        pin.image_large_url = 'http://media-cache-ec0.pinimg.com/1200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg'
        self.assertEqual('http://media-cache-ec0.pinimg.com/1200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg',
                         pin.image_large_url)

        pin.image_large_size_pixels = {
            'width': 700,
            'height': 1058
        }
        self.assertEqual({'width': 700, 'height': 1058}, pin.image_large_size_pixels)

        pin.image_large_size_points = {
            'width': 600,
            'height': 906
        }
        self.assertEqual({'width': 600, 'height': 906}, pin.image_large_size_points)

        pin.price_value = 0
        self.assertEqual(0, pin.price_value)

        pin.price_currency = 'USD'
        self.assertEqual('USD', pin.price_currency)

        pin.attribution = None
        self.assertEqual(None, pin.attribution)

        pin.tracked_link = 'https://www.pinterest.com/pin/283163895292465591/'
        self.assertEqual('https://www.pinterest.com/pin/283163895292465591/', pin.tracked_link)

        pin.promoter = None
        self.assertEqual(None, pin.promoter)

        pin.debug = None
        self.assertEqual(None, pin.debug)

        pin.liked_by_me = False
        self.assertEqual(False, pin.liked_by_me)

        pin.is_repin = False
        self.assertEqual(False, pin.is_repin)

        pin.is_uploaded = False
        self.assertEqual(False, pin.is_uploaded)

        pin.is_playable = False
        self.assertEqual(False, pin.is_playable)

        pin.is_video = False
        self.assertEqual(False, pin.is_video)

        pin.created_at = 'Tue, 10 Mar 2015 07:08:42 +0000'
        self.assertEqual('Tue, 10 Mar 2015 07:08:42 +0000', pin.created_at)

    def testAsDict(self):
        """
        Tests the pinterest.Pin asDict method
        """
        pin = self._get_sample_pin()
        data = pin.asDict()
        self.assertEqual('414753446908885020', data['id'])
        self.assertEqual('414753446908885020', data['cacheable_id'])
        self.assertEqual('', data['title'])
        self.assertEqual('How to Avocado Face Mask: www.balibody.com.au', data['description'])
        self.assertEqual('pin', data['type'])
        self.assertEqual('pinterest.com', data['domain'])
        self.assertEqual('https://www.pinterest.com/pin/283163895292465591/', data['link'])
        self.assertEqual(0, data['like_count'])
        self.assertEqual(0, data['comment_count'])
        self.assertEqual(0, data['repin_count'])
        self.assertEqual('http://media-cache-ec0.pinimg.com/45x45/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg',
                         data['image_square_url'])
        self.assertEqual({'width': 45, 'height': 45}, data['image_square_size_pixels'])
        self.assertEqual({'width': 45, 'height': 45}, data['image_square_size_points'])
        self.assertEqual('http://media-cache-ec0.pinimg.com/200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg',
                         data['image_medium_url'])
        self.assertEqual({'width': 200, 'height': 302}, data['image_medium_size_pixels'])
        self.assertEqual({'width': 200, 'height': 302}, data['image_medium_size_points'])
        self.assertEqual('http://media-cache-ec0.pinimg.com/1200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg',
                         data['image_large_url'])
        self.assertEqual({'width': 700, 'height': 1058}, data['image_large_size_pixels'])
        self.assertEqual({'width': 600, 'height': 906}, data['image_large_size_points'])
        self.assertEqual(0, data['price_value'])
        self.assertEqual('USD', data['price_currency'])
        self.assertEqual(None, data['attribution'])
        self.assertEqual('https://www.pinterest.com/pin/283163895292465591/', data['tracked_link'])
        self.assertEqual(None, data['promoter'])
        self.assertEqual(None, data['debug'])
        self.assertEqual(False, data['liked_by_me'])
        self.assertEqual(False, data['is_repin'])
        self.assertEqual(False, data['is_uploaded'])
        self.assertEqual(False, data['is_playable'])
        self.assertEqual(False, data['is_video'])
        self.assertEqual('Tue, 10 Mar 2015 07:08:42 +0000', data['created_at'])

    def testEq(self):
        """
        Tests the pinterest.Pin __eq__ method
        """
        pin = pinterest.Pin()
        pin.id = '414753446908885020'
        pin.cacheable_id = '414753446908885020'
        pin.title = ''
        pin.description = 'How to Avocado Face Mask: www.balibody.com.au'
        pin.type = 'pin'
        pin.domain = 'pinterest.com'
        pin.link = 'https://www.pinterest.com/pin/283163895292465591/'
        pin.like_count = 0
        pin.comment_count = 0
        pin.repin_count = 0
        pin.image_square_url = 'http://media-cache-ec0.pinimg.com/45x45/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg'
        pin.image_square_size_pixels = {
            'width': 45,
            'height': 45
        }
        pin.image_square_size_points = {
            'width': 45,
            'height': 45
        }
        pin.image_medium_url = 'http://media-cache-ec0.pinimg.com/200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg'
        pin.image_medium_size_pixels = {
            'width': 200,
            'height': 302
        }
        pin.image_medium_size_points = {
            'width': 200,
            'height': 302
        }
        pin.image_large_url = 'http://media-cache-ec0.pinimg.com/1200x/2b/8c/a7/2b8ca70274aafc0f18e01fdadf775808.jpg'
        pin.image_large_size_pixels = {
            'width': 700,
            'height': 1058
        }
        pin.image_large_size_points = {
            'width': 600,
            'height': 906
        }
        pin.price_value = 0
        pin.price_currency = 'USD'
        pin.attribution = None
        pin.tracked_link = 'https://www.pinterest.com/pin/283163895292465591/'
        pin.promoter = None
        pin.debug = None
        pin.liked_by_me = False
        pin.is_repin = False
        pin.is_uploaded = False
        pin.is_playable = False
        pin.is_video = False
        pin.created_at = 'Tue, 10 Mar 2015 07:08:42 +0000'

        self.assertEqual(pin, self._get_sample_pin())

    def testNewFromJsonDict(self):
        """
        Tests the pinterest.Pin newFromJsonDict
        """
        data = json.loads(PinTest.SAMPLE_JSON)
        status = pinterest.Pin.newFromJsonDict(data)
        self.assertEqual(self._get_sample_pin(), status)