# encoding: utf-8

import pinterest
import unittest
import json


class UserTest(unittest.TestCase):
    """
    User model unit tests
    """

    SAMPLE_JSON = ''' {
      "is_employee": false,
      "last_name": "Test",
      "domain_verified": false,
      "following_count": 12,
      "image_medium_url": "http://media-cache-ak0.pinimg.com/avatars/242132_75.jpg",
      "implicitly_followed_by_me": false,
      "like_count": 8,
      "has_password": true,
      "full_name": "Test User",
      "partner": null,
      "image_small_url": "http://media-cache-ak0.pinimg.com/avatars/2321323_30.jpg",
      "gplus_url": null,
      "id": "171911222222223333",
      "first_name": "Test",
      "domain_url": null,
      "personalize_from_offsite_browsing": true,
      "explicitly_followed_by_me": false,
      "location": "",
      "indexed": true,
      "is_partner": false,
      "followed_by_me": false,
      "type": "user",
      "email": "test@gmail.com",
      "website_url": null,
      "board_count": 10,
      "username": "test",
      "repins_from": [],
      "is_default_image": false,
      "pin_thumbnail_urls": [
        "http://media-cache-ak0.pinimg.com/75x75/6c/77/80/8.jpg",
        "http://media-cache-ak0.pinimg.com/75x75/4f/ea/fc/7.jpg",
        "http://media-cache-ec0.pinimg.com/75x75/68/0f/c2/3.jpg",
        "http://media-cache-ec0.pinimg.com/75x75/0d/22/74/3.jpg",
        "http://media-cache-ec0.pinimg.com/75x75/b0/42/c2/6.jpg"
      ],
      "pins": [],
      "latest_category": [
        {
          "token": "weddings",
          "display": "Weddings"
        }
      ],
      "pin_count": 211,
      "ads_customize_from_conversion": true,
      "about": "",
      "followed_boards": [],
      "email_verified": true,
      "created_at": "Sun, 09 Dec 2015 12:28:12 +0000",
      "low_engagement_board_count": 100,
      "verified_domains": [],
      "tag": null,
      "image_large_url": "http://media-cache-ak0.pinimg.com/avatars/60916_140.jpg",
      "debug": null,
      "email_verification_code": null,
      "follower_count": 132,
      "blocked_by_me": false
    }
    '''

    def _get_sample_user(self):
        """
        Builds a sample user
        :return: Returns an instance of pinterest.User
        """
        return pinterest.User(id='171911222222223333',
                              first_name='Test',
                              last_name='Test',
                              full_name='Test User',
                              following_count=12,
                              follower_count=132,
                              pin_count=211,
                              board_count=10,
                              like_count=8,
                              email='test@gmail.com',
                              email_verified=True,
                              email_verification_code=None,
                              username='test',
                              about='',
                              location='',
                              type='user',
                              pins=[],
                              pin_thumbnail_urls=[
                                  'http://media-cache-ak0.pinimg.com/75x75/6c/77/80/8.jpg',
                                  'http://media-cache-ak0.pinimg.com/75x75/4f/ea/fc/7.jpg',
                                  'http://media-cache-ec0.pinimg.com/75x75/68/0f/c2/3.jpg',
                                  'http://media-cache-ec0.pinimg.com/75x75/0d/22/74/3.jpg',
                                  'http://media-cache-ec0.pinimg.com/75x75/b0/42/c2/6.jpg'
                              ],
                              repins_from=[],
                              followed_boards=[],
                              image_small_url='http://media-cache-ak0.pinimg.com/avatars/2321323_30.jpg',
                              image_medium_url='http://media-cache-ak0.pinimg.com/avatars/242132_75.jpg',
                              image_large_url='http://media-cache-ak0.pinimg.com/avatars/60916_140.jpg',
                              is_default_image=False,
                              has_password=True,
                              is_employee=False,
                              followed_by_me=False,
                              domain_verified=False,
                              explicitly_followed_by_me=False,
                              implicitly_followed_by_me=False,
                              blocked_by_me=False,
                              gplus_url=None,
                              domain_url=None,
                              is_partner=False,
                              partner=None,
                              indexed=True,
                              website_url=None,
                              latest_category=[
                                  {
                                      'token': 'weddings',
                                      'display': 'Weddings'
                                  }
                              ],
                              ads_customize_from_conversion=True,
                              low_engagement_board_count=100,
                              personalize_from_offsite_browsing=True,
                              verified_domains=[],
                              tag=None,
                              debug=None,
                              created_at='Sun, 09 Dec 2015 12:28:12 +0000')

    def testInit(self):
        """
        Tests the pinterest.User constructor
        :return:
        """
        user = pinterest.User(id='171911222222223333',
                              first_name='Test',
                              last_name='Test',
                              full_name='Test User',
                              following_count=12,
                              follower_count=132,
                              pin_count=211,
                              board_count=10,
                              like_count=8,
                              email='test@gmail.com',
                              email_verified=True,
                              email_verification_code=None,
                              username='test',
                              about='',
                              location='',
                              type='user',
                              pins=[],
                              pin_thumbnail_urls=[
                                  'http://media-cache-ak0.pinimg.com/75x75/6c/77/80/8.jpg',
                                  'http://media-cache-ak0.pinimg.com/75x75/4f/ea/fc/7.jpg',
                                  'http://media-cache-ec0.pinimg.com/75x75/68/0f/c2/3.jpg',
                                  'http://media-cache-ec0.pinimg.com/75x75/0d/22/74/3.jpg',
                                  'http://media-cache-ec0.pinimg.com/75x75/b0/42/c2/6.jpg'
                              ],
                              repins_from=[],
                              followed_boards=[],
                              image_small_url='http://media-cache-ak0.pinimg.com/avatars/2321323_30.jpg',
                              image_medium_url='http://media-cache-ak0.pinimg.com/avatars/242132_75.jpg',
                              image_large_url='http://media-cache-ak0.pinimg.com/avatars/60916_140.jpg',
                              is_default_image=False,
                              has_password=True,
                              is_employee=False,
                              followed_by_me=False,
                              domain_verified=False,
                              explicitly_followed_by_me=False,
                              implicitly_followed_by_me=False,
                              blocked_by_me=False,
                              gplus_url=None,
                              domain_url=None,
                              is_partner=False,
                              partner=None,
                              indexed=True,
                              website_url=None,
                              latest_category=[
                                  {
                                      'token': 'weddings',
                                      'display': 'Weddings'
                                  }
                              ],
                              ads_customize_from_conversion=True,
                              low_engagement_board_count=100,
                              personalize_from_offsite_browsing=True,
                              verified_domains=[],
                              tag=None,
                              debug=None,
                              created_at='Sun, 09 Dec 2015 12:28:12 +0000')
        self.assertIsInstance(user, pinterest.User)

    def testProperties(self):
        """
        Tests all of the pinterest.User properties
        """
        user = pinterest.User()
        user.id = '171911222222223333'
        self.assertEqual('171911222222223333', user.id)

        user.first_name = 'Test'
        self.assertEqual('Test', user.first_name)

        user.last_name = 'Test'
        self.assertEqual('Test', user.last_name)

        user.full_name = 'Test User'
        self.assertEqual('Test User', user.full_name)

        user.following_count = 12
        self.assertEqual(12, user.following_count)

        user.follower_count = 132
        self.assertEqual(132, user.follower_count)

        user.pin_count = 211
        self.assertEqual(211, user.pin_count)

        user.board_count = 10
        self.assertEqual(10, user.board_count)

        user.like_count = 8
        self.assertEqual(8, user.like_count)

        user.email = 'test@gmail.com'
        self.assertEqual('test@gmail.com', user.email)

        user.email_verified = True
        self.assertEqual(True, user.email_verified)

        user.email_verification_code = None
        self.assertEqual(None, user.email_verification_code)

        user.username = 'test'
        self.assertEqual('test', user.username)

        user.about = ''
        self.assertEqual('', user.about)

        user.location = ''
        self.assertEqual('', user.location)

        user.type = 'user'
        self.assertEqual('user', user.type)

        user.pins = []
        self.assertEqual([], user.pins)

        user.pin_thumbnail_urls = [
            'http://media-cache-ak0.pinimg.com/75x75/6c/77/80/8.jpg',
            'http://media-cache-ak0.pinimg.com/75x75/4f/ea/fc/7.jpg',
            'http://media-cache-ec0.pinimg.com/75x75/68/0f/c2/3.jpg',
            'http://media-cache-ec0.pinimg.com/75x75/0d/22/74/3.jpg',
            'http://media-cache-ec0.pinimg.com/75x75/b0/42/c2/6.jpg'
        ]
        self.assertEqual([
            'http://media-cache-ak0.pinimg.com/75x75/6c/77/80/8.jpg',
            'http://media-cache-ak0.pinimg.com/75x75/4f/ea/fc/7.jpg',
            'http://media-cache-ec0.pinimg.com/75x75/68/0f/c2/3.jpg',
            'http://media-cache-ec0.pinimg.com/75x75/0d/22/74/3.jpg',
            'http://media-cache-ec0.pinimg.com/75x75/b0/42/c2/6.jpg'
        ], user.pin_thumbnail_urls)

        user.repins_from = []
        self.assertEqual([], user.repins_from)

        user.followed_boards = []
        self.assertEqual([], user.followed_boards)

        user.image_small_url = 'http://media-cache-ak0.pinimg.com/avatars/2321323_30.jpg'
        self.assertEqual('http://media-cache-ak0.pinimg.com/avatars/2321323_30.jpg', user.image_small_url)

        user.image_medium_url = 'http://media-cache-ak0.pinimg.com/avatars/242132_75.jpg'
        self.assertEqual('http://media-cache-ak0.pinimg.com/avatars/242132_75.jpg', user.image_medium_url)

        user.image_large_url = 'http://media-cache-ak0.pinimg.com/avatars/60916_140.jpg'
        self.assertEqual('http://media-cache-ak0.pinimg.com/avatars/60916_140.jpg', user.image_large_url)

        user.is_default_image = False
        self.assertEqual(False, user.is_default_image)

        user.has_password = True
        self.assertEqual(True, user.has_password)

        user.is_employee = False
        self.assertEqual(False, user.is_employee)

        user.followed_by_me = False
        self.assertEqual(False, user.followed_by_me)

        user.domain_verified = False
        self.assertEqual(False, user.domain_verified)

        user.explicitly_followed_by_me = False
        self.assertEqual(False, user.explicitly_followed_by_me)

        user.implicitly_followed_by_me = False
        self.assertEqual(False, user.implicitly_followed_by_me)

        user.blocked_by_me = False
        self.assertEqual(False, user.blocked_by_me)

        user.gplus_url = None
        self.assertEqual(None, user.gplus_url)

        user.domain_url = None
        self.assertEqual(None, user.domain_url)

        user.is_partner = False
        self.assertEqual(False, user.is_partner)

        user.partner = None
        self.assertEqual(None, user.partner)

        user.indexed = True
        self.assertEqual(True, user.indexed)

        user.website_url = None
        self.assertEqual(None, user.website_url)

        user.latest_category = [
            {
                'token': 'weddings',
                'display': 'Weddings'
            }
        ]
        self.assertEqual([
            {
                'token': 'weddings',
                'display': 'Weddings'
            }
        ], user.latest_category)

        user.ads_customize_from_conversion = True
        self.assertEqual(True, user.ads_customize_from_conversion)

        user.low_engagement_board_count = 100
        self.assertEqual(100, user.low_engagement_board_count)

        user.personalize_from_offsite_browsing = True
        self.assertEqual(True, user.personalize_from_offsite_browsing)

        user.verified_domains = []
        self.assertEqual([], user.verified_domains)

        user.tag = None
        self.assertEqual(None, user.tag)

        user.debug = None
        self.assertEqual(None, user.debug)

        user.created_at = 'Sun 09 Dec 2015 12:28:12 +0000'
        self.assertEqual('Sun 09 Dec 2015 12:28:12 +0000', user.created_at)

    def testAsDict(self):
        """
        Tests the pinterest.User asDict method
        """
        user = self._get_sample_user()
        data = user.asDict()
        self.assertEqual('171911222222223333', data['id'])
        self.assertEqual('Test', data['first_name'])
        self.assertEqual('Test', data['last_name'])
        self.assertEqual('Test User', data['full_name'])
        self.assertEqual(12, data['following_count'])
        self.assertEqual(132, data['follower_count'])
        self.assertEqual(211, data['pin_count'])
        self.assertEqual(10, data['board_count'])
        self.assertEqual(8, data['like_count'])
        self.assertEqual('test@gmail.com', data['email'])
        self.assertEqual(True, data['email_verified'])
        self.assertEqual(None, data['email_verification_code'])
        self.assertEqual('test', data['username'])
        self.assertEqual('', data['about'])
        self.assertEqual('', data['location'])
        self.assertEqual('user', data['type'])
        self.assertEqual([], data['pins'])
        self.assertEqual([
            'http://media-cache-ak0.pinimg.com/75x75/6c/77/80/8.jpg',
            'http://media-cache-ak0.pinimg.com/75x75/4f/ea/fc/7.jpg',
            'http://media-cache-ec0.pinimg.com/75x75/68/0f/c2/3.jpg',
            'http://media-cache-ec0.pinimg.com/75x75/0d/22/74/3.jpg',
            'http://media-cache-ec0.pinimg.com/75x75/b0/42/c2/6.jpg'
        ], data['pin_thumbnail_urls'])
        self.assertEqual([], data['repins_from'])
        self.assertEqual([], data['followed_boards'])
        self.assertEqual('http://media-cache-ak0.pinimg.com/avatars/2321323_30.jpg', data['image_small_url'])
        self.assertEqual('http://media-cache-ak0.pinimg.com/avatars/242132_75.jpg', data['image_medium_url'])
        self.assertEqual('http://media-cache-ak0.pinimg.com/avatars/60916_140.jpg', data['image_large_url'])
        self.assertEqual(False, data['is_default_image'])
        self.assertEqual(True, data['has_password'])
        self.assertEqual(False, data['is_employee'])
        self.assertEqual(False, data['followed_by_me'])
        self.assertEqual(False, data['domain_verified'])
        self.assertEqual(False, data['explicitly_followed_by_me'])
        self.assertEqual(False, data['implicitly_followed_by_me'])
        self.assertEqual(False, data['blocked_by_me'])
        self.assertEqual(None, data['gplus_url'])
        self.assertEqual(None, data['domain_url'])
        self.assertEqual(False, data['is_partner'])
        self.assertEqual(None, data['partner'])
        self.assertEqual(True, data['indexed'])
        self.assertEqual(None, data['website_url'])
        self.assertEqual([
            {
                'token': 'weddings',
                'display': 'Weddings'
            }
        ], data['latest_category'])
        self.assertEqual(True, data['ads_customize_from_conversion'])
        self.assertEqual(100, data['low_engagement_board_count'])
        self.assertEqual(True, data['personalize_from_offsite_browsing'])
        self.assertEqual([], data['verified_domains'])
        self.assertEqual(None, data['tag'])
        self.assertEqual(None, data['debug'])
        self.assertEqual('Sun, 09 Dec 2015 12:28:12 +0000', data['created_at'])

    def testEq(self):
        """
        Tests the pinterest.User __eq__ method
        """
        user = pinterest.User()
        user.id = '171911222222223333'
        user.first_name = 'Test'
        user.last_name = 'Test'
        user.full_name = 'Test User'
        user.following_count = 12
        user.follower_count = 132
        user.pin_count = 211
        user.board_count = 10
        user.like_count = 8
        user.email = 'test@gmail.com'
        user.email_verified = True
        user.email_verification_code = None
        user.username = 'test'
        user.about = ''
        user.location = ''
        user.type = 'user'
        user.pins = []
        user.pin_thumbnail_urls = [
            'http://media-cache-ak0.pinimg.com/75x75/6c/77/80/8.jpg',
            'http://media-cache-ak0.pinimg.com/75x75/4f/ea/fc/7.jpg',
            'http://media-cache-ec0.pinimg.com/75x75/68/0f/c2/3.jpg',
            'http://media-cache-ec0.pinimg.com/75x75/0d/22/74/3.jpg',
            'http://media-cache-ec0.pinimg.com/75x75/b0/42/c2/6.jpg'
        ]
        user.repins_from = []
        user.followed_boards = []
        user.image_small_url = 'http://media-cache-ak0.pinimg.com/avatars/2321323_30.jpg'
        user.image_medium_url = 'http://media-cache-ak0.pinimg.com/avatars/242132_75.jpg'
        user.image_large_url = 'http://media-cache-ak0.pinimg.com/avatars/60916_140.jpg'
        user.is_default_image = False
        user.has_password = True
        user.is_employee = False
        user.followed_by_me = False
        user.domain_verified = False
        user.explicitly_followed_by_me = False
        user.implicitly_followed_by_me = False
        user.blocked_by_me = False
        user.gplus_url = None
        user.domain_url = None
        user.is_partner = False
        user.partner = None
        user.indexed = True
        user.website_url = None
        user.latest_category = [
            {
                'token': 'weddings',
                'display': 'Weddings'
            }
        ]
        user.ads_customize_from_conversion = True
        user.low_engagement_board_count = 100
        user.personalize_from_offsite_browsing = True
        user.verified_domains = []
        user.tag = None
        user.debug = None
        user.created_at = 'Sun, 09 Dec 2015 12:28:12 +0000'
        self.assertEqual(user, self._get_sample_user())

    def testNewFromJsonDict(self):
        """
        Tests the pinterest.User newFromJsonDict
        """
        data = json.loads(UserTest.SAMPLE_JSON)
        status = pinterest.User.newFromJsonDict(data)
        self.assertEqual(self._get_sample_user(), status)