import unittest

import test_actions


class TestSourceCode(unittest.TestCase):
    def test_version(self):
        print(test_actions.__version__)
