import unittest
import prague_clocks as pc
import pdb
import warnings

example_modulo = 15
example_triangular_num_list = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105]
example_modulo_list = [0, 1, 3, 6, 10, 13, 15]
example_prague_clock = [1, 2, 3, 4, 3, 2]
example_demo_hour = 6
example_demo = [[1], [2], [3], [4], [3, 2], [1, 2, 3]]

class prague_clock_tests(unittest.TestCase):
    def test001_triangular_num_list(self):
        self.assertEqual(
            example_triangular_num_list,
            pc.triangular_num_list(example_modulo)
        )

    def test002_modulo_list(self):
        self.assertEqual(
            example_modulo_list,
            pc.modulo_list(example_modulo)
        )

    def test003_modulo_list(self):
        self.assertEqual(
            example_modulo_list,
            pc.modulo_list(example_modulo, example_triangular_num_list)
        )

    def test004_prague_clock(self):
        self.assertEqual(
            example_prague_clock,
            pc.prague_clock(num_list=example_modulo_list)
        )

    def test005_prague_clock_end_to_end(self):
        self.assertEqual(
            example_prague_clock,
            pc.prague_clock(example_modulo)
        )

    def test006_prague_clock_warning(self):
        with self.assertRaises(UserWarning) as e:
#             with warnings.simplefilter('error'):
                pc.prague_clock(**{'modulo' : example_modulo, 'num_list' : example_modulo_list})

    def test007_demo(self):
        self.assertEqual(
            example_demo,
            pc.demo(example_demo_hour, example_prague_clock)
        )

if __name__ == '__main__':
        pdb.set_trace()
        unittest.main()