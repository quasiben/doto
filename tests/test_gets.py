import doto
import unittest



class TestMetaGets(unittest.TestCase):

    def test_gets(self):
        d0 = doto.connect_d0()
        self.assertEqual(d0.get_all_ssh_keys(status_check=True),200)
        self.assertEqual(d0.get_all_regions(status_check=True),200)
        self.assertEqual(d0.get_sizes(status_check=True),200)
        self.assertEqual(d0.get_all_droplets(status_check=True),200)
        self.assertEqual(d0.get_all_images(status_check=True),200)
        self.assertEqual(d0.get_domains(status_check=True),200)


if __name__ == '__main__':
    unittest.main()
