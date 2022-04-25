# -*- coding: utf-8 -*-

from .context import log_speedtest, plot_speedtest

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts_log_speedtest(self):
        self.assertIsNone(log_speedtest.main())

    def test_thoughts_plot_speedtest(self):
        self.assertIsNone(plot_speedtest.main())


if __name__ == '__main__':
    unittest.main()