import falcon
import os
from wsgiref import simple_server

import requests
from requests.auth import _basic_auth_str as basic_auth_str

AUTH = basic_auth_str(
    os.environ.get("BASIC_USERNAME"),
    os.environ.get("BASIC_PASS"))
URL = os.environ.get("DEST_URL")


class Forward(object):
    def __call__(self, req, resp):
        headers = req.headers.copy()
        headers["AUTHORIZATION"] = AUTH
        params = req.params
        method = req.method
        url = "{0}{1}".format(URL, req.path)
        data = req.stream.read()
        r = requests.request(
            method, url, params=params, headers=headers, data=data,
            verify=False)
        resp.headers = r.headers
        resp.status = "{0} {1}".format(str(r.status_code), r.reason)
        resp.body = r.content


api = falcon.API()
api.add_sink(Forward(), "/.*")


if __name__ == '__main__':
    httpd = simple_server.make_server("0.0.0.0", 8000, api)
    httpd.serve_forever()
