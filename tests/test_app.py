# -*- coding: utf-8 -*-
import unittest

import requests


class TestAPI(unittest.TestCase):
    def test_hello(self):
        payload = {
            'grant_type': 'authorization_code',
            'redirect_uri': 'http://xxx.xyz.com/request_listener',
        }

        url = 'https://www.telelicense.site/'

        response: requests.Response = requests.get(url, data=payload, verify=True)
        print(response.content)


if __name__ == "__main__":
    unittest.main()
