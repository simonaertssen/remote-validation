# -*- coding: utf-8 -*-
import unittest

import requests


class TestAPI(unittest.TestCase):
    def test_hello(self):
        payload = {
            'grant_type': 'authorization_code',
            'redirect_uri': 'http://xxx.xyz.com/request_listener',
        }

        url = 'https://127.0.0.1:5000'

        response = requests.post(url, data=payload, verify=True)
        print(response)


if __name__ == "__main__":
    unittest.main()
