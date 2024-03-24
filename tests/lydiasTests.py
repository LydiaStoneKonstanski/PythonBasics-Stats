import statistics
import unittest.mock
from statzcw import statszcw
import numpy as np
class StatsZcwTests(unittest.TestCase):
    def test_zcount(self):
        case = [1.0, 1.0, 1.0]
        self.assertEqual(3.0, statszcw.zcount(case))


    def test_zmean(self):
        case = [1.0, 2.0, 3.0]
        self.assertEqual(2.0, statszcw.zmean(case))


    def test_zmode(self):
        case = [1.0, 2.0, 3.0, 3.0]
        self.assertEqual(3.0, statszcw.zmode(case))


    def test_zmedian(self):
        case = [1.0, 2.0, 3.0, 3.0, 1.0]
        self.assertEqual(2.0, statszcw.zmedian(case))


    def test_zvariance(self):
        case = [1.0, 2.0, 3.0, 3.0, 1.0]
        self.assertEqual(1.0, statszcw.zvariance(case))


    def test_zstddev(self):
        case = [1.0, 2.0, 3.0, 3.0, 1.0]
        self.assertEqual(1.0, statszcw.zstddev(case))


    def test_zstderr(self):
        case = [1.0, 2.0, 3.0, 3.0, 1.0]
        self.assertAlmostEqual(0.447213595499916, statszcw.zstderr(case), 6)


    def test_cov(self):
        case_x, case_y = [1.0, 2.0, 3.0], [4.0, 5.0, 6.0]
        self.assertAlmostEqual(1, statszcw.cov(case_x, case_y), 6)


    def test_cov_error(self):
        case_x, case_y = [1.0, 2.0, 3.0], [4.0, 5.0]
        self.assertRaises(ValueError, statszcw.cov, case_x, case_y)


    def test_corr(self):
        case_x, case_y = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0], [4.0, 5.0, 6.0, 7.0, 8.0]
        self.assertRaises(ValueError, statszcw.zcorr, case_x, case_y)