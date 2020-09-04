import unittest

from gitee import Gitee


class Test_Issue(unittest.TestCase):
    def setUp(self):
        ...

    def tearDown(self):
        ...

    def test_list(self):
        g = Gitee()
        print(g.get_issues().list('kingreatwill', 'kingreatwill'))
