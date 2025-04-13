import unittest

import drodarie_test_actions


class TestSourceCode(unittest.TestCase):
    def test_version(self):
        print(drodarie_test_actions.__version__)
