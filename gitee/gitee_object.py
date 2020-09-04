import typing
from dataclasses import dataclass

import requests


@dataclass
class Response(object):
    ok: bool
    code: int
    data: typing.Any
    message: str


class GiteeObject(object):
    def __init__(self, access_token=''):
        self.access_token = access_token

    @property
    def base_url(self):
        return 'https://gitee.com/api/'

    @property
    def version(self):
        return 'v5'

    def do_get(self, url, params: dict = None):
        req_url = self.base_url + self.version + url

        if self.access_token:
            if not params:
                params = {}
            params.setdefault('access_token', self.access_token)

        resp = requests.get(req_url, params=params)
        if resp.ok:
            return Response(True, resp.status_code, resp.json(), '')
        return Response(False, resp.status_code, None, resp.text)
