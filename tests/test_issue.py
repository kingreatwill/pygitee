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

    def test_create(self):
        instance = Issue(access_token='x')
        print(instance.create('kingreatwill', 'kingreatwill', 'api create v2',body="增加body描述"))

    def test_update(self):
        instance = Issue(access_token='x')
        print(instance.update('kingreatwill', 'kingreatwill', 'I1TYID',body="增加body描述 updated"))