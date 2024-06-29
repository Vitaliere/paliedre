import unittest
from unittest.mock import patch, mock_open

from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """100.0	0.0	 0.0	0.0
4   1 	4
0	0	0
0	1   0
0	1	1
0	0	1
4	1    2    3    4
"""
        fake_file_path = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 4)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 1)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 4)

    def test_summa_area(self):
        self.assertAlmostEqual(self.polyedr.sum, 0)
