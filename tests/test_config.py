import os
import unittest

import doto
from doto import Config


doto_path = os.path.join(os.path.dirname(doto.__file__),'dotorc')
config = Config(doto_path)

class TestConfig(unittest.TestCase):

    def test_glob(self):
        self.assertEqual(config.get('Credentials','client_id'),'XXXXXXXXXXXXX')
        self.assertEqual(config.get('Credentials','api_key'),\
                         '99999999999999999999999')

if __name__ == '__main__':
    unittest.main()