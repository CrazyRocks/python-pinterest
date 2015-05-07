# encoding: utf-8

import pinterest
import unittest
import json


class DomainTest(unittest.TestCase):
    """
    Domain model unit tests
    """

    SAMPLE_JSON = '''{
      "thumbnails": [
        "https://s-media-cache-ak0.pinimg.com/45x45/76/45/50/764550383dd456233a1722c5d8332392.jpg",
        "https://s-media-cache-ak0.pinimg.com/45x45/45/87/8c/45878c9750634f229a181f494c2e0588.jpg",
        "https://s-media-cache-ak0.pinimg.com/45x45/e3/2b/da/e32bda99fc4a67e27207bda7483db5d1.jpg",
        "https://s-media-cache-ak0.pinimg.com/45x45/aa/83/52/aa8352eb4526720b45ea7ef71fdc396f.jpg",
        "https://s-media-cache-ak0.pinimg.com/45x45/69/ba/17/69ba17bb8e261982f60e4a326001812a.jpg"
      ],
      "type": "domain",
      "favicon": "http://www.google.com/s2/favicons?domain=pinterest.com",
      "access": [
        "view_analysis"
      ],
      "client_details": {},
      "id": "123456789",
      "name": "pinterest.com"
    }'''

    def _get_sample_domain(self):
        """
        Builds a sample domain
        :return: Returns an instance of pinterest.Domain
        """
        return pinterest.Domain(id='123456789',
                                name='pinterest.com',
                                type='domain',
                                favicon='http://www.google.com/s2/favicons?domain=pinterest.com',
                                thumbnails=[
                                    'https://s-media-cache-ak0.pinimg.com/45x45/76/45/50/764550383dd456233a1722c5d8332392.jpg',
                                    'https://s-media-cache-ak0.pinimg.com/45x45/45/87/8c/45878c9750634f229a181f494c2e0588.jpg',
                                    'https://s-media-cache-ak0.pinimg.com/45x45/e3/2b/da/e32bda99fc4a67e27207bda7483db5d1.jpg',
                                    'https://s-media-cache-ak0.pinimg.com/45x45/aa/83/52/aa8352eb4526720b45ea7ef71fdc396f.jpg',
                                    'https://s-media-cache-ak0.pinimg.com/45x45/69/ba/17/69ba17bb8e261982f60e4a326001812a.jpg'
                                ],
                                access=['view_analysis'],
                                client_details={})

    def testInit(self):
        """
        Tests the pinterest.Domain constructor
        :return:
        """
        domain = pinterest.Domain(id='123456789',
                                  name='pinterest.com',
                                  type='domain',
                                  favicon='http://www.google.com/s2/favicons?domain=pinterest.com',
                                  thumbnails=[
                                      'https://s-media-cache-ak0.pinimg.com/45x45/76/45/50/764550383dd456233a1722c5d8332392.jpg',
                                      'https://s-media-cache-ak0.pinimg.com/45x45/45/87/8c/45878c9750634f229a181f494c2e0588.jpg',
                                      'https://s-media-cache-ak0.pinimg.com/45x45/e3/2b/da/e32bda99fc4a67e27207bda7483db5d1.jpg',
                                      'https://s-media-cache-ak0.pinimg.com/45x45/aa/83/52/aa8352eb4526720b45ea7ef71fdc396f.jpg',
                                      'https://s-media-cache-ak0.pinimg.com/45x45/69/ba/17/69ba17bb8e261982f60e4a326001812a.jpg'
                                  ],
                                  access=['view_analysis'],
                                  client_details={})
        self.assertIsInstance(domain, pinterest.Domain)

    def testProperties(self):
        """
        Tests all of the pinterest.Domain properties
        """
        domain = pinterest.Domain()
        domain.id = '123456789'
        self.assertEqual('123456789', domain.id)

        domain.name = 'pinterest.com'
        self.assertEqual('pinterest.com', domain.name)

        domain.type = 'domain'
        self.assertEqual('domain', domain.type)

        domain.favicon = 'http://www.google.com/s2/favicons?domain=pinterest.com'
        self.assertEqual('http://www.google.com/s2/favicons?domain=pinterest.com', domain.favicon)

        domain.thumbnails = [
            'https://s-media-cache-ak0.pinimg.com/45x45/76/45/50/764550383dd456233a1722c5d8332392.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/45/87/8c/45878c9750634f229a181f494c2e0588.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/e3/2b/da/e32bda99fc4a67e27207bda7483db5d1.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/aa/83/52/aa8352eb4526720b45ea7ef71fdc396f.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/69/ba/17/69ba17bb8e261982f60e4a326001812a.jpg']
        self.assertEqual([
            'https://s-media-cache-ak0.pinimg.com/45x45/76/45/50/764550383dd456233a1722c5d8332392.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/45/87/8c/45878c9750634f229a181f494c2e0588.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/e3/2b/da/e32bda99fc4a67e27207bda7483db5d1.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/aa/83/52/aa8352eb4526720b45ea7ef71fdc396f.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/69/ba/17/69ba17bb8e261982f60e4a326001812a.jpg'],
            domain.thumbnails)

        domain.access = ['view_analysis']
        self.assertEqual(['view_analysis'], domain.access)

        domain.client_details = {}
        self.assertEqual({}, domain.client_details)

    def testAsDict(self):
        """
        Tests the pinterest.Domain asDict method
        """
        domain = self._get_sample_domain()
        data = domain.asDict()
        self.assertEqual('123456789', data['id'])
        self.assertEqual('pinterest.com', data['name'])
        self.assertEqual('domain', data['type'])
        self.assertEqual('http://www.google.com/s2/favicons?domain=pinterest.com', data['favicon'])
        self.assertEqual([
            'https://s-media-cache-ak0.pinimg.com/45x45/76/45/50/764550383dd456233a1722c5d8332392.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/45/87/8c/45878c9750634f229a181f494c2e0588.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/e3/2b/da/e32bda99fc4a67e27207bda7483db5d1.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/aa/83/52/aa8352eb4526720b45ea7ef71fdc396f.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/69/ba/17/69ba17bb8e261982f60e4a326001812a.jpg'],
            data['thumbnails'])
        self.assertEqual(['view_analysis'], data['access'])
        self.assertEqual({}, data['client_details'])

    def testEq(self):
        """
        Tests the pinterest.Domain __eq__ method
        """
        domain = pinterest.Domain()
        domain.id = '123456789'
        domain.name = 'pinterest.com'
        domain.type = 'domain'
        domain.favicon = 'http://www.google.com/s2/favicons?domain=pinterest.com'
        domain.thumbnails = [
            'https://s-media-cache-ak0.pinimg.com/45x45/76/45/50/764550383dd456233a1722c5d8332392.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/45/87/8c/45878c9750634f229a181f494c2e0588.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/e3/2b/da/e32bda99fc4a67e27207bda7483db5d1.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/aa/83/52/aa8352eb4526720b45ea7ef71fdc396f.jpg',
            'https://s-media-cache-ak0.pinimg.com/45x45/69/ba/17/69ba17bb8e261982f60e4a326001812a.jpg']
        domain.access = ['view_analysis']
        domain.client_details = {}
        self.assertEqual(domain, self._get_sample_domain())

    def testNewFromJsonDict(self):
        """
        Tests the pinterest.Domain newFromJsonDict
        """
        data = json.loads(DomainTest.SAMPLE_JSON)
        status = pinterest.Domain.newFromJsonDict(data)
        self.assertEqual(self._get_sample_domain(), status)