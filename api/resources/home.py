import os
import json
import falcon
import logging
import requests

from datetime import datetime
from decimal import Decimal
from requests.exceptions import HTTPError


class Home:
    def __init__(self):
        self.logger = logging.getLogger('thingsapp.' + __name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(name)s - %(message)s')

        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def on_get(self, req, res):
        self.logger.info(f'Start: GET')
        res.status = falcon.get_http_status(status_code=200)
        try:
            response = requests.get('http://www.mocky.io/v2/5ea8c3162d0000644f3a40f0')
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Other error occurred: {err}')

        response_dict = response.json()

        # print("Recebido GET em {}".format(datetime.utcnow().isoformat()))
        # response_dict = {
        #     "company": "qi_tech",
        #     "proccess_id": str(os.getpid())
        # }

        res.body = json.dumps(response_dict)
        self.logger.info(f'End.')

    def on_post(self, req, res):
        self.logger.info(f'Start: POST')
        body = req.stream.read(req.content_length or 0)
        body = json.loads(body.decode('utf-8'), parse_float=Decimal)
        # print("Recebido POST em {}".format(datetime.utcnow().isoformat()))
        res.status = falcon.get_http_status(status_code=200)
        response_dict = {
            "company": "qi_tech",
            "proccess_id": str(os.getpid()),
            "body": body
        }
        res.body = json.dumps(response_dict)
        self.logger.info(f'End.')
