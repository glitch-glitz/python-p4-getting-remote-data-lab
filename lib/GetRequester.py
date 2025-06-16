import requests
import json

# class GetRequester:

#     def __init__(self, url):
#         self.url = url  # Store the URL(where to fetch data) provided during initialization

#     def get_response_body(self):
#         # Send GET request to the stored URL
#         response = requests.get(self.url)
#         # Return the raw response content as text
#         return response.text

#     def load_json(self):
#         # Get the response body text
#         response_body = self.get_response_body()
#         # Parse the JSON string into Python objects
#         return json.loads(response_body)


class GetRequester:
    # initialize with a string URL
    def __init__(self, url):
        self.url = url

    # method that sends a GET request to the URL passed in on initialization and return the body of the response.
    def get_response_body(self):
        response = requests.get(self.url)

        return response.content

    # send a request, then return a Python list or dictionary made up of data converted from the response of that request.
    def load_json(self):
        person_info = []
        info = json.loads(self.get_response_body())
        for i in info:
            person_info.append(i)

        return person_info
        # return [elem for elem in json.loads(self.get_response_body())]
        # return json.loads(self.get_response_body())


requester = GetRequester(
    url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
)
requester.load_json()
