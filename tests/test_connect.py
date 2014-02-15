import os
import unittest

import doto

d0 = doto.connect_d0()

class TestConfig(unittest.TestCase):

    def test_get_all_droplets(self):
        self.assertEqual(d0.get_all_droplets(status_check=True),200)
        self.assertEqual(d0.get_sizes(status_check=True),200)
        self.assertEqual(d0.get_images(status_check=True),200)
        self.assertEqual(d0.get_domains(status_check=True),200)
        self.assertEqual(d0.get_regions(status_check=True),200)
        self.assertEqual(d0.get_ssh_keys(status_check=True),200)

if __name__ == '__main__':
    unittest.main()


droplet.power_off()
while droplet.event_status != 'done':
    droplet.event_update()