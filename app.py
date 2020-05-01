import falcon
from api.resources.home import Home
from api.resources.report import Report


def create():
    api = falcon.API()
    api.add_route('/', Home())
    api.add_route('/report', Report())
    return api


app = application = create()
