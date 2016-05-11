import unittest
import prague_clocks as pc
import pdb

example_m = 15
example_triangular_num_list = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105]
example_modulo_list = [0, 1, 3, 6, 10, 13, 15]
example_sorted_list_diff = [1, 2, 3, 4, 3, 2]

class prague_clock_tests(unittest.TestCase):
    def test001_triangular_num_list(self):
        self.assertEqual(
            example_triangular_num_list,
            pc.triangular_num_list(example_m)
        )

    def test002_modulo_list(self):
        self.assertEqual(
            example_modulo_list,
            pc.modulo_list(example_m)
        )

    def test003_modulo_list(self):
        self.assertEqual(
            example_modulo_list,
            pc.modulo_list(example_m, example_triangular_num_list)
        )

    def test004_sorted_list_diff(self):
        self.assertEqual(
            example_sorted_list_diff,
            pc.sorted_list_diff(example_modulo_list)
        )


if __name__ == '__main__':
        pdb.set_trace()
        unittest.main()