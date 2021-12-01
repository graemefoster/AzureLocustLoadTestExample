from locust import HttpUser, task, between
from json import JSONDecodeError, loads
import http.client


class QuickstartUser(HttpUser):
    wait_time = between(0.2, 0.5)

    @task
    def call_api(self):
        postcode = "6000".zfill(4)
        api = "/weather/forecast?postcode=" + postcode

        with self.client.get(api, catch_response=True) as response:
            try:
                if response.json()["postcode"] != postcode:
                    response.failure("Did not get expected postcode in weather result")
            except JSONDecodeError:
                    response.failure("Response from " + api + " could not be decoded as JSON:" + response.text)

    def on_start(self):
        # conn = http.client.HTTPSConnection("identityserverfwkmqd2jwtbwo.azurewebsites.net")
        # payload = "grant_type=client_credentials&client_id=frontend-1&client_secret=frontend-secret&scope=employee-apis"
        # headers = { 'content-type': "application/x-www-form-urlencoded" }
        # conn.request("POST", "/connect/token", payload, headers)
        # res = conn.getresponse()
        # data = res.read()
        # token = loads(data.decode("utf-8"))

        # self.client.headers.update({'Authorization' : 'Bearer ' + token["access_token"]})
        self.client.headers.update({'ocp-apim-subscription-key' : '<key>'})

