import unittest

from gitee.issue import Issue


class Test_Issue(unittest.TestCase):
    def setUp(self):
        ...

    def tearDown(self):
        ...

    def test_list(self):
        instance = Issue()
        print(instance.list('kingreatwill', 'kingreatwill'))

    def test_get(self):
        instance = Issue()
        print(instance.get('kingreatwill', 'kingreatwill','I1TXFW'))
